@echo oFF
rem ע��=ǰ�󶼲����пո�
setlocal ENABLEDELAYEDEXPANSION
set shorttime=%time:~0,2%-%time:~3,2%
set datetime=%date:~0,10%
if "!shorttime:~0,1!" == " " set shorttime=%time:~1,1%-%time:~3,2%
VER|find "5.0">NUL 
IF NOT ERRORLEVEL 1 set datetime=%date:~4,10%

set srcfile=D:\dbbackupIV\�ٷ�170\
set dbbak=dbbak!datetime!_!shorttime!
"C:\Program Files\WinRAR\Rar.exe" a -r D:\���ݿ�ÿ�´浲\�ٷ�170\!dbbak!.rar -inul -m1 -ibck !srcfile!"

set srcfile=D:\dbbackupIV\��II�����ǿ�\
set dbbak=dbbak!datetime!_!shorttime!
"C:\Program Files\WinRAR\Rar.exe" a -r D:\���ݿ�ÿ�´浲\��II�����ǿ�\!dbbak!.rar -inul -m1 -ibck !srcfile!"

set srcfile=D:\dbbackupIV\��I�Ʒ��ͱ߷�\
set dbbak=dbbak!datetime!_!shorttime!
"C:\Program Files\WinRAR\Rar.exe" a -r D:\���ݿ�ÿ�´浲\��I�Ʒ��ͱ߷�\!dbbak!.rar -inul -m1 -ibck !srcfile!"

set srcfile=D:\dbbackupIV\��I�̶�\
set dbbak=dbbak!datetime!_!shorttime!
"C:\Program Files\WinRAR\Rar.exe" a -r D:\���ݿ�ÿ�´浲\��I�̶�\!dbbak!.rar -inul -m1 -ibck !srcfile!"

set srcfile=D:\dbbackupIV\�����߷�\
set dbbak=dbbak!datetime!_!shorttime!
"C:\Program Files\WinRAR\Rar.exe" a -r D:\���ݿ�ÿ�´浲\�����߷�\!dbbak!.rar -inul -m1 -ibck !srcfile!"

set srcfile=D:\dbbackupIV\��II����\
set dbbak=dbbak!datetime!_!shorttime!
"C:\Program Files\WinRAR\Rar.exe" a -r D:\���ݿ�ÿ�´浲\��II����\!dbbak!.rar -inul -m1 -ibck !srcfile!"

set srcfile=D:\dbbackupIV\��I����������\
set dbbak=dbbak!datetime!_!shorttime!
"C:\Program Files\WinRAR\Rar.exe" a -r D:\���ݿ�ÿ�´浲\��I����������\!dbbak!.rar -inul -m1 -ibck !srcfile!"

set srcfile=D:\dbbackupIV\125.64.92.89\
set dbbak=dbbak!datetime!_!shorttime!
"C:\Program Files\WinRAR\Rar.exe" a -r D:\���ݿ�ÿ�´浲\125.64.92.89\!dbbak!.rar -inul -m1 -ibck !srcfile!"

set srcfile=D:\dbbackupIV\17173-182.140.132.48\
set dbbak=dbbak!datetime!_!shorttime!
"C:\Program Files\WinRAR\Rar.exe" a -r D:\���ݿ�ÿ�´浲\17173-182.140.132.48\!dbbak!.rar -inul -m1 -ibck !srcfile!"

set srcfile=D:\dbbak\��I����17173-182.140.132.68\
set dbbak=dbbak!datetime!_!shorttime!
"C:\Program Files\WinRAR\Rar.exe" a -r D:\���ݿ�ÿ�´浲\��I����17173-182.140.132.68\!dbbak!.rar -inul -m1 -ibck !srcfile!"

set srcfile=D:\dbbackupIV\��������-59.152.232.162\
set dbbak=dbbak!datetime!_!shorttime!
"C:\Program Files\WinRAR\Rar.exe" a -r D:\���ݿ�ÿ�´浲\��������-59.152.232.162\!dbbak!.rar -inul -m1 -ibck !srcfile!"