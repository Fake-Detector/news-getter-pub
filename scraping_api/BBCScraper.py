import json

from grpc_api.protos import news_getter_pb2
from scraping_api.ScraperInterface import ScraperInterface
from scraping_api.models.news_full_info import NewsFullInfo
from scraping_api.models.news_short_info import NewsShortInfo


class BBCScraper(ScraperInterface):
    def get_news(self, url: str) -> NewsFullInfo | None:
        soup = super()._get_content(url)
        article_blocks = soup.findAll(['div'], attrs={'data-component': 'text-block'})
        content = ""
        title = ""

        if article_blocks:
            content = "".join([x.text + '\n' for x in article_blocks])

        script = soup.find("script", attrs={"id": "__NEXT_DATA__", "type": "application/json"})

        if script:
            json_content = json.loads(script.text).get("props", "").get("pageProps", "")
            page_key = json_content.get("pageKey", "")
            contents = json_content.get("page", "").get(page_key, "").get("contents", "")
            for item in contents:
                match item["type"]:
                    case "headline":
                        if title == "":
                            title = item["model"]["blocks"][0]["model"]["text"]
                    case "text":
                        content += item["model"]["blocks"][0]["model"]["text"] + '\n'
                    case "subheadline":
                        break

        if content == "":
            return None

        return NewsFullInfo(url=url, title=title, content=content, source_type=news_getter_pb2.Site.BBC)

    def get_articles(self, page: int) -> list[NewsShortInfo]:
        return super().get_articles(page)
