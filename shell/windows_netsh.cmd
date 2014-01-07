@rem filename: windows_netsh.cmd
@rem date: 20130106-1000
@rem author: chengl6500
@rem descript: change ip address mask gateway
@rem other: 文件编码不能用UTF-8格式
@rem 以@rem或者:开始的是注释语句（不会执行）
@rem 以:开始的也是注释语句（不会执行）
: (netsh interface ip  set address eth0  static 192.168.1.219 255.255.255.0 192.168.1.1 14)
@rem Begin
netsh interface ip  set address eth0  static 192.168.1.219 255.255.255.0 192.168.1.1 14
@rem End