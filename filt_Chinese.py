# -*- coding: utf-8 -*-
# 筛选出中文，剔除英文，数字，标点符号等

import sys
import re
#from __future__ import print_function
reload(sys)
sys.setdefaultencoding('utf8')
f = open("outcome6.txt", 'w+')
rf = open('source6.txt')
s = rf.read()

#print s
#unicode
s = unicode(s)
 
#unicode chinese
re_words = re.compile(u"[\u4e00-\u9fa5]+")
m =  re_words.search(s,0)
#print "--------"
#print m
#print m.group()
res = re.findall(re_words, s)       # 查询出所有的匹配字符串
if res:
    print "There are %d parts:\n" % len(res)
    for r in res: 
        print >> f, r,
print "--------"
 
#print "There are %d parts:\n"% len(res) 