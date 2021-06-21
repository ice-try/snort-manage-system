# coding=utf-8
import os
import sys
if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'snort.settings')


from panel.config import *
from panel.db import *




def job():
    # 导出json路径
    cur_path = sys.path[-1]
    print os.getcwd()
    jsonStyleFilePath = get_rule_json(os.getcwd(), 0)
    print "jsonStyleFilePath===" + jsonStyleFilePath
    # python ruleFormat.py toZnids txtStyleFilePath jsonStyleFilePath
    tool_path = from_other_get_tool_path(os.getcwd(), 0)
    print "tool_path===" + tool_path
    # 库里读取数据另存为得路径
    txtStyleFilePath = get_rule_from_db(os.getcwd(), 0)
    if not os.path.exists(txtStyleFilePath):
        os.makedirs(txtStyleFilePath)
    if not os.path.exists(jsonStyleFilePath):
        os.makedirs(jsonStyleFilePath)
    #os.system('cp '+ tool_path + '/fromDB.rules '+os.path.join(txtStyleFilePath,"fromDB.rules"))
    newer_db_to_rule_file(os.path.join(txtStyleFilePath, "fromDB.rules"))
    cmd = 'python ' + os.path.join(tool_path, 'ruleFormat.py') + \
          ' toZnids ' + os.path.join(txtStyleFilePath, 'fromDB.rules') + ' ' + \
          os.path.join(jsonStyleFilePath, 'export.rules')
    print(cmd)
    os.system(cmd)


if __name__ == "__main__":
    job()
