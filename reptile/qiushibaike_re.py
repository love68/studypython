import re
import urllib
import urllib.request

url = "https://www.qiushibaike.com/8hr/page/1/"

headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}

request = urllib.request.Request(url,headers=headers)

response = urllib.request.urlopen(request)

html = response.read().decode("UTF-8")

#爬取用户名
#pattern = re.compile(r"<h2>(.*?)</h2>",re.S)

#爬取内容
pattern = re.compile(r'<div class="content">(.*?)</div>',re.S)


content_list = re.findall(pattern,html)

for content in content_list:
    print(content)

