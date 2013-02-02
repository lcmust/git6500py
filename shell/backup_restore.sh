#!/bin/bash
#backup your files || restore your backup files
#backup :filename <----to---> backup_filename
#restore:backup_filename <--to-->  filename
#function 1: backup
#function 2: restore
#
#shell command:(sudo script_filename backup  /path/to/ zs-backup_filename )
#backup :filename <----to---> zs-backup_filename
#
#shell command:(sudo script_filename restore /path/to/ backup_filename )
#restore:backup_filename <--to-->  filename

#/mnt/sda3 HAS 5 operating system: "rh5" "ct62" "" "" ""
#now(20120517-1050) is :"ct62"

backup_or_restore=$1
target_path=$2
to_process=$3
to_process=${to_process:-"zs-"}
###echo ${back_or_restore}
###echo ${to_process}

function test_ls {
cd ${target_path}
for file_name in `ls |grep -Ei  "${to_process}"`
    do
	ls -dF ${file_name}
    done
}

function backup {
echo "Begin:"
cd ${target_path}
for file_name in `ls |grep -Evi  "zs-|vmware|tools"`
    do
    	new_file_name="${to_process}_${file_name}"
    	mv ${file_name} ${new_file_name}
    	echo "BackupFrom:${file_name} TO: ${new_file_name}"
    done
echo "OK!"
}

restore() {
echo "Begin:"
cd ${target_path}
for file_name in `ls |grep -Ei  "${to_process}"`
    do
    	old_file_name=${file_name#*_}
    	mv ${file_name} ${old_file_name}
    	echo "RestoreFrom:${file_name} TO: ${old_file_name}"
    done
echo "OK!"
}

${backup_or_restore} ${to_process}
