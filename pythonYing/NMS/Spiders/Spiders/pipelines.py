# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter


class SpidersPipeline:
    # def process_item(self, item, spider):
    # return item

    def process_item(self, item, spider):
        print("=================== process_item in pipeline =======================")
        prd_name = item['prd_name']
        link = item['link']
        comments = item['comments']
        output = f'|{prd_name}|\t|{link}|\t|{comments}|\n\n'
        with open('./phone.txt', 'a+', encoding='utf-8') as article:
            article.write(output)

        with open("./phones.csv", "a+b") as f:
            exporter = CsvItemExporter(f, include_headers_line=False)
            exporter.start_exporting()
            exporter.export_item(item)
            exporter.finish_exporting()

        return item
