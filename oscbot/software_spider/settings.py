#!/usr/bin/python
# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
SPIDER_MODULES = ['software_spider.spiders']
NEWSPIDER_MODULE = 'software_spider.spiders'
DEFAULT_ITEM_CLASS = 'software_spider.items.SoftwareItem'
ITEM_PIPELINES = ['software_spider.pipelines.PythonicPipeline','scrapy.contrib.pipeline.images.ImagesPipeline']
IMAGES_STORE = '/path/to/valid/dir'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'