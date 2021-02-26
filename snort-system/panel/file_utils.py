# -*- coding: UTF-8 -*-

import os


def test_dir_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
