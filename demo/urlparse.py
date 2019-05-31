# from urllib.parse import urlparse

# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment',allow_fragments=False)
# print(result.scheme,result[0],result.netloc,result[1],sep='\n')

# from urllib.parse import urlunparse

# data = ['http','www.baidu.com','index.html','user','a=6','comment']
# print(urlunparse(data))

# from urllib.parse import urlsplit

# result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
# print(result.scheme,result[0])

# from urllib.parse import urlunsplit

# data = ['http','www.baidu.com','index.html','a=6','comment']
# print(urlunsplit(data))

# from urllib.parse import urljoin

# print(urljoin('http://www.baidu.com','FAQ.html'))

# from urllib.parse import urlencode

# params = {
#     'name':'germey',
#     'age':22
# }
# base_url ='http://www.baidu.com?'
# url = base_url + urlencode(params)
# print(url)

# from urllib.parse import parse_qsl

# query = 'name=germey&age=22'
# print(parse_qsl(query))

# from urllib.parse import quote

# keyword ='壁纸'
# url ='https://www.baidu.com/s?wd=' + quote(keyword)
# print(url)

from urllib.parse import unquote

url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'

print(unquote(url))