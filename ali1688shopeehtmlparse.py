import settings
from ali1688scraperbrowser import ScraperBrowser
from bs4 import BeautifulSoup
import datetime
from functools import reduce
import re


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


class DougHtmlParse(object):
    def __init__(self):
        pass

    # 整理资料格式product_id;category_name;url
    def get_product_info(self, product_id, category_name,exclude_img, web_page_url):
        sb=ScraperBrowser()
        sb.web_page_url=web_page_url
        html_text=sb.get_html_text()
        exclude_imgs = []
        if not exclude_img:
            exclude_imgs = exclude_img.split(',')
        soup=BeautifulSoup(html_text)

        shopee_product=map(lambda x:None,range(1,78))
        shopee_product[0]=category_name
        # 产品标题
        productname=soup.find('h1', class_='d-title')
        # print('productname:', productname.get_text())
        shopee_product[1]=category_name

        # 查找产品描述
        # psummary=soup.select('div.product-property-main')
        psummary=soup.find('div', id='mod-detail-attributes', class_='mod-detail-attributes')
        feature_tds=psummary.select('td')
        tdi=0
        tds=[]
        for td in feature_tds:
            tdi+=1
            spans=td.get_text()
            if spans:
                tds.append(spans)
        # print('spans:')
        # print(spans.replace('\n','')+':'+str(tdi))
        product_desc=reduce(lambda x, y: x + y,
                            map(lambda x: x + ':' if tds.index(x) % 2 == 0 and x else x + '\n', tds))
        # print(product_desc)
        shopee_product[2]=product_desc
        shopee_product[6]=3
        shopee_product[7]=product_id
        # 查找产品价格及价格折扣
        pricetag=soup.find('span', class_='value price-length-6')
        # print(pricetag)
        if not pricetag:
            pricetag=soup.find('div', class_='price-original-sku')
        # print(pricetag)
        productprice=pricetag.get_text()
        if productprice.find('-') < 0:
            print('productprice:', productprice)
        else:
            print('productprice[]:', productprice.split('-')[1].strip())

        # 查找产品attibutes及attributes相应的价格
        attrscontent={}
        attr_list=[]
        attr_one_part=soup.select('div.d-content div.obj-leading')
        # print(attr_one_part)
        if attr_one_part:
            print('attr_one_part:[dddd]')
            for one_part in attr_one_part:
                # print(header)
                header_tag=one_part.find('span', class_='obj-title')
                attrkey=header_tag.string
                print('attrkey:', attrkey)
                dllis=[]
                list_tag=one_part.select('div.obj-content li a')
                for lli in list_tag:
                    # print(lli['title'])
                    dllis.append([lli['title']])
                attrscontent[attrkey]=dllis
                attr_list.append(dllis)
            print(attrscontent)
        else:
            print('attr_one_part:[]')

        attr_sku_part=soup.select('div.d-content div.obj-sku')
        if attr_sku_part:
            for obj_sku in attr_sku_part:
                header_tag=obj_sku.find('span', class_='obj-title')
                attrkey=header_tag.string
                print('attrkey:', attrkey)
                dllis=[]
                list_tag=obj_sku.select('div.obj-content tr')
                for tr in list_tag:
                    # print(lli['title'])
                    name_span=tr.find('td', class_='name').find('span')
                    if name_span.string:
                        name=name_span.string
                    else:
                        name=name_span['title']
                    print('name:', name)
                    price=tr.find('td', class_='price').find('em', class_='value').string
                    print('price:', price)
                    count=tr.find('td', class_='count').find('em', class_='value').string
                    print('count:', count)
                    if count != '0':
                        dllis.append([name, price, count])
                attrscontent[attrkey]=dllis
                attr_list.append(dllis)
        # print('attrscontent:', attrscontent)
        attr_values_array=reduce(get_attr_content, attr_list) if len(attr_list) > 0 else []
        print('attr_values_array:', attr_values_array)
        vi = 1
        for attr_value in attr_values_array:
            if vi > 15:
                break
            vti = (vi-1)*4 +1
            shopee_product[vti + 8]=str(product_id) + '-' + str(vi)
            shopee_product[vti + 9]=re.sub('[ ]+',' ',attr_value[0])
            shopee_product[vti + 10]=attr_value[1]
            shopee_product[vti + 11]=200
            vi+=1



        # 查找产品图片
        productimages=[]
        # images = soup.select('div.tab-content-container')
        # print(images)

        ulimages=soup.select('div.tab-content-container div.vertical-img img')
        # print(ulimages)
        for img in ulimages:
            imgurl=img['src']
            if 'lazyload.png' in imgurl:
                imgurl=img['data-lazy-src']
            imgurl=imgurl.replace('.60x60.jpg', '.jpg')
            productimages.append(imgurl)
        print(productimages)
        mi = 1
        for img in productimages:
            #判断是否要去掉此图片
            if mi in exclude_imgs:
                continue
            if mi>9:
                break
            shopee_product[mi+68] = img

        return shopee_product

    def __del__(self):
        pass
