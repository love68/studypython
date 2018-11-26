import urllib.request
import os


response = urllib.request.urlopen("http://www.baidu.com")

html = response.read()

f = open("baidushouye.html","wb+")

f.write(html)

f.close()




