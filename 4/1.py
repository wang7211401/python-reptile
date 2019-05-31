html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters;and their names were
<a href ="http://example.com/elsie" class="sister" id="linkl"><!-- Elsie --></a> hello
<a href ="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
import re
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
# print(soup)
# print(soup.prettify())
# print(type(soup.title))
# print(soup.title.string)
# print(soup.head)
# print(soup.p)
# print(soup.title.name)
# print(soup.p.attrs)
# print(soup.p.attrs['name'])
# print(soup.p.attrs['class'])
# print(soup.p.descendants)
# for i,child in enumerate(soup.p.descendants):
#     print(i,child)
# print(soup.a.parent)
# print('next sibling',soup.a.next_sibling)
# print('prev sibling',soup.a.previous_sibling)
# print('next siblings',list(enumerate(soup.a.next_sibling)))
# print('prev siblings',list(enumerate(soup.a.previous_sibling)))
# for item in soup.find_all(name="p"):
#     for a in item.find_all(name="a"):
#         print(a.string)

# print(soup.find_all(class_='title'))
# print(soup.find_all(text=re.compile('the')))
for a in soup.select('.story .sister'):
    print('get_text:',a.get_text())
    print('string:',a.string)