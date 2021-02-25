# -*- coding: UTF-8 -*-

import re

msg_pattern = re.compile(r'msg:.*;')
double_quote_pattern = re.compile(r'\"(.*)\"')
sid_pattern = re.compile(r'sid:.*;')


# hit_rule_pattern = re.compile(r'[*].*[*]')

#
# def get_rule_msg_id():
#     with open('all.rules', 'r') as f:
#         get = f.readlines()
#     if len(get) > 0:
#         for i in range(len(get)):
#             line = get[i]
#             if not line.startswith('#'):
#                 msg_line = msg_pattern.search(line)
#                 sid_line = sid_pattern.search(line)
#                 if msg_line is not None and sid_line is not None:
#                     msg = double_quote_pattern.findall(msg_line.group().split(';')[0])[0]
#                     print msg
#                     sid = sid_line.group().split(';')[0].replace('sid:', '')
#                     print sid


def get_hit_result():
    with open('log/fast.log', 'r') as f:
        hit_lines = f.readlines()
    hit_lines_len = len(hit_lines)
    if hit_lines_len > 0:
        for i in range(hit_lines_len):
            hit_result = hit_lines[i].split('[**]')[1]
            hit_rule_id = hit_result.split(']')[0].split(':')[1]
            print hit_rule_id
            hit_rule_name = hit_result.split(']')[1].strip()
            print hit_rule_name


# get_rule_msg_id()
get_hit_result()
