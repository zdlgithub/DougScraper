from bs4 import BeautifulSoup

html='''
	<html>
    <head>
        <title>Test</title>
    </head>
    <body>
    <div class="divclass">
        <h1>Parse me!</h1>
        <div>
        <img src = "" />
        <p>A paragraph.</p></div>
        <p class = "p_font">A paragraph with class.</p>
        </div>
        <!-- comment -->
        <div>
            <p>A paragraph in div.</p>
        </div>
    </body>
	</html>
	'''

soup=BeautifulSoup(html,features="html.parser")
# print(soup.name)
# print(soup.div)
# soup.div['class']=['ca','ab']
# print(soup.div.string)
# soup.div.replace_with('testdiv')
# print(soup.div.string)
# print(soup.find_all('div'))
# for child in soup.body.descendants:
# 	print(child)
# for child in soup.body.contents:
# 	print(child)
# for child in soup.body.children:
# 	print(child)
# for child in soup.body.strings:
# 	print(child)
# for child in soup.body.stripped_strings:
# 	print(child)
# print(soup.div.next_sibling.next_sibling)
#print(soup.div.next_element.next_element)
# for child in soup.div.next_elements:
# 	print(child)
# soup.div.insert(1,'inster div')
# print(soup.div)
# newtag=soup.new_tag('i')
# newtag.string='instert i tag'
# soup.div.insert_before(newtag)
# print(soup.body)

# ntag=soup.new_tag('div')
# ntag.string='new div'
# soup.div.replace_with(ntag)
# print(str(soup.body.prettify()))
print(soup.div.get_text('|',strip=True))