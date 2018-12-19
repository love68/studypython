# -*- coding: utf-8 -*-
'''
企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高
　　　于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提
　　　成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于
　　　40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于
　　　100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
'''
print("请输入利润")
profit_input = input()
profit = int(profit_input)
profit = profit / 100000
boss = 0
if profit < 1:
    print("发放第一级奖金")
    boss = profit * 0.1 * 100000
elif profit < 2:
    print("发放第二级奖金")
    boss = 100000 * 0.1 + (profit - 100000)*0.075
elif profit < 4:
    print("发放第三级奖金")
    boss = (profit-200000)*0.05
else:
    print("发放第四级奖金")
    boss = profit*0.01
print("当月的奖金为"+str(profit)+"元")


