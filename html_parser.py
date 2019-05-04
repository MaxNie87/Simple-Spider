import re
import urllib.parse
from bs4 import BeautifulSoup

class ResData:
    pass

class HtmlParser(object):

    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont,'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()

        links = soup.find_all('a', href=re.compile(r"^\?\S*"))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = ResData()
        res_data.titles = set()

        # url
        res_data.url = page_url
 
        pattern = re.compile(r'^[\u4e00-\u9fa5]{0,}$')

        title_nodes = soup.find_all('span', class_="title")
        for title_node in title_nodes:
            value = title_node.get_text()

            if pattern.match(value):
                res_data.titles.add(value)

        return res_data