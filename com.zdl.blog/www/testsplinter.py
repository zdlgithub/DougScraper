#!/usr/bin
#pip install splinter
#一个Python 2和3兼容性库
#pip install six
import platform as pf
import os
from time import sleep
from splinter.browser import Browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.webkitgtk
from bs4 import BeautifulSoup

def add_chome_webdriver():
	print(pf.system())
	working_path = os.getcwd()
	print(working_path)
	library='library'
	path = os.path.join(working_path,library)
	print(path)	
	os.environ['PATH']+='{}{}{}'.format(os.pathsep,path,os.pathsep)
	print(os.environ['PATH'])

url='https://www.aliexpress.com/item/Sequined-synthetic-leather-blue-women-kitten-heel-sandals-Latin-jazz-dancing-shoes-metal-silver-skid-resistance/32926119244.html?spm=2114.search0103.3.54.42c41a44LP5AjD&ws_ab_test=searchweb0_0,searchweb201602_5_5734715_10065_10068_5734615_10890_5730315_319_10546_5734815_10548_317_10696_10924_453_10084_454_10083_10618_10920_5729215_10921_10922_10307_537_536_10059_10884_10887_10928_100031_321_322_10103_5734515-5734715,searchweb201603_51,ppcSwitch_0&algo_expid=01d893b5-20dd-47c3-894f-853a5ee05099-7&algo_pvid=01d893b5-20dd-47c3-894f-853a5ee05099'

def find_website():		
	# driver = webdriver.PhantomJS(executable_path="d:\python\python37\phantomJS.exe")	
	with Browser('chrome',headless=False) as browser:
		browser.visit(url)
		# input = browser.find_by_id('kw')
		# input.fill('知乎')

		# btn = browser.find_by_css('#su')		
		# btn.click()
		# # print(browser.html)
		# print(btn.html)

		# if browser.is_text_present('发现更大的世界'):
		# 	print('YES')
		# else:
		# 	print('No')
		
		# pdt=browser.find_by_css('.ui-tab-active a')
		# pdt.click()
		sleep(5)		
		html_text=browser.html
		parse_html_by_beautifulsoup(html_text)
		# print(browser.html)
		# browser.execute_script('''seajs.iuse("//i.alicdn.com/ae-detail-ui/alone/main-detail-v170105.js")(function(Detail) {
  #               Detail.init();
  #           });''')
		# print(browser.find_by_css('.product-description-main').html)
		# browser.quit();
		
def find_website_by_chrome():	
	options = webdriver.ChromeOptions()
	# options.add_argument('handless')
	# options.set_headless(True)
	options.headless=True 
	options.add_argument('--start-maximized')
	# options.add_argument('--disable-gpu')
	# browser=webdriver.Chrome(options=options)
	prefs = {
		    'profile.default_content_setting_values': {
		        'images': 1,
		        # 'javascript': 1,
		        # 'geolocation': 1
		    }
		}
	options.add_experimental_option('prefs',prefs)
	browser=webdriver.Chrome(options=options)

	browser.get(url)
	print('url')	
	# sleep(5)
	# target = browser.find_element_by_class_name('product-description-main')
	# browser.execute_script("arguments[0].scrollIntoView();", target) #拖动到可见的元素去,只在窗口模式下有用
	# ahrefsg = browser.find_element_by_link_text('Seller Guarantees')
	# print(ahrefsg.text)
	# # ahrefsg.click()
	# ahref.send_keys(Keys.TAB)
	# sleep(5)
	# 
	ahref = browser.find_element_by_link_text('Product Details')	
	print(ahref.text)	
	ahref.send_keys(Keys.TAB)
	# sleep(5)
	i = 0
	while i<5:
		i+=1
		try:
			loading32 = browser.find_element_by_css_selector('.product-description-main .loading32')	
			print('loading32:',loading32)		
		except:
			print('not loading32')		
			break;
		print('while sleep5')
		sleep(5)
	# browser.execute_script('window.scrollTo(100, document.body.scrollHeight);')

	# try:
	# 	dwait =WebDriverWait(browser,10).until_not(lambda browser:browser.find_element_by_css_selector('.product-description-main>.loading32'))
	# 	print('waitabc')		
	# except Exception as e:
	# 	print(e)

	# sleep(5)
	html_text = browser.page_source
	browser.quit()
	# print(html_text)
	parse_html_by_beautifulsoup(html_text)

def find_website_by_firefox():
	options = webdriver.FirefoxOptions()
	options.headless=True
	# options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0"')
	
	b = webdriver.Firefox(options=options)
	b.get(url)
	print('url')	
	sleep(5)
	# target = b.find_element_by_class_name('product-description-main')
	# b.execute_script("arguments[0].scrollIntoView();", target) #拖动到可见的元素去
	ahref = b.find_element_by_link_text('Product Details')
	print('ahreflocation:',ahref.location)
	print(ahref)
	ahref.send_keys(Keys.TAB)
	i = 0
	while i<10:
		i +=1
		ahref.send_keys(Keys.ARROW_DOWN)
		ahref.send_keys(Keys.ARROW_DOWN)
	
	sleep(15)
	html_text = b.page_source
	b.quit()
	# pdesc1 = b.find_element_by_class_name("description-content")
	# print(pdesc1.text())
	# print(html_text)
	parse_html_by_beautifulsoup(html_text)
	
def parse_html_by_beautifulsoup(html_text):
	soup = BeautifulSoup(html_text,features="html.parser")
	pdesc = soup.find('div',class_='product-description-main')
	kses = pdesc.find_all('kse:widget')
	if kses!=None:
		for kse in kses:
			kse.decompose()
	print('Product desc')
	print(pdesc)

if __name__ == '__main__':
	add_chome_webdriver()
	# find_website()
	# find_website_by_chrome()
	find_website_by_firefox()