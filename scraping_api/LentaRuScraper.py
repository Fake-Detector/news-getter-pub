import json

from grpc_api.protos import news_getter_pb2, news_getter_pb2_grpc
from scraping_api.ScraperInterface import ScraperInterface
from scraping_api.models.news_full_info import NewsFullInfo
from scraping_api.models.news_short_info import NewsShortInfo


class LentaRuScraper(ScraperInterface):
    def __init__(self):
        self.news_page_url = 'https://lenta.ru/parts/news/'
        self.news_main_url = 'https://lenta.ru'

    def get_news(self, url: str) -> NewsFullInfo | None:
        url = url.replace("m.lenta.ru", "lenta.ru")
        soup = super()._get_content(url)
        script_tag = soup.find('script', type='application/ld+json')

        if script_tag:
            json_content = json.loads(script_tag.string)
            url = json_content.get("url", "")
            title = json_content.get("name", "")
            content = json_content.get("articleBody", "")

            return NewsFullInfo(url=url, title=title, content=content, source_type=news_getter_pb2.Site.LentaRu)
        else:
            return None

    def get_articles(self, page: int) -> list[NewsShortInfo]:
        soup = super()._get_content(f"{self.news_page_url}{page}")

        page_parts = soup.findAll("li", {"class": "parts-page__item"})

        articles = []
        for page_part in page_parts:
            news_tag = page_part.find("a", {"class": "card-full-news _parts-news"})
            if news_tag:
                content_tag = news_tag.find("h3", {"class": "card-full-news__title"})
                if content_tag:
                    content = content_tag.text
                    url = news_tag.get("href", "")
                    if url != "":
                        articles.append(NewsShortInfo(url=f"{self.news_main_url}{url}", content=content))

        return articles
