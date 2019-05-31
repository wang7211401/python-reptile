html = '''
<title>demo</title>
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''

from pyquery import PyQuery as pq
import requests
# doc = pq(url="https://www.baidu.com")
# doc = pq(requests.get('https://cuiqingcai.com').text)
doc = pq(html)

# print(doc('#container .list'))
# print(doc('title'))
items = doc('li').items()
# lis = items.children('.active')
# print(lis)
# print(type(lis))
# parents = items.parents()
# print(type(items))
# for li in items:
#     print(li)
a = doc('.item-0.active')
print(a.html())