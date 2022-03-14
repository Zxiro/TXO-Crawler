import scrapy
import time
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from txo_crawler.items import TxoCrawlerItem


class TxoSpider(CrawlSpider):
    name = 'txo'
    allowed_domains = ['www.taifex.com.tw']
    start_urls = ['http://www.taifex.com.tw/cht/3/dlFutPrevious30DaysSalesData/']

    rules = (
        Rule(LinkExtractor(allow=r'cht/3/dlFutPrevious30DaysSalesData/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        file_url = response.css('#button7.btn_orange::attr(onclick)').re(r"https://www.taifex.com.tw/file/taifex/Dailydownload/DailydownloadCSV/Daily.*[^)']")
        print('file_url: ', file_url)
        for url in file_url:
            file_url = response.urljoin(url)
            item = TxoCrawlerItem()
            item['file_urls'] = [file_url]
            yield item
            time.sleep(0.5)

