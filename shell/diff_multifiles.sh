#!/bin/bash
DIFF_COMMAND=/usr/bin/diff
global_result_equl=""
global_result_notequl=""
if [ -z $1 ]; then
	target_dir="/mnt/sda2h/tools/git1/git6500/bak_config/home_user"
else
	target_dir="$1"
fi
if [ -z $2 ]; then
	source_dir="/home/love"
else
	source_dir="$2"
fi
echo "${target_dir}"
echo "${source_dir}"
cd "${target_dir}"
for file1 in `ls -a`;
do
	diff_cmd="${DIFF_COMMAND} ${target_dir}/${file1}  ${source_dir}/${file1} > /dev/null 2>&1"
	###diff_cmd="diff ${target_dir}/${file1}  ${source_dir}/${file1}"
	echo ${diff_cmd}
	diff_resu=`${diff_cmd}`
	if [ $? -eq 0 ]; then
		global_result_equl="${global_result_equl} $file1 "
		echo "equl:" $file1;
	else
		global_result_notequl="${global_result_notequl} $file1 "
		echo "not equl:" $file1;
	fi
done
if [ -n "${global_result_equl}" ]; then
	echo "equl(s):" ${global_result_equl}
fi
if [ -n "${global_result_notequl}" ]; then
	echo "Not equl(s):" ${global_result_notequl}
fi
