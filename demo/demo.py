# import socket
# import urllib.request
# import urllib.error

# try:
#     response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('TIME OUT')

# request = urllib.request.Request('https://python.org')
# response= urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

from urllib import request,parse

url = 'http://httpbin.org/post'
headers={
    'User-Agent':'Mozilla/4.0 (Compatible;MSIE 5.5;Windows NT)',
    'Host':'httpbin.org'
}
dict={
    'name':'Germey'
}
data = bytes(parse.urlencode(dict),encoding='utf8')
req = request.Request(url=url,data=data,headers=headers,method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))