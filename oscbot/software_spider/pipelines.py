#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb

class PythonicPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host = 'localhost', user = 'pythonic', passwd = 'pythonic', db = 'pythonic', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()
        if self.cursor:
            print "*****************************************************"
            
    def process_item(self, item, spider):
        try:
            self.cursor.execute("""
            insert into pypi_raw (name,slug,icon,category,label,description,homepage,license,github,language,os)
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,
                (item['name'].encode("utf-8"),
                item['slug'].encode("utf-8"),
                item['icon'].encode("utf-8"),
                item['category'].encode("utf-8"),
                item['label'].encode("utf-8"),
                item['description'].encode("utf-8"),
                item['homepage'].encode("utf-8"),
                item['license'].encode("utf-8"),
                item['github'].encode("utf-8"),
                item['language'].encode("utf-8"),
                item['os'].encode("utf-8"))
            )
            self.conn.commit()
        except MySQLdb.Error,e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item