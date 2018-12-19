# -*- coding: utf-8 -*-
class Phone(object):
    def __send_msg(self):
        print("正在发送短信")

    def send_msg(self,money):
        if(money>0):
            self.__send_msg()
        else:
            print("余额不足，请先充值。。。")

phone = Phone()
phone.send_msg(-1)


