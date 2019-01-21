import json
'''
可以将字符串转换为python对象
'''

l = '[1, 2, 3, 4]'

#print(json.loads(l))

strDict = '{"city": "北京", "name": "大猫"}'

print(json.loads(strDict))

