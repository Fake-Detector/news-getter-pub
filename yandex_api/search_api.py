from xml.sax.saxutils import escape
import xml.etree.ElementTree as ET
import urllib3

from yandex_api.config import yandex_config

FolderId = "b1g1a6s45gjkvablcdoj"
YANDEX_URL = "https://yandex.ru/search/xml"


class SearchApi:
    def __init__(self, filter_type: str = "strict"):
        self.token = yandex_config["TOKEN"]
        self.filter_type = filter_type
        self.folder_id = FolderId

    def _search(self, query: str, site: str | None, page_number=0, max_passages=5):
        http = urllib3.PoolManager()

        url = f"{YANDEX_URL}?folderid={self.folder_id}&filter={self.filter_type}"

        headers = {
            'Authorization': f'Api-Key {self.token}',
            'Content-Type': 'application/xml; charset=utf-8'
        }

        escaped_query = escape(query)
        body = f"""<?xml version="1.0" encoding="UTF-8"?>
                <request>
                    <query>{escaped_query} {"site:" + site if site is not None and site != "" else ""}</query>
                    <sortby order="descending">rlv</sortby>
                    <maxpassages>{max_passages}</maxpassages>
                    <page>{page_number}</page>
                    <groupings>
                        <groupby attr="d" mode="deep" groups-on-page="10" docs-in-group="3" />
                    </groupings>
                </request>"""

        response = http.request('POST', url, body=body.encode('utf-8'), headers=headers)

        return response.data.decode('utf-8')

    def _get_links(self, xml: str):
        urls = []

        root = ET.fromstring(xml)

        for group in root.findall(".//group"):
            url_element = group.find(".//url")
            if url_element is not None:
                urls.append(url_element.text)

        return urls

    def _get_links_extended(self, query: str, site: str | None, limit: int, max_passages: int):
        result_links = []
        page_number = 0
        while len(result_links) < limit:
            xml = self._search(query, site=site, page_number=page_number, max_passages=max_passages)
            links = self._get_links(xml)
            result_links.extend(links)
            page_number += 1
            if len(links) < max_passages:
                break

        return result_links[:limit]

    def get_links(self, query: str, sites: list[str] = None, max_links=5, max_passages=3):
        result_links = []

        if sites is None or len(sites) == 0:
            result_links = self._get_links_extended(query, None, max_links, max_passages)
        else:
            for site in sites:
                links = self._get_links_extended(query, site, max_links, max_passages)
                result_links.extend(links)

        return result_links
