import sys,importlib
import pynlpir

# ------------------开始---------------------
print('------------------Start---------------------')
# ------------------网络资源关键词提取---------------------
print('------------------网络资源关键词提取---------------------')
import scrapy

importlib.reload(sys)

class BaiduSearchSpider(scrapy.Spider):
    name = "baidu_search"
    allowed_domains = ["baidu.com"]
    start_urls = [
        "https://www.baidu.com/s?wd=机器学习"
    ]

    def parse(self, response):
        print(response)



print('------------------End---------------------')
# pynlpir.close()