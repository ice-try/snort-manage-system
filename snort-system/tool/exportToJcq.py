# coding=utf-8
import os
import sys

sys.path.append("../panel")
from config import *
from db import *


def job():
    # 导出json路径
    jsonStyleFilePath = get_rule_json(os.getcwd(), 1)
    print "jsonStyleFilePath===" + jsonStyleFilePath
    # python ruleFormat.py toZnids txtStyleFilePath jsonStyleFilePath
    tool_path = from_other_get_tool_path(os.getcwd(), 1)
    print "tool_path===" + tool_path
    # 库里读取数据另存为得路径
    txtStyleFilePath = get_rule_from_db(os.getcwd(), 1)
    if not os.path.exists(txtStyleFilePath):
        os.makedirs(txtStyleFilePath)
    if not os.path.exists(jsonStyleFilePath):
        os.makedirs(jsonStyleFilePath)
    newer_db_to_rule_file(os.path.join(txtStyleFilePath, "fromDB.rules"))
    cmd = 'python ' + os.path.join(tool_path, 'ruleFormat.py') + ' toZnids ' + os.path.join(txtStyleFilePath,
                                                                                            "fromDB.rules") + ' ' + os.path.join(
        jsonStyleFilePath, 'export.rules')
    print(cmd)
    os.system(cmd)


if __name__ == "__main__":
    job()
