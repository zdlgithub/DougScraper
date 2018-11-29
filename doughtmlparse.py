import settings
from scraperbrowser import ScraperBrowser
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
    def get_product_info(self, product_id, category_name, web_page_url):
        sb=ScraperBrowser()
        sb.web_page_url=web_page_url
        html_text=sb.get_html_text()

        soup=BeautifulSoup(html_text)
        # 取得标题
        head_title=re.sub(settings.ALIEXPRESS_DOMAIN, settings.MY_DOMAIN, soup.title.string)
        print('headTitle:', head_title)

        # 取得关键词
        meta_keywords=soup.find('meta', attrs={'name': 'keywords'})['content']
        print('meta_keywords:', meta_keywords)

        # 取得描述
        meta_desc = soup.find('meta', attrs={'name': 'description'})['content'].replace('\n', ' ')
        meta_desc = re.sub(settings.ALIEXPRESS_DOMAIN, settings.MY_DOMAIN, meta_desc)
        print('meta_desc:', meta_desc)

        # 产品标题
        product_name=soup.find('h1', class_='product-name')
        print('product_name:', product_name.string)

        # 过滤掉产品中的物殊字符
        rewriteurl=re.sub(r'[+":/&?#()*^,)]+', ' ', product_name.string).lower()
        rewriteurl=re.sub(r'[ ]+', '-', rewriteurl)
        # 查找产品价格及价格折扣
        product_price=soup.find('span', id='j-sku-price').get_text()
        print(product_price)
        match_result=re.match(r'(\d+\.\d+) \- (\d+\.\d+)', product_price)
        if match_result:
            product_price = match_result.group(2)
        print('product_price:', product_price)

        # discount_price=soup.find('span', id='j-sku-discount-price')
        # print('discount_price:', discount_price.string)

        # 查找产品图片
        product_images=[]
        product_images_alt_text=[]
        ulimages=soup.select('ul#j-image-thumb-list img')
        for img in ulimages:
            imgurl=img['src']
            product_images.append(imgurl.replace('_50x50.jpg', ''))
            product_images_alt_text.append(img['alt'])
        print(product_images)

        # 拼接初始的image position信息
        img_pos_str=reduce(lambda x, y: str(x) + ',' + str(y), list(range(1, len(product_images) + 1)))

        supplier_ref=''
        supplier=''
        manufacturer=''
        ean_13=''
        upc=''
        short_desc=''

        # 查找产品attibutes及attributes相应的图片
        attrs_array=[]
        # attributs=soup.find('div',id="j-product-info-sku").find_all('dl')
        attrs_content=soup.select('div#j-product-info-sku dl')
        attr_product_id=product_id
        attr_reference='P' + product_id
        attr_names=''
        attr_values=''
        attr_type='radio'
        i=0
        for dl in attrs_content:
            i=i + 1
            print(i)
            attr_key=dl.dt.string.rstrip(':')
            split_char='' if i == 1 else ','
            attr_names+=split_char + attr_key + ':' + attr_type + ':' + str(i - 1)
            print('attr_names:', attr_names)
            dlli=dl.select('li')
            dllis=[]
            for lli in dlli:
                if lli.has_attr('class') and lli['class'][0] == 'item-sku-image':
                    vname=lli.a['title']
                    if (lli.a.img):
                        pic=lli.a.img['src'].replace('_50x50.jpg', '')
                        if not (pic in product_images):
                            product_images.append(pic)
                        product_images_alt_text.append(vname)
                        pic_index=product_images.index(pic)
                    dllis.append([vname + ':' + str(i - 1), str(pic_index + 1), pic])
                elif lli.span:
                    vname=lli.a.span.string
                    dllis.append([vname + ':' + str(i - 1)])
                else:
                    pass
            attrs_array.append(dllis)
        print(attrs_array)
        attr_values_array=reduce(get_attr_content, attrs_array) if len(attrs_array) > 0 else []
        attr_products=[]
        n=0
        for v in attr_values_array:
            n+=1
            attr_ref=re.sub(r':\d\,|:\d', ' ', v[0]).replace(' ', '-') + attr_reference
            attr_img_pos = '' if len(v) == 1 else v[1]
            attr_img_pos = (attr_img_pos + ',' + img_pos_str) if n == 1 else attr_img_pos
            # Product ID*;Product Reference;Attribute (Name:Type:Position)*;Value (Value:Position)*;v[0].replace(',','-')
            # Supplier reference;Reference;EAN13;UPC;#Wholesale price;Impact on price;Ecotax;Quantity;Minimal quantity;Low stock level;Low stock alert;
            # Impact on weight;Default (0 = No, 1 = Yes);Combination available date;
            # Image position;Image URLs (x,y,z...);Image alt texts (x,y,z...);ID / Name of shop;Advanced Stock Managment;Depends on stock;Warehouse
            attr_string=product_id + '\;' + 'P' + product_id + '\;' + attr_names + '\;' + v[0] + '\;' + \
                        supplier_ref + '\;' + attr_ref + '\;' + ean_13 + '\;' + upc + '\;0\;0\;0\;0\;0\;0\;0\;' + \
                        '0\;' + ('1\;' if n == 1 else '0\;') + '2999-12-31\;' + attr_img_pos + '\;\;\;1\;0\;0\;0\;'
            attr_products.append(attr_string)

        # 查找产品描述
        # psummary=soup.select('div.product-property-main')
        features=''
        psummary=soup.find('div', id=None, class_='product-property-main')
        feature_lis=psummary.select('li')
        lin=0
        for lli in feature_lis:
            lin+=1
            spans=lli.get_text()

            features+=spans.replace('\n', '').replace(',','，') + ':' + str(lin) + ','
        features=features.rstrip(',')

        # print('features', features)
        # pdesc = soup.select('div.product-video-main,div.product-description-main')
        pdescvideo=soup.find('div', class_='product-video-main')
        # print(pdescvideo)

        pdesc=soup.find('div', class_='product-description-main')
        kses=pdesc.find_all('kse:widget')
        if kses != None:
            for kse in kses:
                kse.decompose()
        # print('Product desc')
        # print(pdesc)

        package=soup.find('div', class_='pnl-packaging-main')
        # print(str(package))
        pattern=re.compile(r'(\d+|\d+\.\d+)([cm]+)')
        result1=pattern.findall(str(package))
        width=result1[0][0]
        height=result1[1][0]
        depth=result1[2][0]

        pattern=re.compile(r'(\d+|\d+\.\d+)([kg]+)')
        result1=pattern.findall(str(package))
        weight=result1[0][0]

        product_desc=(str(psummary) + str(pdescvideo) + str(pdesc) + str(package)).replace('\n', '')
        product_desc=re.sub(r'data\-[\w\-="\.]*', '', product_desc)

        # 产品中的图片
        # 产品中的相关产品列表
        #
        #
        # Prestashop中Attribute的图片Atribute，及产品详情中Atribute对应的图片
        # Product ID;Active (0/1);Name *;Categories (x,y,z...);
        # Price tax included;Tax rules ID;Wholesale price;On sale (0/1);
        # Discount amount;Discount percent;Discount from (yyyy-mm-dd);Discount to (yyyy-mm-dd);
        # Reference #;Supplier reference #;Supplier;Manufacturer;EAN13;UPC;Ecotax;
        # Width;Height;Depth;Weight;delivery in stock;delivery out stock;Quantity;Minimal quantity;Low stock threshold;low stock alert;Visibility;Additional shipping cost;Unity;Unit price;
        # Short description;Description;Tags (x,y,z...);Meta title;Meta keywords;Meta description;URL rewritten;
        # Text when in stock;Text when backorder allowed;Available for order (0 = No, 1 = Yes);Product available date;Product creation date;Show price (0 = No, 1 = Yes);
        # Image URLs (x,y,z...);Image alt texts (x,y,z...);Delete existing images (0 = No, 1 = Yes);Feature(Name:Value:Position);Available online only (0 = No, 1 = Yes);Condition;
        # Customizable (0 = No, 1 = Yes);Uploadable files (0 = No, 1 = Yes);Text fields (0 = No, 1 = Yes);Out of stock;ID / Name of shop;Advanced stock management;Depends On Stock;Warehouse

        product_string=product_id + '\;1\;' + product_name.string + '\;' + category_name + '\;' + \
                       product_price + '\;' + '\;' + '0\;1\;' + \
                       '\;\;\;\;' + \
                       'P' + product_id + '\;' + supplier_ref + '\;' + supplier + '\;' + manufacturer + '\;' + ean_13 + '\;' + upc + '\;0\;' + \
                       width + '\;' + height + '\;' + depth + '\;' + weight + '\;\;\;1000\;1\;2\;\;0\;0\;\;\;' + \
                       short_desc + '\;' + product_desc + '\;\;' + head_title + '\;' + meta_keywords + '\;' + meta_desc + '\;' + rewriteurl + '-' + product_id + '\;' + \
                       '\;\;1\;\;' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\;1\;' + \
                       ','.join(product_images) + '\;' + ','.join(
            product_images_alt_text) + '\;0\;' + features + '\;0\;new\;' + \
                       '0\;0\;0\;0\;0\;0\;0\;0'

        return [product_string, attr_products]

    def __del__(self):
        pass
