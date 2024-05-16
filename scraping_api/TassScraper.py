import re

import requests

from grpc_api.protos import news_getter_pb2
from scraping_api.ScraperInterface import ScraperInterface
from scraping_api.models.news_full_info import NewsFullInfo
from scraping_api.models.news_short_info import NewsShortInfo


class TassScraper(ScraperInterface):
    def get_news(self, url: str) -> NewsFullInfo | None:
        soup = super()._get_content_v2(url)

        title = soup.find("h1", {"class": "tass_pkg_title-xVUT1"}).text

        image_body = soup.find("img", {"class": "ImageSSR_image__5T3Id"})
        image = None

        if image_body:
            image = image_body.get("src")

        content = ""
        article_body = soup.find('article')

        if article_body:
            for unwanted_div in article_body.find_all('div', class_=re.compile('^ExternalBlock')):
                unwanted_div.decompose()

        if article_body:
            content = super()._remove_inner_html_tags(article_body.text.strip())

        if content == '':
            return None

        return NewsFullInfo(url=url, title=title, content=content, images=[image] if image is not None else [],
                            source_type=news_getter_pb2.Site.Tass)

    def get_articles(self, page: int) -> list[NewsShortInfo]:
        return super().get_articles(page)
