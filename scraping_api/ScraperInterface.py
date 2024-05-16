import requests
import urllib3

from scraping_api.models.news_full_info import NewsFullInfo
from scraping_api.models.news_short_info import NewsShortInfo
from bs4 import BeautifulSoup
import re


class ScraperInterface:
    def _get_content(self, url: str, encoding="utf-8") -> BeautifulSoup:
        http = urllib3.PoolManager()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }
        response = http.request('GET', url, headers=headers).data.decode(encoding)
        soup = BeautifulSoup(response, 'html.parser')
        return soup

    def _get_content_v2(self, url: str, encoding="utf-8") -> BeautifulSoup:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }
        response = requests.get(url, headers=headers).text
        soup = BeautifulSoup(response, 'html.parser')
        return soup

    def _remove_inner_html_tags(self, text: str) -> str:
        cleaner = re.compile('<.*?>')
        return cleaner.sub('', text)

    def get_news(self, url: str) -> NewsFullInfo | None:
        return None

    def get_articles(self, page: int) -> list[NewsShortInfo]:
        return []
