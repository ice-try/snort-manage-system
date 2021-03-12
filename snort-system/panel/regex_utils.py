# -*- coding: UTF-8 -*-

import re


# 校验是否是非负整数且非0时不以0开头
def is_integer(num):
    num_pattern = re.compile(r'^[1-9]\d*|0$')
    test_flag = False
    if num is not None and num.isdigit():
        if num_pattern.match(num) is not None:
            test_flag = True
    return test_flag


# 校验是否是合法ip
def is_ip(ip):
    ip_flag = True
    if ip == "any":
        return True
    # ip_pattern = re.compile(r'((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')
    ip_list = str(ip).split('.')
    if len(ip_list) == 4:
        for i in range(4):
            if not is_integer(ip_list[i]):
                ip_flag = False
                break
            if int(ip_list[i]) < 0 or int(ip_list[i]) > 255:
                ip_flag = False
                break
    else:
        ip_flag = False
    return ip_flag


# 校验是否是合法端口号
def is_port(port):
    port_flag = True
    if port == "any":
        return True
    if not is_integer(port) or int(port) < 0 or int(port) > 65535:
        port_flag = False
    return port_flag


def is_str_null(s):
    str_flag = False
    if s is None or s == "":
        str_flag = True
    return str_flag
