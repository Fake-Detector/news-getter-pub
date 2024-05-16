from grpc_api.protos import news_getter_pb2
from scraping_api.ScraperInterface import ScraperInterface
from scraping_api.models.news_full_info import NewsFullInfo
from scraping_api.models.news_short_info import NewsShortInfo


class RiaScraper(ScraperInterface):
    def get_news(self, url: str) -> NewsFullInfo | None:
        soup = super()._get_content(url)

        title_body = soup.find(["div", "h1"], {"class": "article__title"})
        title = ""
        if title_body:
            title = title_body.text

        image_body = soup.find("div", {"class": "article__header"})
        image = None

        if image_body:
            image = image_body.find("div", {"class": "photoview__open"}).get("data-photoview-src")

        content = ""
        article_body = soup.find('div', itemprop='articleBody')

        if article_body:
            content = super()._remove_inner_html_tags(article_body.text.strip())

        if content == '':
            return None

        return NewsFullInfo(url=url, title=title, content=content, images=[image] if image is not None else [],
                            source_type=news_getter_pb2.Site.Ria)

    def get_articles(self, page: int) -> list[NewsShortInfo]:
        return super().get_articles(page)
