from grpc_api.protos import news_getter_pb2
from scraping_api.BBCScraper import BBCScraper
from scraping_api.CNNScrapper import CNNScraper
from scraping_api.InterfaxScraper import InterfaxScraper
from scraping_api.IzRuScraper import IzRuScraper
from scraping_api.LentaRuScraper import LentaRuScraper
from scraping_api.RiaScraper import RiaScraper
from scraping_api.ScraperInterface import ScraperInterface
from scraping_api.TassScraper import TassScraper


def get_news_scraper(type: news_getter_pb2.Site) -> ScraperInterface:
    match type:
        case news_getter_pb2.Site.LentaRu:
            return LentaRuScraper()
        case news_getter_pb2.Site.IzRu:
            return IzRuScraper()
        case news_getter_pb2.Site.Ria:
            return RiaScraper()
        case news_getter_pb2.Site.Interfax:
            return InterfaxScraper()
        case news_getter_pb2.Site.Tass:
            return TassScraper()
        case news_getter_pb2.Site.BBC:
            return BBCScraper()
        case news_getter_pb2.Site.CNN:
            return CNNScraper()
