'''import scrapy

class MySpider(scrapy.Spider):
    name = "Peter"
    start_urls = ["https://ventadebienes.bancobcr.com/wps/portal/bcrb"]

    def parse(self, response):
        print("aaaaa")
        urls = response.css('div.table-cell.cell100.bienImgBox a::attr(href)').getall()
        print("aaa")
        for url in urls:
            print("a")
            yield {
                'url': url
            }
print("hola")
'''
from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print("aaa")
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')
