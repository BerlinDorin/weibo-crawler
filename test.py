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



def main():
    try:
        config = get_config()
        print(config)
    except Exception as e:
        print('Error: ', e)


if __name__ == '__main__':
    main()
