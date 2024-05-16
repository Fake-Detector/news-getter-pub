import logging
import grpc
from grpc_reflection.v1alpha import reflection
from concurrent import futures

from grpc_api.protos import news_getter_pb2_grpc, news_getter_pb2
from grpc_api.services.news_getter_service import NewsGetterService
from scraping_api.ScrapperFactory import get_news_scraper
from yandex_api.search_api import SearchApi

import requests
from bs4 import BeautifulSoup


def service_init():
    logging.info(f"Start service init")
    search_api = SearchApi()

    return NewsGetterService(search_api=search_api)


def main():
    logging.basicConfig(level=logging.DEBUG)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service = service_init()
    news_getter_pb2_grpc.add_NewsGetterServicer_to_server(service, server)

    service_names = (
        news_getter_pb2.DESCRIPTOR.services_by_name['NewsGetter'].full_name,
        reflection.SERVICE_NAME
    )

    reflection.enable_server_reflection(service_names, server)
    port = 50052
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    logging.info(f"Server started on {port} port")
    server.wait_for_termination()


if __name__ == '__main__':
    main()
