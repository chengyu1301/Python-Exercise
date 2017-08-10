# -*- coding:utf-8 -*-

import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

from baiduCrawler import htmlDownloader
from baiduCrawler import htmlOutputer
from baiduCrawler import htmlParser
from baiduCrawler import urlManager


class SpiderMain():
    def __init__(self):
        self.urls= urlManager.UrlManager()
        self.downloader = htmlDownloader.htmlDownloader()
        self.parser = htmlParser.HtmlParser()
        self.outputer = htmlOutputer.HtmlOutputer()
    def crawl(self, rootURL):
        count = 1
        self.urls.addNewURL(rootURL)
        while self.urls.hasNewURL():
            try:
                newURL = self.urls.getNewURL()
                print('Craw %d: %s' % (count, newURL))
                htmlContent = self.downloader.download(newURL)
 
                newURLs, newData = self.parser.parse(newURL, htmlContent)
                self.urls.addNewURLs(newURLs)
                self.outputer.collectData(newData)
            
                if count == 1000:
                    break
                count += 1
            except:
                print('Craw failed')
        
        
        self.outputer.outputHtml()

if __name__ == '__main__':
    rootURL = 'https://baike.baidu.com/item/Python/407313'
    spider = SpiderMain()
    spider.crawl(rootURL)
