from grpc_api.protos import news_getter_pb2
from scraping_api.ScraperInterface import ScraperInterface
from scraping_api.models.news_full_info import NewsFullInfo
from scraping_api.models.news_short_info import NewsShortInfo


class IzRuScraper(ScraperInterface):
    def get_news(self, url: str) -> NewsFullInfo | None:
        soup = super()._get_content(url)

        title_body = soup.find("h1", itemprop="headline")
        title = ""
        if title_body:
            title = title_body.find("span").text

        content = ""
        article_body = soup.find('div', itemprop='articleBody')

        if article_body is None:
            article_body = soup.find("div", {"class": "text-article"}).find('div', itemprop='description')

        if article_body:
            for unwanted_div in article_body.find_all('div', class_=['more_style_one', 'slider-block2__inside__item']):
                unwanted_div.decompose()

        if article_body:
            paragraphs = article_body.find_all('p')
            for p in paragraphs:
                content += super()._remove_inner_html_tags(p.text.strip()) + "\n"

        if content == '':
            return None

        return NewsFullInfo(url=url, title=title, content=content, source_type=news_getter_pb2.Site.IzRu)

    def get_articles(self, page: int) -> list[NewsShortInfo]:
        return super().get_articles(page)
