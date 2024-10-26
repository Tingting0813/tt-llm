#!/bin/bash
# 检查~/.bashrc文件是否已经包含指定的命令
if grep -Fxq "source /opt/conda/bin/activate base" ~/.bashrc
then
    echo "Command already added."
else
    # 如果没有包含，则将命令添加到~/.bashrc文件的末尾
    echo "source /opt/conda/bin/activate base" >> ~/.bashrc
    echo "Command added to ~/.bashrc"
fi