# -*- coding: UTF-8 -*-
import commands
import re
from db import *
from verify_pcap import *


def rules_verify(rule):
    """
    :describe:  验证规则是否被支持
    :param:     待验证规则文件
    :return:    True:支持 False:不支持
    """
    get_suricata_rules()
    suricata_log_path = get_suricata_log_path()
    test_dir_exists(suricata_log_path)
    yaml_path = get_suricata_yaml_path()
    # cmd = './tool/test_tool ' + rule
    cmd = 'suricata -c ' + yaml_path + ' -S ' + rule + ' -T -l ' + suricata_log_path
    result = commands.getstatusoutput(cmd)
    # result = re.findall(r'Rule(.+?):', str(result))
    rule_file_size = os.path.getsize(rule)
    # print rule_file_size
    if rule_file_size != 0:
        # print re.search(r'error parsing signature', result[1])
        if 'error parsing signature' in result[1]:
            return False
        else:
            return True
    else:
        return True
    # if len(result) != 0:
    #     if 'unsupported' in result[0]:
    #         return False
    #     else:
    #         return True
    # else:
    #     return True


def is_hit(rule, pcap, user, ip):
    result = []
    sid_list = []
    hit_list = []
    """
    :describe:      检测规则是否命中pcap
    :param param1:  待检测规则文件
    :param param2:  待检测pcap文件
    :param param3:  当前登录用户
    :return:        True:命中 False:未命中
    """
    # cmd = './tool/test_tool ' + rule + ' ' + pcap
    get_suricata_rules()
    suricata_log_path = get_suricata_log_path()
    test_dir_exists(suricata_log_path)
    yaml_path = get_suricata_yaml_path()
    cmd = 'suricata -c ' + yaml_path + ' -S ' + rule + ' -r ' + pcap + ' -l ' + suricata_log_path
    os.system(cmd)
    result_path = os.path.join(suricata_log_path, 'fast.log')
    del_cmd = 'rm -rf ' + suricata_log_path + '*'
    # print 'del_cmd' + del_cmd
    if not os.path.exists(result_path):
        record_log(filter(str.isdigit, rule), '规则检测',
                   user, '失败', ip, '规则有问题')
        return False
    if os.path.getsize(result_path) == 0:
        record_log(filter(str.isdigit, rule), '规则检测',
                   user, '失败', ip, '%s未命中规则%s' % (pcap, rule))
        os.system(del_cmd)
        return False

    with open(result_path, 'r')as f:
        result = f.readlines()
    if len(result) == 0:
        record_log(filter(str.isdigit, rule), '规则检测',
                   user, '失败', ip, '%s未命中规则%s' % (pcap, rule))
        os.system(del_cmd)
        return False
    for i in range(len(result)):
        hit_result = result[i].split('[**]')[1]
        hit_rule_id = hit_result.split(']')[0].split(':')[1]
        hit_rule_name = hit_result.split(']')[1].strip()
        hit_dict = {hit_rule_id: hit_rule_name}
        hit_list.append(hit_dict)
        sid_list.append(hit_rule_id)

    if len(sid_list) > 0:
        record_log(filter(str.isdigit, rule), '规则检测',
                   user, '成功', ip, '%s成功命中规则%s' % (pcap, rule))
        os.system(del_cmd)
        return True
    record_log(filter(str.isdigit, rule), '规则检测',
               user, '失败', ip, '%s未命中规则%s' % (pcap, rule))
    os.system(del_cmd)
    return False

    # try:
    #     sid_list = re.findall(r'hit rules\:(.+?):', self.result)
    # except Exception as e:
    #     print 're find error:', e

    # result = commands.getstatusoutput(cmd)
    # set_default_env()
    # if 'hit rules' in str(result):
    #     record_log(filter(str.isdigit, rule), '规则检测',
    #                user, '成功', ip, '%s成功命中规则%s' % (pcap, rule))
    #     return True
    # record_log(filter(str.isdigit, rule), '规则检测',
    #            user, '失败', ip, '%s未命中规则%s' % (pcap, rule))
    # return False
