# -*- coding: UTF-8 -*-


import os
import ConfigParser


def get_rule_from_db(cur_path, sub_num):
    """
        :describe:  获得json格式规则的导出路径，当调用该方法的文件与当前文件不在同一个目录下时使用
        :param:     cur_path是当前所在目录，sub_num是当前目录相对于当前目录的上级目录需要返回多少层
        :return:    json格式规则的导出路径
        """
    print "from_db"
    sub_str = ""
    if sub_num > 0:
        sub_str = ".."
        for i in range(sub_num - 1):
            sub_str += "/.."
    dir_path = os.path.abspath(os.path.join(cur_path, sub_str))
    path = dir_path + '/panel/config.ini'
    print path
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    from_db = cf.get('db', 'from_db')
    print from_db
    return from_db


def get_rule_json(cur_path, sub_num):
    """
        :describe:  获得json格式规则的导出路径，当调用该方法的文件与当前文件不在同一个目录下时使用
        :param:     cur_path是当前所在目录，sub_num是当前目录相对于当前目录的上级目录需要返回多少层
        :return:    json格式规则的导出路径
        """
    print "rule_json"
    sub_str = ""
    if sub_num > 0:
        sub_str = ".."
        for i in range(sub_num - 1):
            sub_str += "/.."
    dir_path = os.path.abspath(os.path.join(cur_path, sub_str))
    path = dir_path + '/panel/config.ini'
    print path
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    rule_json = cf.get('export', 'rule_json')
    print rule_json
    return rule_json


def from_other_get_tool_path(cur_path, sub_num):
    """
        :describe:  获得tool存储路径，当调用该方法的文件与当前文件不在同一个目录下时使用
        :param:     cur_path是当前所在目录，sub_num是当前目录相对于当前目录的上级目录需要返回多少层
        :return:    tool存储路径
        """
    sub_str = ""
    if sub_num > 0:
        sub_str = ".."
        for i in range(sub_num - 1):
            sub_str += "/.."
    dir_path = os.path.abspath(os.path.join(cur_path, sub_str))
    path = dir_path + '/panel/config.ini'
    print path
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    tool_path = cf.get('tool', 'tool_path')
    return tool_path


def get_tool_path():
    """
        :describe:  获得tool存储路径
        :param:     无
        :return:    tool存储路径
        """
    path = os.getcwd() + '/panel/config.ini'
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    tool_path = cf.get('tool', 'tool_path')
    return tool_path


def get_suricata_yaml_path():
    """
    :describe:  获得suricata配置文件存储路径
    :param:     无
    :return:    suricata配置文件存储路径
    """
    path = os.getcwd() + '/panel/config.ini'
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    yaml_path = cf.get('suricata', 'yaml_path')
    return yaml_path


def get_suricata_log_path():
    """
    :describe:  获得suricata日志存储路径
    :param:     无
    :return:    suricata日志存储路径
    """
    path = os.getcwd() + '/panel/config.ini'
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    log_path = cf.get('suricata', 'log_path')
    return log_path


def get_suricata_rule_path():
    """
    :describe:  获得suricata规则存储路径
    :param:     无
    :return:    suricata规则存储路径
    """
    path = os.getcwd() + '/panel/config.ini'
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    rule_path = cf.get('suricata', 'rule_path')
    return rule_path


def get_update_path():
    """
    :describe:  获得更新程序路径
    :param:     无
    :return:    更新程序路径
    """
    path = os.getcwd() + '/panel/config.ini'
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    update_path = cf.get('update', 'update_path')
    return update_path


def get_rules_path():
    """
    :describe:  获得规则文件目录
    :param:     无
    :return:    规则文件目录
    """
    path = os.getcwd() + '/panel/config.ini'
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    rules_path = cf.get('update', 'new_rules_path')
    return rules_path


def get_file_path():
    """
    :describe:  获得names文件目录
    :param:     无
    :return:    names文件目录
    """
    path = os.getcwd() + '/panel/config.ini'
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    file_path = cf.get('tmp', 'path')
    return file_path


