# -*- coding: UTF-8 -*-
import re
import os


class GetHitRule(object):
    """
    获取命中上传的pcap的规则
    """

    def __init__(self):
        self.result_path = r"F:\Projects\PycharmProjects\snort-manage-system\snort-system\test\log"
        # self.result = ""
        self.result = []
        self.tips = ""
        self.sid_list = []
        self.result_list = []

    def read_result(self):
        """
        :describe:  读取命中结果文件
        :param:     类对象
        :return:    无
        """
        try:
            with open(os.path.join(self.result_path, 'fast.log')) as f:
                self.result_list = f.readlines()
                print self.result_list
        except IOError as e:
            print 'error:', e
        if len(self.result_list) > 0:
            self.result = self.result_list
            # index = len(self.result_list) - 1
            # self.result = self.result_list[index]
            print self.result
        else:
            pass

    def judge_hit_rule(self):
        """
        :describe:  判断哪条规则命中
        :param:     类对象
        :return:    命中pcap的规则ID列表
        """
        sid_list = []
        hit_list = []
        if len(self.result) == 0:
            return None
        for i in range(len(self.result)):
            hit_result = self.result[i].split('[**]')[1]
            hit_rule_id = hit_result.split(']')[0].split(':')[1]
            print hit_rule_id
            hit_rule_name = hit_result.split(']')[1].strip()
            print hit_rule_name
            hit_dict = {hit_rule_id: hit_rule_name}
            hit_list.append(hit_dict)
            sid_list.append(hit_rule_id)
        # try:
        #     sid_list = re.findall(r'hit rules\:(.+?):', self.result)
        # except Exception as e:
        #     print 're find error:', e
        if len(sid_list) == 0:
            return None
        else:
            self.sid_list = sid_list
        return self.sid_list

    def get_hit_result(self):
        """
        :describe:  获取命中信息
        :param:     类对象
        :return:    命中规则描述
        """
        self.read_result()
        sid_list = self.judge_hit_rule()
        if sid_list is None:
            self.tips = '未命中任何规则!'
        else:
            self.tips = '命中%s号规则!' % self.sid_list
        print self.tips
        return self.tips


# GetHitRule.get_hit_result()
hit = GetHitRule()
hit.get_hit_result()
