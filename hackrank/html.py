#Ӧ��HTMLParser��������������ʲô�������Դ���
#��д��ԭ���ķ���
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





