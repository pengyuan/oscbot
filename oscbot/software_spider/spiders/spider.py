#!/usr/bin/python
# -*- coding: utf-8 -*-
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from software_spider.items import SoftwareItem
import string
import urllib2
import urlparse

class SoftwareInfoSpider(BaseSpider):
    name = "pythonic"
    allowed_domains = ["oschina.net"]
    start_urls = ["http://www.oschina.net/project/list?p=1"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        page = hxs.select("//div[@class='ProjectList']/ul[@class='pager']/li[@class='page current']/a/text()").extract()[0]
        print "page:::",page
        next_page = int(page) + 1

        for per in hxs.select("//div[@class='ProjectList']/ul[@class='List']/li"):
            partlink = per.select("h3/a/@href").extract()[0]
            link = urlparse.urljoin('http://www.oschina.net',partlink)
            yield Request(link, callback=self.parse_software)

        if next_page <= 1311:
            url = urlparse.urljoin('http://www.oschina.net', 'project/list?p=%s' % next_page)
            yield Request(url, callback=self.parse)
    
    def parse_software(self, response):
        hxs1 = HtmlXPathSelector(response)
        name = hxs1.select("//div[@class='ProjectMain']/div[1]/h1[@class='PN']/a[@class='name']/u/text()").extract()[0].strip()
        slug = response.url.split('/')[-1]
        icon = hxs1.select("//div[@class='ProjectMain']/div[1]/h1[@class='PN']/img/@src").extract()
        if icon:
            if icon == '/img/logo/default.gif':
                icon = ''
            else:
                icon = icon[0].strip()
        else:
            icon = ''
             
        category = hxs1.select("//div[@class='wp998']/dl/dt[2]/a[2]/text()").extract()
        if category:
            category = category[0].strip()
        else:
            category = ''
             
        label = hxs1.select("//div[@class='ProjectMain']/div[1]/h1[@class='PN']/a[@class='name']/text()").extract()
        if label:
            label = label[0].strip()
        else:
            label = ''
 
        description = ''.join(hxs1.select("//div[@class='Body']/div[@id='p_fullcontent']/p").extract()).strip() #带<p></p>
        #description = re.sub(r'<[^>]*?>','',content)
        homepage = hxs1.select("//div[@class='Body']/ul[@class='urls']/li[1]/a/@href").extract()
        if homepage: 
            url = urlparse.urljoin('http://www.oschina.net', homepage[0].strip())
            headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',"Accept":"text/html,*/*","Connection":"Keep-Alive"} #由于网站禁止爬虫，在请求加上头信息，伪装成浏览器访问
            req = urllib2.Request(url = url,headers = headers)
            try:
                u = urllib2.urlopen(req, timeout=20)
                homepage = u.url
            except urllib2.URLError, e:  
                print e.reason
                homepage = ''
                pass
        else:
            homepage = ''
        slicense = hxs1.select("//div[@class='Body']/ul[@class='attrs']/li[not(@class='lang')][1]/a/text()").extract()
        if slicense:
            slicense = slicense[0].strip()
        else:
            slicense = hxs1.select("//div[@class='Body']/ul[@class='attrs']/li[not(@class='lang')][1]/text()").extract()
            if slicense:
                slicense = string.replace(slicense[0],u"授权协议：","",1).strip()
            else:
                slicense = ''
        github = hxs1.select("//div[@class='GithubEmbed']/div[@class='github-widget']/@data-repo").extract()
        if github:
            github = github[0].strip()
        else:
            github = ''
        
        language = hxs1.select("//div[@class='Body']/ul[@class='attrs']/li[@class='lang']/a/text()").extract()
        if language:
            language = language[0].strip()
        else:
            language = ''
        os = hxs1.select("//div[@class='Body']/ul[@class='attrs']/li[not(@class='lang')][2]/a/text()").extract()
        if os:
            os = os[0].strip()
        else:
            os = ''        
#         print 'name:::',name
#         print 'slug:::',slug
#         print 'icon:::',icon
#         print 'category:::',category
#         print 'label:::',label
#         print 'description:::',description
#         print 'homepage:::',homepage
#         print 'license:::',slicense
#         print 'language:::',language
#         print 'os:::',os
#         print 'github:::',github
        item = SoftwareItem(name=name,slug=slug,icon=icon,category=category,label=label,description=description,homepage=homepage,license=slicense,github=github,language=language,os=os)
        yield item