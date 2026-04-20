#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
wxdump 主程序入口
基于 PyWxDump 的优化升级版本
"""

import argparse
import os
import sys

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pywxdump.cli import console_run


def main():
    """主程序入口"""
    # 如果没有提供任何参数，直接启动API服务
    if len(sys.argv) == 1:
        # 添加 api 参数来启动API服务
        sys.argv.append('api')

    # 调用原始CLI
    console_run()

if __name__ == "__main__":
    main()