def get_upload_path():
    """
    :describe:  获得文件上传目录
    :param:     无
    :return:    文件上传目录
    """
    path = os.getcwd() + '/panel/config.ini'
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    file_path = cf.get('upload', 'path')
    return file_path


def get_download_path():
    """
    :describe:  获得规则导出目录
    :param:     无
    :return:    规则导出目录
    """
    path = os.getcwd() + '/panel/config.ini'
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    file_path = cf.get('download', 'path')
    return file_path


def get_pcap_path():
    """
    :describe:  获得pcap文件目录
    :param:     无
    :return:    pcap文件目录
    """
    path = os.getcwd() + '/panel/config.ini'
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    file_path = cf.get('pcap', 'download_path')
    return file_path


def get_stor_path():
    """
    :describe:  获得规则出库存储目录
    :param:     无
    :return:    规则出库存储目录
    """
    path = os.getcwd() + '/panel/config.ini'
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    file_path = cf.get('rule', 'rules_path')
    return file_path


def get_names_stor_path():
    """
    :describe:  获得特征出库存储目录
    :param:     无
    :return:    特征出库存储目录
    """
    path = os.getcwd() + '/panel/config.ini'
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    file_path = cf.get('rule', 'names_path')
    return file_path


def get_zip_path():
    """
    :describe:  获得zip文件目录
    :param:     无
    :return:    zip文件目录
    """
    path = os.getcwd() + '/panel/config.ini'
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    file_path = cf.get('download', 'zip_path')
    return file_path


def get_tmp_rule():
    """
    :describe:  获得临时规则文件目录
    :param:     无
    :return:    临时规则文件目录
    """
    path = os.getcwd() + '/panel/config.ini'
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    file_path = cf.get('tmp', 'rule')
    return file_path


def get_tmp_dir():
    """
    :describe:  获得临时目录
    :param:     无
    :return:    临时目录
    """
    path = os.getcwd() + '/panel/config.ini'
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    file_path = cf.get('tmp', 'dir')
    return file_path


def get_time():
    """
    :describe:  获得更新规则周期
    :param:     无
    :return:    days: 哪天 hours: 几时 minutes: 几分
    """
    path = os.getcwd() + '/panel/config.ini'
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    days = cf.get('update', 'days')
    hours = cf.get('update', 'hours')
    minutes = cf.get('update', 'minutes')
    return days, hours, minutes


def get_url():
    """
    :describe:  获得同步规则URL
    :param:     无
    :return:    URL
    """
    path = os.getcwd() + '/panel/config.ini'
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    url = cf.get('update', 'url')
    return url


def get_storage_path():
    """
    :describe:  获得下载后规则存储目录
    :param:     无
    :return:    规则存储目录
    """
    path = os.getcwd() + '/panel/config.ini'
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    rules_path = cf.get('update', 'rules_path')
    return rules_path


def get_xlsx_path():
    """
    :describe:  获得xlsx文件存储目录
    :param:     无
    :return:    xlsx文件存储目录
    """
    path = os.getcwd() + '/panel/config.ini'
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    rules_path = cf.get('download', 'xlsx_path')
    return rules_path


def get_extract_path():
    """
    :describe:  获得特征提取脚本目录
    :param:     无
    :return:    特征脚本目录
    """
    path = os.getcwd() + '/panel/config.ini'
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    rules_path = cf.get('extract', 'path')
    return rules_path


def get_tmp_names_path():
    """
    :describe:  获得特征提取后names文件暂存路径
    :param:     无
    :return:    names暂存路径
    """
    path = os.getcwd() + '/panel/config.ini'
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    rules_path = cf.get('tmp', 'path')
    return rules_path


def get_out_names_path():
    """
    :describe:  获得导出包含的规则names文件存储路径
    :param:     无
    :return:    导出包含的规则names文件存储路径
    """
    path = os.getcwd() + '/panel/config.ini'
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    rules_path = cf.get('rule', 'out_names')
    return rules_path
