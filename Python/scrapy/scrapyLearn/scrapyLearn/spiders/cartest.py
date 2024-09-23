import scrapy
from scrapy import Request
from scrapy.selector import Selector

from scrapyLearn.items import cartestItem

class CartestSpider(scrapy.Spider):
    name = "cartest"
    allowed_domains = ["www.globalnevs.com"]
    start_urls = ["https://www.globalnevs.com/zh-cn/policy"]

    def parse(self, response):
        sel = Selector(response)
        list_items = sel.css('#__nuxt .flex .mb-2 .flex-1 .flex-col main')
        print(f'Found {len(list_items)} items.')

        for list_item in list_items:
            car_item = cartestItem()
            car_item['name'] = list_item.css(
                'div:nth-child(1) > a > div.text-truncate.text-4\\.5.line-height-6.font-600.mb-2.text-gray-800.transition-colors.group-hover\\:text-green-600.group-active\\:text-green-500'
            ).extract_first()
            if car_item['name']:
                yield car_item
            else:
                print('No name found for this item.')