from bs4 import BeautifulSoup
from urllib import request
import re

with open('p2.html',encoding='utf-8') as fp:
	soup = BeautifulSoup(fp)

# req = request.Request('https://www.aliexpress.com/store/product/Outdoor-Suvival-Aluminum-Tactical-Pen-Multi-purpose-Outdoor-Emergency-Break-Glass-Outdoor-Camping-Trip-Kit/1708277_32841619817.html?spm=2114.12010612.8148356.1.514d4cdcW7STCF')
# # req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as fp:
# 	soup = BeautifulSoup(fp)

# 取得标题
headTitle = soup.title.string
print('headTitle:',headTitle)
# print(soup.find('meta',attrs={'name':'keywords'}))
# 取得关键词
metacontent = soup.find('meta',attrs={'name':'keywords'})['content']
print('metacontent:',metacontent)

# 取得描述
metadesc = soup.find('meta',attrs={'name':'description'})
print('metadesc:',metadesc['content'])

# 产品标题
productname = soup.find('h1',class_='product-name')
print('productname:',productname.get_text())

rewriteurl = re.sub(r'[\+":]+',' ',productname.string)
print(rewriteurl.lower().replace(' ','-'))

# 查找产品价格及价格折扣
productprice = soup.find('span',id='j-sku-price').get_text()
if productprice.find('-')<0:
	print('productprice:',productprice)
else:
	print('productprice[]:',productprice.split('-')[1].strip())

discountprice = soup.find('span',id='j-sku-discount-price')
print('discountprice:',discountprice.string)
# 查找产品attibutes及attributes相应的图片
attrscontent={}
# attributs=soup.find('div',id="j-product-info-sku").find_all('dl')
attributs=soup.select('div#j-product-info-sku dl')
i=0
for dl in attributs:
	i=i+1
	print(i)
	attrkey=dl.dt.string.rstrip(':')
	print('attrkey:',attrkey.rstrip(':'))
	dlli = dl.select('li')
	dllis=[]
	for lli in dlli:
		if (lli.has_attr('class') and lli['class'][0]=='item-sku-image'):			
			vname=lli.a['title']
			if(lli.a.img):
				samllpic=lli.a.img['src']	
				bigpic=lli.a.img['bigpic']
			dllis.append([vname,samllpic,bigpic])
		elif (lli.span):
			vname=lli.a.span.string
			dllis.append([vname])
		else:
			pass
		# print('dllis:',dllis)
	attrscontent[attrkey]=dllis
	print(attrscontent)		

# 查找产品图片
productimages=[]
ulimages = soup.select('ul#j-image-thumb-list img')
for img in ulimages:
	imgurl=img['src'].replace('_50x50.jpg','')
	productimages.append(imgurl)
print(productimages)

# 查找产品描述
# psummary=soup.select('div.product-property-main')
psummary = soup.find('div',id=None,class_='product-property-main')
feature_lis=psummary.select('li')   
lin = 0         
for lli in feature_lis:
	lin+=1
	spans = lli.get_text()
	print('spans:')
	print(spans.replace('\n','')+':'+str(lin))

print(psummary)
#pdesc = soup.select('div.product-video-main,div.product-description-main')
pdescvideo = soup.find('div',class_='product-video-main')
print(pdescvideo)

pdesc = soup.find('div',class_='product-description-main')
kses = pdesc.find_all('kse:widget')
if kses!=None:
	for kse in kses:
		kse.decompose()

pdescstr =re.sub(r'data\-[\w\-="\.]*','',str(pdesc))
print('Product desc')
print(pdescstr)

package = soup.find('div',class_='pnl-packaging-main')
print(str(package))

pattern = re.compile(r'(\d+|\d+\.\d+)([cm]+|[kg]+)')
result1=pattern.findall(str(package))
print(result1)

# 产品中的图片
# 产品中的相关产品列表
# 
# 
# Prestashop中Attribute的图片Atribute，及产品详情中Atribute对应的图片
with open('p1.csv','a+') as fs:
	fs.write('\n')
	fs.write('\n' + str(package).replace('\n',''))