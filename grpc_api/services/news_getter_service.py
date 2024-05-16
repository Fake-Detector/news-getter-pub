from grpc_api.models.website import website_url, website_url_regex
from grpc_api.protos import news_getter_pb2, news_getter_pb2_grpc
from scraping_api.ScraperInterface import ScraperInterface
from scraping_api.ScrapperFactory import get_news_scraper
from yandex_api.search_api import SearchApi

import re


class NewsGetterService(news_getter_pb2_grpc.NewsGetterServicer):
    def __init__(self, search_api: SearchApi):
        self.search_api = search_api

    def SearchNews(self, request, context):
        try:
            links = self.search_api.get_links(
                request.query,
                list(set([website_url[name] for name in request.sites])),
                request.max_site_links)

            return news_getter_pb2.SearchNewsResponse(links=links)
        except Exception as error:
            print("SearchNews: ", error)
            return news_getter_pb2.SearchNewsResponse(links=[])

    def GetNewsContent(self, request, context):
        try:
            scraper = self.get_scraper(request)
            if scraper is None:
                return news_getter_pb2.GetNewsContentResponse(is_success=False)

            news = scraper.get_news(request.url)
            if news is None:
                return news_getter_pb2.GetNewsContentResponse(is_success=False)

            return news_getter_pb2.GetNewsContentResponse(is_success=True, url=news.url, title=news.title,
                                                          content=news.content, images=news.images, videos=news.videos,
                                                          source_type=news.source_type)
        except Exception as error:
            print("GetNewsContent: ", error)
            return news_getter_pb2.GetNewsContentResponse(is_success=False)

    @staticmethod
    def get_scraper(request) -> ScraperInterface | None:
        if request.scraper == news_getter_pb2.Site.AutoDetect:
            for site in website_url_regex.keys():
                if re.search(website_url_regex[site], request.url):
                    return get_news_scraper(site)
        else:
            if re.search(website_url_regex[request.scraper], request.url):
                return get_news_scraper(request.scraper)

        return None

    def GetListNews(self, request, context):
        try:
            scraper = get_news_scraper(request.source_type)
            if scraper is None:
                return news_getter_pb2.GetListNewsResponse(news=[])

            news = scraper.get_articles(request.page)
            if news is None:
                return news_getter_pb2.GetListNewsResponse(news=[])

            return news_getter_pb2.GetListNewsResponse(
                news=[news_getter_pb2.ShortNews(url=item.url, content=item.content) for item in news])
        except Exception as error:
            print("GetNewsContent: ", error)
            return news_getter_pb2.GetListNewsResponse(news=[])
