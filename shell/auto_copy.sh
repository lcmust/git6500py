#!/bin/bash
target_dir=$1
shift 1
for i in $* ;
do
    cp $i $target_dir
done
