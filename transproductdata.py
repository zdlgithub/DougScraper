import mysql.connector as sc
from mysql.connector import errorcode
import datetime,os,settings,re

try:
    print('begin:'+datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    cnx = sc.connect(user='root', password='Dx+1234', host='127.0.0.1', database='test')
    cursor = cnx.cursor()
    cursor.execute('''select sku,meta_keywords,description, description_short, specification,title, meta_title, meta_description, name, name_url,
                    list_price, price, weight,packaging_height, packaging_length, packaging_width, declaration_name,pic_large,
                    func_getcategorynames(c_level_2) as category_name,
                    case when isnull(c_level_3) then func_getcategorynames(c_level_2) else func_getcategorynames(c_level_3) end as category_name3
                     from product order by sku''')
    i = 10000
    k = 1
    supplier_ref = supplier = manufacturer = ean_13 = upc = ''
    file_head = 'Product ID^Active (0/1)^Name *^Categories (x,y,z...)^Price tax included^Tax rules ID^Wholesale price^On sale (0/1)^Discount amount^Discount percent^Discount from (yyyy-mm-dd)^Discount to (yyyy-mm-dd)^Reference #^Supplier reference #^Supplier^Manufacturer^EAN13^UPC^Ecotax^Width^Height^Depth^Weight^delivery in stock^delivery out stock^Quantity^Minimal quantity^Low stock threshold^Low Stock Alert^Visibility^Additional shipping cost^Unity^Unit price^Short description^Description^Tags (x,y,z...)^Meta title^Meta keywords^Meta description^URL rewritten^Text when in stock^Text when backorder allowed^Available for order (0 = No, 1 = Yes)^Product available date^Product creation date^Show price (0 = No, 1 = Yes)^Image URLs (x,y,z...)^Image alt texts (x,y,z...)^Delete existing images (0 = No, 1 = Yes)^Feature(Name:Value:Position)^Available online only (0 = No, 1 = Yes)^Condition^Customizable (0 = No, 1 = Yes)^Uploadable files (0 = No, 1 = Yes)^Text fields (0 = No, 1 = Yes)^Out of stock^ID / Name of shop^Advanced stock management^Depends On Stock^Warehouse'
    current_datetime=datetime.datetime.now().strftime('%Y%m%d%H')
    product_file_path = os.path.join(settings.BASE_DIR,'datafiles','product_special_'+current_datetime+'_1.csv')
    pfs=open(product_file_path, 'a+', encoding='utf-8')
    pfs.write(file_head)
    for sku, meta_keywords, description, description_short, specification, title, meta_title, meta_description,\
        name, name_url, list_price, price, weight, packaging_height, packaging_length, packaging_width,\
        declaration_name, pic_large, category_name,category_name3 in cursor:
        # print(c)
        i += 1
        if i % 30 == 0:
            k += 1
            pfs.close()
            current_datetime=datetime.datetime.now().strftime('%Y%m%d%H')
            product_file_path=os.path.join(settings.BASE_DIR, 'datafiles',
                                           'product_special_' + current_datetime + '_'+str(k)+'.csv')
            pfs=open(product_file_path, 'a+', encoding='utf-8')
            pfs.write(file_head)
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
        title = title.replace('\n','')
        name = re.sub('[=]+',' ',name)
        head_title = name + ' in ' + category_name3.replace('/', ' ').replace('AS ', '') + ' on athereshopping.com'
        meta_keywords = category_name3.replace('/', ', ').replace('AS ', '')
        meta_desc = 'Find More Information about ' + name + ' in '+category_name3.replace('/', ' ').replace('AS ', '') + ' by athereshopping.com'
        rewriteurl = name_url
        product_id = str(i)
        short_desc = title
        features=''
        description = (description + specification).replace('\n', '')
        description=re.sub('href="http://www.dx.com/p/[\w#-.]*"', 'href="#"',description)
        description=re.sub('href="javascript:;"', 'href="#"', description)
        description=re.sub('<iframe[\w=/.:*;%?# &"\->]*</iframe>', '',description)
        description=re.sub('[ ]{2,}', ' ',description)
        desreplace = 'All packages from DX.com are sent without DX logo or any information indicating DX.com. Due to package variations from suppliers, the product packaging customers receive may be different from the images displayed.'
        description= description.replace(desreplace, '').replace('dx.com','athereshopping.com')
        product_images = pic_large.replace('/productimages','https://partner.img.dxcdn.com/productimages').replace('/sbnimages','https://photo.volumerate.com/sbnimages').replace(';',',')
        product_string = product_id + '^1^' + name + '^' + 'AS Special/' + category_name.replace('AS Lights & Lighting','AS LED Lights & Flashlights').replace('AS VR Special/','') + '^' + \
                         str(price) + '^' + '^' + str(list_price) + '^1^' + \
                         '^^^^' + \
                         'P' + str(sku) + '^' + supplier_ref + '^' + supplier + '^' + manufacturer + '^' + ean_13 + '^' + upc + '^0^' + \
                         str(packaging_width) + '^' + str(packaging_height) + '^' + str(packaging_length) + '^' + str(weight) + '^^^9999^1^2^^0^0^^^' + \
                         short_desc + '^' + description + '^^' + head_title + '^' + meta_keywords + '^' + meta_desc + '^' + rewriteurl + '-' + product_id + '^' + \
                         '^^1^^' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '^1^' + \
                         product_images + '^^0^' + features + '^0^new^' + \
                         '0^0^0^0^0^0^0^0'
        print('successful:' + str(sku) + '_' + str(i))
        pfs.write('\n' + product_string)
    cursor.close()
    print('connect successful.')
except sc.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
except Exception as ec:
    print('error:'+str(sku)+'_'+str(i))
    print(ec)
else:
    cnx.close()
    print('closed')
    pfs.close()
print('end:'+datetime.datetime.now().strftime('%Y%m%d%H%M%S'))