#!/bin/bash
# 请编写一个Shell脚本，它把第二个位置参数及其以后的各个位置参数指定的文件复制到第一个位置参数执行的目录中。
# 请问如何用最简单的方法编写
# http://segmentfault.com/q/1010000000152929
target_dir=$1
shift 1
for i in $* ;
do
    cp $i $target_dir
done
