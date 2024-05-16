from grpc_api.protos import news_getter_pb2
from scraping_api.ScraperInterface import ScraperInterface
from scraping_api.models.news_full_info import NewsFullInfo
from scraping_api.models.news_short_info import NewsShortInfo


class CNNScraper(ScraperInterface):
    def get_news(self, url: str) -> NewsFullInfo | None:
        soup = super()._get_content(url)

        title = soup.find("h1", {"id": "maincontent"}).text.strip()

        image_body = soup.find("div", {"class": "image__lede"})
        image = None

        if image_body:
            image = image_body.find("div", {"data-component-name": "image"}).get("data-url")

        article_body = soup.find('div', itemprop='articleBody')
        content = ""

        if article_body:
            for unwanted_div in article_body.find_all('div', class_='related-content'):
                unwanted_div.decompose()

        if article_body:
            paragraphs = article_body.find_all('p')
            for p in paragraphs:
                content += p.text.strip() + "\n"

        if content == "":
            return None

        return NewsFullInfo(url=url, title=title, content=content, images=[image] if image is not None else [],
                            source_type=news_getter_pb2.Site.CNN)

    def get_articles(self, page: int) -> list[NewsShortInfo]:
        return super().get_articles(page)
