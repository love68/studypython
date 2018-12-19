import requests
import json
import time
import random

headers = {
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 8.1.0; \
    Mi Note 3 MIUI/V10.0.4.0.OCHCNFH)"
}
t1 = int(time.time())

# 顶级url获取列表
topurl = "http://w.pandora.xiaomi.com/api/a2/gallery/rank?kind=latest&offset=0&_net_type=1\
&count=30&delta=0&_vname=M918103130-MA&_vcode=2018103130&_res=hd1080&_nonce=-357004631\
&_bat_lev=91&_devtype=1&_andrver=27&_locale=zh_CN\
&_miui_ver_t=stable&_ts=" + str(t1)

# 获取响应文件
response = requests.get(topurl, headers=headers).text


# 转成Python对象
items = json.loads(response)["items"]

ip = ["118.180.21.203", "118.180.21.194"]

for item in items:
    t2 = int(time.time())
    id1 = item["meta"]["album_info"]["id"]

    # 每组图片的地址
    urlLevel2 = "http://w.pandora.xiaomi.com/api/a3/gallery/\
    notify_express?_net_type=1&_res=hd1080&id=" + \
        id1 + "&_ts=" + str(t2)
    text = requests.get(urlLevel2, headers=headers).text
    datas = json.loads(text)["items"]
    for data in datas:
        addr = data["images"][0]["cl_url"]["locator"]
        # 具体图片的地址
        fullurl = "http://" + random.choice(ip) \
            + "/wallpaper.cdn.pandora.xiaomi.com/thumbnail/webp/w1080/" + addr
        image = requests.get(fullurl, headers=headers).content
        with open("d:\\image\\xiaomi\\" + data["id"] + ".webp", "wb") as f:
            f.write(image)
