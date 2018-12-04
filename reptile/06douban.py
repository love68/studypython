#!/usr/bin/env/ python3
# -*- encoding=utf-8 -*-

import urllib.request
import ssl

context = ssl._create_unverified_context()

def movieSpider():
    """
        模拟Ajax请求
    """

    url = "https://movie.douban.com/j/chart/top_list?"

    header = {"User-Agent" : "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.7.62 Version/11.01"}

    formData = {
            "type" : "11",
            "interval_id" : "100:90",
            "action" : "",
            "start" : "0",
            "limit" : "20"
        }

    #将str类型转换为bytes类型
    data = urllib.parse.urlencode(formData).encode("utf-8")

    request = urllib.request.Request(url, data=data, headers=header)

    print(urllib.request.urlopen(request,context=context).read().decode("utf-8"))

if __name__ == "__main__":
    movieSpider()

