import re
from functools import reduce



# tmpstring = 'abc weight height depth 30cm x 20cm x 2.0cm (11.81in x 7.87in x 0.79in)'

# pattern = re.compile(r'(\d+|\d+\.\d+)([cm]+)')
# result1=pattern.findall(tmpstring)
# print(result1)

# it = re.finditer(r"(\d+|\d+\.\d+)[cm]+",tmpstring)

# for match in it:
# 	print(match.group())


# divstring ='''<div class="ui-box product-description-main" data-widget-cid="widget-28" id="j-product-description">
# 				<div class="ui-box-title" data-spm-anchor-id="2114.10010108.0.i9.41214a7e3AvA4k">Product Description</div>'''
# reobj = re.findall(r'data\-[\w\-="\.]*',divstring)
# print(reobj)

# dstr = re.sub(r'data\-[\w\-="\.]*','',divstring)
# print(dstr)

# rewriteurl=re.sub(r'[+":/&?#()*^,)]+', ' ', r'Prod:u+?    c?  t_na+  m&  e.s    r/i(n#g)kk*k^kjjjjj,kkkkk').lower()
# rewriteurl=re.sub(r'[ ]+', '-', rewriteurl)
# print(rewriteurl)

attr_ref = re.sub(r':\d+\,|:\d+|[ ]+', '-', '6 Holes:01,abc Black:11')
print(attr_ref)
# # 
# restr =r'(\n|[aA]liexpress|[aA]libaba)+'
# attr_ref = re.sub(restr, 'athereshopping', 'aliexpressaliexpress.com ddd\nkfdk alibaba group')
# print(attr_ref)

# img_pos = reduce(lambda x, y: str(x)+',' +str(y), list(range(1,4)))
# print(list(range(1,4)))
# print(img_pos)

# match_result = re.match(r'(\d+\.\d+) \- (\d+\.\d+)','236.88')
# print(match_result)
# print(match_result.group(2))



# 	
# line = "Cats are smarter than dogs"
# matchObj = re.match( r'([a-z]*) are (.*?) .*', line, re.M|re.I)
# if matchObj:
#     print("matchObj.group() : ", matchObj.group())
#     print("matchObj.group(1) : ", matchObj.group(1))
#     print("matchObj.group(2) : ", matchObj.group(2))
# else:
#     print("No match!!")