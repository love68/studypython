# -*- coding: utf-8 -*-
import os

os.chdir("G:\美剧\天堂执法者\天堂执法者第一季")

for temp in os.listdir():
    index2 = temp.find(".rmvb")
    index1 = temp.find(".Chi_Eng.")
    new_name = temp.replace(temp[index1+1:index2+1],"")
    print(new_name)
    os.rename(temp,new_name)
