@rem filename: windows_netsh.cmd
@rem date: 20130106-1000
@rem author: chengl6500
@rem descript: change ip address mask gateway
@rem other: �ļ����벻����UTF-8��ʽ
@rem ��@rem����:��ʼ����ע����䣨����ִ�У�
@rem ��:��ʼ��Ҳ��ע����䣨����ִ�У�
: (netsh interface ip  set address eth0  static 192.168.1.219 255.255.255.0 192.168.1.1 14)
@rem Begin
netsh interface ip  set address eth0  static 192.168.1.219 255.255.255.0 192.168.1.1 14
@rem End