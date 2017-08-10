# -*- coding:utf-8 -*-

class UrlManager(object):
    
    def __init__(self):
        self.newURLs = set()
        self.oldURLs = set()
    
    def addNewURL(self, url):
        if url is None:
            return
        if url not in self.newURLs and url not in self.oldURLs:
            self.newURLs.add(url)
    def addNewURLs(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.addNewURL(url)
            
    def hasNewURL(self):
        return len(self.newURLs) != 0
    
    def getNewURL(self):
        newURL = self.newURLs.pop()
        self.oldURLs.add(newURL)
        return newURL
    
    



