#!/bin/bash
# cmd: sudo this_file.sh
#
back_home=" .themes/ .tmux.conf .tmuxp/ .gitconfig .emacs .emacs_custom.el .emacs.bmk .hgrc .chengl6500.rc .rules_arptables.txt .rules_iptables.txt .vimrc .bashrc .zshrc .irssi .xinitrc .remmina/ .ssh/ .config/xfce4/ .config/Terminal/ .gnupg/"
back_sys="fstab profile profile_golang.sh profile_jdk7u2.sh rc.local sudoers auto.misc auto.master xdg/ samba/ iet/ NetworkManager/ apt/ default/"
bak_dir_home="/mnt/sda2h/tools/git1/git_config.bak/home_user/"
bak_dir_sys="/mnt/sda2h/tools/git1/git_config.bak/sys_etc/"
### bak_dir_home="/tmp/test/home"
### bak_dir_sys="/tmp/test/sys"
###ready bak_dir
if [ ! -d ${bak_dir_home} ]; then
    mkdir ${bak_dir_home}
fi

if [ ! -d ${bak_dir_sys} ]; then
    mkdir ${bak_dir_sys}
fi
###
###backup home
for files in ${back_home}
do
    if [ -f  /home/love/${files} ]; then
        cp /home/love/${files} ${bak_dir_home}
    elif [ -d /home/love/${files} ]; then
	cp -r /home/love/${files} ${bak_dir_home}
    fi
done
###
###backup sys
for files in ${back_sys}
do
    if [ -f  /etc/${files} ]; then
        cp /etc/${files} ${bak_dir_sys}
    elif [ -d /etc/${files} ]; then
	cp -r /etc/${files} ${bak_dir_sys}
    fi
done
###
sudo chown -R love.love $bak_dir_home
sudo chown -R love.root $bak_dir_sys
