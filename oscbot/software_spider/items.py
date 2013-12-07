#!/usr/bin/python
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field

#     name = models.CharField(max_length=20,blank=False,null=False,unique=False)
#     slug = models.CharField(max_length=20)
#     #icon = models.ImageField()
#     #category = models.ForeignKey('Category',null=True)
#     #screenshot = models.ImageField()
#     #label = models.ManyToManyField('Label')
#     label = models.CharField(max_length=30)
#     description = models.TextField()
#     homepage = models.URLField(max_length=30)
#     license = models.CharField(max_length=10)
#     github = models.URLField(max_length=30)
#     language = models.CharField(max_length=10)
#     os = models.CharField(max_length=20)

class SoftwareItem(Item):
    name = Field()
    slug = Field()
    icon = Field()
    image_urls = Field()
    images = Field()
    category = Field()
    label = Field()
    description = Field()
    homepage = Field()
    license = Field()
    github = Field()
    language = Field()
    os = Field()