# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exporters import JsonLinesItemExporter
from datetime import datetime
import os,json


class CrawlerPipeline:
    def __init__(self):
        file_name = f"paguemenos_products_{datetime.now().date()}.json"
        current_directory = os.path.dirname(os.path.abspath(__file__))
        self.file = os.path.join(current_directory, "raw", file_name)
        self.items = []

    def process_item(self, item, spider):
        self.items.append(item)
        return item

    def close_spider(self, spider):
        with open(self.file, 'w', newline='\n') as file:
            json.dump(self.items, file, indent=4)
    
