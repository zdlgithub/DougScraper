from urllib import request
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time

def get_trans_text():
	url = 'https://translate.google.cn/#view=home&op=translate&sl=zh-CN&tl=en&text=%3Cdiv%20class%3D%22dpl-box-title%22%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%E8%B4%A7%E5%93%81%E7%B1%BB%E5%9E%8B%0A%20%20%20%20%20%20%20%20%3C%2Fdiv%3E'
	# req = request.urlopen(url)
	wd = webdriver.Chrome(executable_path=os.path.join(os.path.dirname(__file__),'library/chromedriver.exe'))
	wd.get(url)
	time.sleep(10)
	html_text = wd.page_source
	wd.quit()
	print(html_text)
	soup=BeautifulSoup(html_text,features="html.parser")
	print(soup.string())


if __name__=='__main__':
	get_trans_text()