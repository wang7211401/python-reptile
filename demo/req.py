# import requests
# import re
# r = requests.get('https://www.baidu.com')

# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)

# r = requests.get('http://httpbin.org/get?name=germey&age=22')
# print(r.text)

# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
# }
# r = requests.get('https://www.zhihu.com/explore',headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
# titles = re.findall(pattern,r.text)
# print(titles)

# r = requests.get("https://github.com/favicon.ico")
# with open('favicon.ico','wb') as f:
#     f.write(r.content)

# data = {'name':'germey','age':22}
# r =requests.post("http://httpbin.org/post",data=data)
# print(r.text)

# r = requests.get('http://www.jianshu.com')
# print(type(r.status_code),r.status_code)
# print(type(r.headers),r.headers)
# print(type(r.cookies),r.cookies)

# files = {'files':open('favicon.ico','rb')}
# r =requests.post("http://httpbin.org/post",files=files)
# print(r.text)

# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

# from requests.packages import urllib3
# urllib3.disable_warnings()
# response = requests.get('https://www.12306.cn',verify=False)
# print(response.status_code)


# import logging
# logging.captureWarnings(True)
# response = requests.get('https://www.12306.cn',verify=False)
# print(response.status_code)

# response = requests.get('https://www.12306.cn',cert=('/path/server.crt','/path/key'))
# print(response.status_code)

# proxies ={
#     "http":"http://10.10.1.10:3128",
#     "https":"http://10.10.1.10:1080"
# }

# requests.get("http://www.taobao.com",proxies=proxies)

from requests import Request,Session

url = 'http://httpbin.org/post'
data ={
    'name':'germey'
}

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
}

s = Session()
req = Request('POST',url,data=data,headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)

print(r.text)