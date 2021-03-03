# -*- coding: UTF-8 -*-

import os


# 判定文件夹是否存在，不存在则创建
def test_dir_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
