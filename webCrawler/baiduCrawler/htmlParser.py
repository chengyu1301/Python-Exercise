# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import re
from anaconda_project.plugins.network_util import urlparse

class HtmlParser(object):


    
    def getNewURLs(self, pageURL, soup):
        newURLs = set()
        links = soup.find_all('a', href=re.compile(r'/item/[A-Za-z0-9\%]+'))

        for link in links:
            newURL = link['href']
            newURL = urlparse.urljoin(pageURL, newURL)
            newURLs.add(newURL)
        return newURLs
    
    def newData(self, pageURL, soup):
        resData = {}
        
        resData['url'] = pageURL
        
        titleNode = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        resData['title'] = titleNode.get_text()
        
        summaryNode = soup.find('div', class_='lemma-summary')
        resData['summary'] = summaryNode.get_text()
        
        return resData
    

    
    def parse(self, pageURL, htmlContent):
        if pageURL is None or htmlContent is None:
            return
        
        soup = BeautifulSoup(htmlContent, 'html.parser', from_encoding='utf-8')
        newURLs = self.getNewURLs(pageURL, soup)
        newData = self.newData(pageURL, soup)
        
        return newURLs, newData
    
