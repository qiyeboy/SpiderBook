#coding:utf-8
import re
import urllib.parse
import logging  
from bs4 import BeautifulSoup
import pprint

from .HtmlDownloader import HtmlDownloader

class HtmlParser:
    def __init__(self, cfg):
        self.url_fiter_keys = cfg["url_fiter_keys"]
        self.url_reverse_keys = cfg["url_reverse_keys"]

    def url_fiter_keys(self, urls):
        for url in urls:
            for url_fiter_key in url_fiter_keys:
                if url_fiter_key in url:
                    return False
            for url_reverse_key in url_reverse_keys:
                if url_reverse_key in url:
                    return True

    def parser(self,page_url,html_cont):
        '''
        用于解析网页内容抽取URL和数据
        :param page_url: 下载页面的URL
        :param html_cont: 下载的网页内容
        :return:返回URL和数据
        '''
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data


    def _get_new_urls(self,page_url,soup):
        '''
        抽取新的URL集合
        :param page_url: 下载页面的URL
        :param soup:soup
        :return: 返回新的URL集合
        '''
        new_urls = set()
        #抽取符合要求的a标签
        # 原书代码
        # links = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
        #2017-07-03 更新,原因百度词条的链接形式发生改变
        '''
        links = soup.find_all('a',href=re.compile(r'/item/.*'))
        for link in links:
            #提取href属性
            new_url = link['href']
            #拼接成完整网址
            new_full_url = urllib.parse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls
        '''
        for link in soup.find_all('a'):
            if link.get('href') and link.get('href').startswith("http"):
                #print(link.get('href'))
                new_urls.add(link.get('href'))
        #pprint.PrettyPrinter(indent=4).pprint(new_urls)
        filter(self.url_fiter_keys, new_urls)
        #new_urls = set(url for url in new_urls if "dxy" in(url))
        #pprint.PrettyPrinter(indent=4).pprint(new_urls)
        logging.info(new_urls)  
        return new_urls

    def _get_new_data(self,page_url,soup):
        '''
        抽取有效数据
        :param page_url:下载页面的URL
        :param soup:
        :return:返回有效数据
        '''
        '''
        data={}
        data['url']=page_url
        title = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title']=title.get_text()
        summary = soup.find('div',class_='lemma-summary')
        #获取到tag中包含的所有文版内容包括子孙tag中的内容,并将结果作为Unicode字符串返回
        data['summary']=summary.get_text()
        return data
        '''
        data={}
        data['url']=page_url
        data['summary']=[]
        for p in soup.find_all('p'):
            #print(p)
            for string in p.stripped_strings:
                #print(repr(string))
                data['summary'].append(string)
        logging.info(data)
        return data


if __name__ == "__main__":
    url="http://www.dxy.cn"
    content = HtmlDownloader().download(url)
    new_urls,data = HtmlParser().parser(url,content)
