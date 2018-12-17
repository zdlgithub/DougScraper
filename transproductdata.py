import mysql.connector as sc
from mysql.connector import errorcode
import datetime

try:
    cnx = sc.connect(user='root', password='Dx+1234', host='127.0.0.1', database='test')
    cursor = cnx.cursor()
    cursor.execute('''select sku,meta_keywords,description, description_short, specification,title, meta_title, meta_description, name, name_url,
                    list_price, price, weight,packaging_height, packaging_length, packaging_width, declaration_name,pic_large,
                    case when isnull(c_level_3) then func_getcategorynames(c_level_2) else func_getcategorynames(c_level_3) end category_name
                     from product where sku=129829''')
    i = 6000
    supplier_ref = supplier = manufacturer = ean_13 = upc = ''
    for sku, meta_keywords, description, description_short, specification, title, meta_title, meta_description,\
        name, name_url, list_price, price, weight, packaging_height, packaging_length, packaging_width,\
        declaration_name, pic_large, category_name in cursor:
        # print(c)
        i += 1
        print('sku:{},sku:{}'.format(sku, meta_keywords))
        # Product ID;Active (0/1);Name *;Categories (x,y,z...);
        # Price tax included;Tax rules ID;Wholesale price;On sale (0/1);
        # Discount amount;Discount percent;Discount from (yyyy-mm-dd);Discount to (yyyy-mm-dd);
        # Reference #;Supplier reference #;Supplier;Manufacturer;EAN13;UPC;Ecotax;
        # Width;Height;Depth;Weight;delivery in stock;delivery out stock;Quantity;Minimal quantity;Low stock threshold;low stock alert;Visibility;Additional shipping cost;Unity;Unit price;
        # Short description;Description;Tags (x,y,z...);Meta title;Meta keywords;Meta description;URL rewritten;
        # Text when in stock;Text when backorder allowed;Available for order (0 = No, 1 = Yes);Product available date;Product creation date;Show price (0 = No, 1 = Yes);
        # Image URLs (x,y,z...);Image alt texts (x,y,z...);Delete existing images (0 = No, 1 = Yes);Feature(Name:Value:Position);Available online only (0 = No, 1 = Yes);Condition;
        # Customizable (0 = No, 1 = Yes);Uploadable files (0 = No, 1 = Yes);Text fields (0 = No, 1 = Yes);Out of stock;ID / Name of shop;Advanced stock management;Depends On Stock;Warehouse
        head_title = title + ' in ' + category_name.replace('/', ' ').replace('AS ', '') + ' on athereshopping.com'
        meta_keywords = category_name.replace('/', ', ').replace('AS ', '')
        meta_desc = 'Find More Information about ' + name + ' in '+category_name.replace('/', ' ').replace('AS ', '') + ' by athereshopping.com'
        rewriteurl = name_url
        product_id = str(i)
        short_desc = ''
        features=''
        description = (description + specification).replace('\n', '')
        product_images = pic_large.replace('/productimages','https://partner.img.dxcdn.com/productimages').replace('/sbnimages','https://photo.volumerate.com/sbnimages').replace(';',',')
        product_string = product_id + '\;1\;' + title + '\;' + 'AS Special/' + category_name.replace('AS Lights & Lighting','AS LED Lights & Flashlights') + '\;' + \
                         str(list_price) + '\;' + '\;' + str(price) + '\;1\;' + \
                         '\;\;\;\;' + \
                         'P' + str(sku) + '\;' + supplier_ref + '\;' + supplier + '\;' + manufacturer + '\;' + ean_13 + '\;' + upc + '\;0\;' + \
                         str(packaging_width) + '\;' + str(packaging_height) + '\;' + str(packaging_length) + '\;' + str(weight) + '\;\;\;9999\;1\;2\;\;0\;0\;\;\;' + \
                         short_desc + '\;' + description + '\;\;' + head_title + '\;' + meta_keywords + '\;' + meta_desc + '\;' + rewriteurl + '-' + product_id + '\;' + \
                         '\;\;1\;\;' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\;1\;' + \
                         product_images + '\;\;0\;' + features + '\;0\;new\;' + \
                         '0\;0\;0\;0\;0\;0\;0\;0'
        print(product_string)
    cursor.close()
    print('cconnect successful.')
except sc.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()
    print('closed')