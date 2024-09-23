# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl
import pymysql

class MysqlPipeline:
    def __init__(self):
        self.conn=pymysql.connect(host='localhost',user='root',password='123456',database='spider')
        self.cursor=self.conn.cursor()

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        title=item.get('title', '')
        subject=item.get('subject', '')
        rank=item.get('rank', '')

        sql="insert into movie(title,subject,rank) values(%s,%s,%s)"
        self.cursor.execute(sql,(title,subject,rank))
        self.conn.commit()

        return item

class ScrapylearnPipeline:

    def __init__(self):
        self.wb=openpyxl.Workbook()
        self.ws=self.wb.active
        self.ws.title='豆瓣电影top250'
        self.ws.append(['title','subject','rank'])

    def close_spider(self, spider):
        self.wb.save('电影top250.xlsx')


    def process_item(self, item, spider):
        # 提前处理防止空值
        title=item.get('title','')
        subject=item.get('subject', '')
        rank=item.get('rank', '')

        self.ws.append([title, subject, rank])

        # 也可以直接传
        self.ws.append(list(item.values()))
        return item
