import re

from grpc_api.protos import news_getter_pb2
from scraping_api.ScraperInterface import ScraperInterface
from scraping_api.models.news_full_info import NewsFullInfo
from scraping_api.models.news_short_info import NewsShortInfo


class InterfaxScraper(ScraperInterface):
    def get_news(self, url: str) -> NewsFullInfo | None:
        soup = super()._get_content(url, encoding="cp1251")

        title = soup.find('title')
        image = None

        if title is not None:
            title = title.text.strip()
            image = soup.find('img', attrs={'alt': title})['src']
        else:
            title = ''

        article_block = soup.find('article')

        if article_block:
            for unwanted_div in article_block.find_all('div', class_=re.compile('^wg_news')):
                unwanted_div.decompose()
            for unwanted_div in article_block.find_all(['aside', 'figure']):
                unwanted_div.decompose()
            content = article_block.text.strip()
        else:
            return None

        return NewsFullInfo(url=url, title=title, content=content, images=[image] if image is not None else [],
                            source_type=news_getter_pb2.Site.Interfax)

    def get_articles(self, page: int) -> list[NewsShortInfo]:
        return super().get_articles(page)
