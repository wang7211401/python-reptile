from lxml import etree

# text = '''
# <div>
# <ul>
# <li class="item-0"><a href="linkl.html">first item</a></li>
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-inactive"><a href="link3.html">third item</a></li>
# <li class="item-1"><a href="link4.html">fourth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a></li>
# </ul>
# </div>
# '''

# html = etree.HTML(text)
html = etree.parse('./test.html',etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode('utf-8'))

# text = '''
# <li class="li li-first" name="item"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
result = html.xpath('//li[1]/a/text()')
print(result)
result = html.xpath('//li[last()]/a/text()')
print(result)
result = html.xpath('//li[position() < 3]/a/text()')
print(result)
result = html.xpath('//li[last()-1]/a/text()')
print(result)