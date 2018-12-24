from bs4 import BeautifulSoup
from urllib import request
import re
from functools import reduce




with open('ali16881.html',encoding='utf-8') as fp:
	soup = BeautifulSoup(fp)

# req = request.Request('https://www.aliexpress.com/store/product/Outdoor-Suvival-Aluminum-Tactical-Pen-Multi-purpose-Outdoor-Emergency-Break-Glass-Outdoor-Camping-Trip-Kit/1708277_32841619817.html?spm=2114.12010612.8148356.1.514d4cdcW7STCF')
# # req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as fp:
# 	soup = BeautifulSoup(fp)


# 产品标题
productname = soup.find('h1',class_='d-title')
print('productname:',productname.get_text())

# rewriteurl = re.sub(r'[\+":]+',' ',productname.string)
# print(rewriteurl.lower().replace(' ','-'))

# 查找产品价格及价格折扣

pricetag =soup.find('span',class_='value price-length-6')
# print(pricetag)
if not pricetag:
	pricetag = soup.find('div',class_='price-original-sku')
# print(pricetag)
productprice=pricetag.get_text()
if productprice.find('-')<0:
	print('productprice:',productprice)
else:
	print('productprice[]:',productprice.split('-')[1].strip())


# 查找产品attibutes及attributes相应的价格
attrscontent={}
attr_one_part = soup.select('div.d-content div.obj-leading')
attr_list=[]
# print(attr_one_part)
if attr_one_part:
	print('attr_one_part:[dddd]')
	for one_part in attr_one_part:	
		# print(header)	
		header_tag = one_part.find('span',class_='obj-title')
		attrkey=header_tag.string
		print('attrkey:',attrkey)
		dllis=[]
		list_tag = one_part.select('div.obj-content li a')
		for lli in list_tag:
			# print(lli['title'])
			dllis.append([lli['title']])
		attrscontent[attrkey]=dllis
		attr_list.append(dllis)
	print(attrscontent)
else:
	print('attr_one_part:[]')

attr_sku_part = soup.select('div.d-content div.obj-sku')
if attr_sku_part:
	for obj_sku in attr_sku_part:
		header_tag = obj_sku.find('span',class_='obj-title')
		attrkey=header_tag.string
		print('attrkey:',attrkey)
		dllis=[]
		list_tag = obj_sku.select('div.obj-content tr')
		for tr in list_tag:
			# print(lli['title'])
			name_span = tr.find('td',class_='name').find('span')
			if name_span.string:
				name = name_span.string
			else:
				name = name_span['title']
			print('name:',name)
			price = tr.find('td',class_='price').find('em',class_='value').string
			print('price:',price)
			count = tr.find('td',class_='count').find('em',class_='value').string
			print('count:',count)
			if count!='0':
				dllis.append([name,price,count])
		attrscontent[attrkey]=dllis
		attr_list.append(dllis)
print('attrscontent:',attrscontent)
print('attr_list:',attr_list)


def get_attr_content(aa, bb):
    cc=[]
    for a in aa:
        for b in bb:
            ctemp=[]
            tmp0=a[0] + ',' + b[0]
            ctemp.append(tmp0)
            tmp1=''
            if len(a) > 1 and len(b) > 1:
                tmp1=a[1] + ',' + b[1]
            elif len(a) > 1:
                tmp1=a[1]
            elif len(b) > 1:
                tmp1=b[1]
            ctemp.append(tmp1)
            cc.append(ctemp)
    return cc

attr_values_array=reduce(get_attr_content, attr_list) if len(attr_list) > 0 else []
print('attr_values_array:',attr_values_array)
# 查找产品图片
productimages=[]
# images = soup.select('div.tab-content-container')
# print(images)

ulimages = soup.select('div.tab-content-container div.vertical-img img')
# print(ulimages)
for img in ulimages:	
	imgurl=img['src']
	if 'lazyload.png' in imgurl:
		imgurl=img['data-lazy-src']
	imgurl=imgurl.replace('.60x60.jpg','.jpg')
	productimages.append(imgurl)
print(productimages)

# 查找产品描述
# psummary=soup.select('div.product-property-main')
psummary = soup.find('div',id='mod-detail-attributes',class_='mod-detail-attributes')
feature_tds=psummary.select('td')   
tdi = 0    
tds =[]     
for td in feature_tds:
	tdi+=1
	spans = td.get_text()
	if spans:
		tds.append(spans)
	# print('spans:')
	# print(spans.replace('\n','')+':'+str(tdi))
product_desc = reduce(lambda x,y:x+y,map(lambda x:x+':' if  tds.index(x)%2==0 and x else x+'\n',tds))
print(product_desc)


# 产品中的图片
# 产品中的相关产品列表
# 
# 
# Prestashop中Attribute的图片Atribute，及产品详情中Atribute对应的图片
# with open('p1.csv','a+') as fs:
# 	fs.write('\n')
# 	fs.write('\n' + str(package).replace('\n',''))