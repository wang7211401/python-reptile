import requests
from parsel import Selector
import time
import re, random, os

def scraw_pin_ids():

	pin_ids = []
	urls = []
	page = 2
	flag = True

	while flag:
		try:
			url = "http://huaban.com/search/?q=%E6%B5%B7%E8%B4%BC%E7%8E%8B%E5%A3%81%E7%BA%B8"
			headers1 = {
			'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
			'Accept':'application/json',
			'X-Request':'JSON',
			'X-Requested-With':'XMLHttpRequest',
			}

			params = {
				'joqwb7d5':'',
				'page':str(page),
				'per_page':'20',
				'wfl':'1'
			}

			z1 = requests.get(url, params=params, headers=headers1)

			if z1.json()['pins']:
				print('pins:')
				print(len(z1.json()['pins']))
				page = page + 1
				print('page:')
				print(page)
				for i in z1.json()['pins']:
					urls.append(i['file']['key'])
					# pin_ids.append(i['pin_id'])
					# pin_id = pin_ids[-1]
					# print(i['pin_id'])
					# with open("pin_ids.txt",'ab') as f:
					# 	f.write(str(i['pin_id'])+"\n")
					# 	f.close()
					time.sleep(0.001)

				print(urls)	
			else:
				flag = False
				return set(urls)
		except:
			continue


def scraw_urls(pin_ids):

	urls = []

	urlss = ['http://huaban.com/pins/' + str(i) +'/' for i in pin_ids]
	for url in urlss:
		try:
			headers = {
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
			}

			z3 = requests.get(url, headers=headers)

			text = z3.text

			pattern = re.compile('"key":"(.*?)"', re.S)
			items = re.findall(pattern, text)

			urls.extend(items)
			print(items)
			print('============================================================================================================')
		except:
			continue
	return set(urls)


def download(urls):
	headers1 = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
	}
	n = 1
	# urls = set(urls)
	for url in urls:
		try:
			if not os.path.exists(os.path.join(file_path, "haizei")):
				os.makedirs(os.path.join(file_path, "haizei"))
			os.chdir(file_path + '\\' + "haizei")
			try:
				url = 'http://img.hb.aicdn.com/' + url
				r = requests.get(url, headers=headers1)
				if len(r.content)>40000:
					with open(str(n)+".jpg", 'wb') as f:
						f.write(r.content)
						f.close()
						print("第" + str(n) + "张图片下载成功")
						n+=1
						# time.sleep(3)
			except:
				continue
		except:
			continue

# 图片存储路径
file_path = 'D:\huaban'
pin_urls = scraw_pin_ids()
# urls = scraw_urls(pin_ids)
download(pin_urls)


# url = 'http://huaban.com/favorite/beauty/'
# headers = {
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
# }
# z = requests.get(url,headers=headers)
# print(z.status_code)
# # 返回200
# # 使用parsel中的Selector 来解析
# sel = Selector(text=z.text)
# print(sel.xpath('//a[@class="img x layer-view loaded"]/@href'))

# params = {
# 'j0ga0hbi':'',
# 'max':'1062161596',
# 'limit':'100',
# 'wfl':'1'
# }
# z1 = requests.get(url=url,params=params,headers=headers)
# print(z1.status_code)
# 返回200
# print(z1.json())

# headers1 = {
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
# 'Accept':'application/json',
# 'X-Request':'JSON',
# 'X-Requested-With':'XMLHttpRequest'
# }
# z2 = requests.get(url=url,params=params,headers=headers1)
# print(z2.content)