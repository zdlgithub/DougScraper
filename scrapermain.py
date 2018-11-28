
from doughtmlparse import DougHtmlParse
import os, settings, datetime


if __name__ == '__main__':
    line_strings = []
    # 整理资料格式product_id;category_name;url
    url_file_path = os.path.join(settings.BASE_DIR,'datafiles','webpageurl.csv')
    current_datetime = datetime.datetime.now().strftime('%Y%m%d%H')
    product_file_path = os.path.join(settings.BASE_DIR,'datafiles','products_'+current_datetime+'.csv')
    combination_file_path=os.path.join(settings.BASE_DIR, 'datafiles', 'combinations_' + current_datetime + '.csv')

    with open(url_file_path,'r') as fs:
        for fl in fs.readlines():
            line_strings.append(fl)
    print(line_strings)
    pfs = open(product_file_path,'a+', encoding='utf-8')
    cfs=open(combination_file_path, 'a+', encoding='utf-8')
    for ls in line_strings:
        try:
            urls = ls.split(';')
            dhp = DougHtmlParse()
            html_text = dhp.get_product_info(urls[0],urls[1],urls[2])
        except Exception as e:
            print('Get URL Error:%s,ErrorInfo:%s' % urls[0],urls[2], repr(e))

        print(1)
        pfs.write('\n' + html_text[0])
        for ht in html_text[1]:
            cfs.write('\n' + ht)
    pfs.close()
    cfs.close()