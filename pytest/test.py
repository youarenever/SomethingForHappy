# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title><title>The Dormouse's story2</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sistersand their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
and they lived at the bottom of a well.</p>
<p class="story">xxxx</p>
"""

soup = BeautifulSoup(html)
# print soup.prettify()

# 当前节点操作
print soup.p.attrs

print soup.p['class']

soup.p['class']="ddd"
print soup.p['class']

print soup.p.string

# 子节点获取
print soup.head.contents  #list

print soup.head.children
for c in soup.head.children:
    print c
    print c.name

print "========所有子孙节点"
for c in soup.head.descendants:
    print c

print "========find_all搜索子tag，返回的是结果list"
print soup.find_all('b')  #list
print soup.find_all('b',limit=2)  #限制条数
print soup.find_all('b',recursive=False)  #只搜索b的直接子节点
print soup.find_all(["a", "b"]) #list
print soup.find_all('a',id='link2')
print soup.find_all(text="The Dormouse's story2")

print "========find_all class"
print soup.find_all('a', {"class": "sister"})

print "========find搜索子tag,返回的是结果,用法同find_all"

print soup.find('a',id='link2')
print soup.find('a',id='link2').name
print soup.find('a',id='link2').string

#css选择器
print "========css选择器"
print soup.select('title')
print soup.select('a')