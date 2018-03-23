#应用HTMLParser包，看看包中有什么方法可以处理
#重写了原来的方法
from html.parser import HTMLParser
class Myhtml(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print('Start:',tag)
        for ele in attrs:
            print('->',ele[0],'>',ele[1])

    def handle_endtag(self,tag):
        print('End:',tag)

    def handle_startendtag(self,tag,attrs):
        print('Empty:',tag)
        for ele in attrs:
            print('->',ele[0],'>',ele[1])

MyParser = Myhtml()
MyParser.feed(''.join([input().strip() for _ in range(int(input()))]))





