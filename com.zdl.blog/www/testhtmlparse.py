from html.parser import HTMLParser

contenthtml=''
def _attr(attrlist, attrname):
    for attr in attrlist:
        if attr[0] == attrname:
            return attr[1]
    return None
class MyHTMLParser(HTMLParser):
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.flag=0
        self.endflag=0
        self.divflag=False    

    def handle_starttag(self, tag, attrs):
        """
        recognize start tag, like <div>
        :param tag:
        :param attrs:
        :return:
        """
        self.flag=self.flag+1        
        print("Encountered a start tag:", tag)
        print("Encountered a start flag:", self.flag)
        if(tag=='div' and _attr(attrs,"class")=="divclass"):
            self.divflag=True

    def handle_endtag(self, tag):
        """
        recognize end tag, like </div>
        :param tag:
        :return:
        """
        self.endflag=self.endflag+1
        print("Encountered an end tag :", tag)
        print("Encountered an end flag:", self.endflag)
    def handle_data(self, data):
        """
        recognize data, html content string
        :param data:
        :return:
        """
        if(self.divflag==True ):
            print("Encountered some data  :", data)

    def handle_startendtag(self, tag, attrs):
        """
        recognize tag that without endtag, like <img />
        :param tag:
        :param attrs:
        :return:
        """  

        print("Encountered startendtag :", tag)

    def handle_comment(self,data):
        """

        :param data:
        :return:
        """
        print("Encountered comment :", data)


parser = MyHTMLParser()
parser.feed('''<html>
    <head>
        <title>Test</title>
    </head>
    <body><div class="divclass">
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
</html>''')