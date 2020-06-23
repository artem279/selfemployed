# -*- coding: utf-8 -*-
import scrapy
from selfemployed.items import SelfemployedItem
import time, random, datetime, json, csv

csv.register_dialect('csvCommaDialect', delimiter='|', lineterminator='\n')


def getvalue(tag):
    value = ''
    try:
        value = tag.replace('\n', '').replace('\r', '').replace('\t', '').replace('|', '/').replace('"', '') \
            .replace('  ', '').replace(';', ',')
    except Exception as e:
        value = ''
    return value


def parse_json(response):
    json_response = json.loads(response)
    item = {}
    item['status'] = str(json_response.get('status'))
    item['message'] = str(json_response.get('message'))
    return item


class SelfemployedSpider(scrapy.Spider):
    name = "selfemployed"

    def start_requests(self):
        url = 'https://statusnpd.nalog.ru/api/v1/tracker/taxpayer_status' # api url
        inn_list = ["000000000000"] # list of id
        date = datetime.date.today().isoformat() # current date
        for e in inn_list:
            yield scrapy.Request(url=url, method='POST', callback=self.parse,
                                 body=json.dumps({"inn": e, "requestDate": date}))

    def parse(self, response):
        item = SelfemployedItem()
        js = parse_json(response.text)
        item['status'] = js['status']
        item['message'] = js['message']
        print(item)
        yield item
