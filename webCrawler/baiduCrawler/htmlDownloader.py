# -*- coding:utf-8 -*-

import urllib
from urllib.request import urlopen


class  htmlDownloader(object):
    
    def download(self, url):

        if url is None:
            return None
        
        htmlRequest = urlopen(url)
    
        if htmlRequest.getcode() != 200:
            return None
        
        return htmlRequest.read()