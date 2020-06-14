# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Time: 2020/6/14 18:04
# @Author: Berlin
------------------------------------------------- 
# @Desc：Summary of function here
# @Params : 
#    1.
#    2.
# @Return : Summary of return here
#    more details of return here
# @Raises :
#    1.
#    2.
-------------------------------------------------
"""
import os
import sys
import json

def get_config():
    """获取config.json文件信息"""
    config_path = os.path.split(
        os.path.realpath(__file__))[0] + os.sep + 'config.json'
    if not os.path.isfile(config_path):
        sys.exit(u'当前路径：%s 不存在配置文件config.json' %
                 (os.path.split(os.path.realpath(__file__))[0] + os.sep))
    try:
        with open(config_path, encoding='utf-8') as f:
            config = json.loads(f.read())
            return config
    except ValueError:
        sys.exit(u'config.json 格式不正确')

def main():
    try:
        config = get_config()
        print(config)
    except Exception as e:
        print('Error: ', e)


if __name__ == '__main__':
    main()
