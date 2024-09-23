import scrapy
from scrapy import Request
from scrapy.selector import Selector

from scrapyLearn.items import MovieItem


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["http://movie.douban.com/top250"]

    # def start_request(self):
    #     for page in range(10):
    #         url = f'http://movie.douban.com/top250?start={25 * page}&filter='
    #         print(url)
    #         yield Request(url=url,callback=self.parse)

    def parse(self, response,**kwargs):
        sel = Selector(response)
        list_items = sel.css('#content > div > div.article > ol > li')

        for list_item in list_items:
            movie_item = MovieItem()
            movie_item['title'] = list_item.css('span.title::text').extract_first()
            movie_item['subject'] = list_item.css('span.inq::text').extract_first()
            movie_item['rank']=list_item.css('span.rating_num::text').extract_first()
            yield movie_item

        next_page = sel.css('span.next a::attr(href)').extract_first()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield Request(next_page_url, callback=self.parse)





