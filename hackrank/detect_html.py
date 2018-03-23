# 重写HTMLParser方法
# 重写handle_starttag方法


from html.parser import HTMLParser
class MyhtmlParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]


html = '\n'.join([input() for _ in range(int(input()))])
parser = MyhtmlParser()
parser.feed(html)
parser.close()




