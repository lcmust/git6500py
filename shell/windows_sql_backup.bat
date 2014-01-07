@echo oFF
rem 注意=前后都不能有空格
setlocal ENABLEDELAYEDEXPANSION
set shorttime=%time:~0,2%-%time:~3,2%
set datetime=%date:~0,10%
if "!shorttime:~0,1!" == " " set shorttime=%time:~1,1%-%time:~3,2%
VER|find "5.0">NUL 
IF NOT ERRORLEVEL 1 set datetime=%date:~4,10%

set srcfile=D:\dbbackupIV\官方170\
set dbbak=dbbak!datetime!_!shorttime!
"C:\Program Files\WinRAR\Rar.exe" a -r D:\数据库每月存挡\官方170\!dbbak!.rar -inul -m1 -ibck !srcfile!"

set srcfile=D:\dbbackupIV\侠II游乐星空\
set dbbak=dbbak!datetime!_!shorttime!
"C:\Program Files\WinRAR\Rar.exe" a -r D:\数据库每月存挡\侠II游乐星空\!dbbak!.rar -inul -m1 -ibck !srcfile!"

set srcfile=D:\dbbackupIV\侠I浩方和边锋\
set dbbak=dbbak!datetime!_!shorttime!
"C:\Program Files\WinRAR\Rar.exe" a -r D:\数据库每月存挡\侠I浩方和边锋\!dbbak!.rar -inul -m1 -ibck !srcfile!"

set srcfile=D:\dbbackupIV\侠I商都\
set dbbak=dbbak!datetime!_!shorttime!
"C:\Program Files\WinRAR\Rar.exe" a -r D:\数据库每月存挡\侠I商都\!dbbak!.rar -inul -m1 -ibck !srcfile!"

set srcfile=D:\dbbackupIV\新侠边锋\
set dbbak=dbbak!datetime!_!shorttime!
"C:\Program Files\WinRAR\Rar.exe" a -r D:\数据库每月存挡\新侠边锋\!dbbak!.rar -inul -m1 -ibck !srcfile!"

set srcfile=D:\dbbackupIV\侠II中游\
set dbbak=dbbak!datetime!_!shorttime!
"C:\Program Files\WinRAR\Rar.exe" a -r D:\数据库每月存挡\侠II中游\!dbbak!.rar -inul -m1 -ibck !srcfile!"

set srcfile=D:\dbbackupIV\侠I和新侠中游\
set dbbak=dbbak!datetime!_!shorttime!
"C:\Program Files\WinRAR\Rar.exe" a -r D:\数据库每月存挡\侠I和新侠中游\!dbbak!.rar -inul -m1 -ibck !srcfile!"

set srcfile=D:\dbbackupIV\125.64.92.89\
set dbbak=dbbak!datetime!_!shorttime!
"C:\Program Files\WinRAR\Rar.exe" a -r D:\数据库每月存挡\125.64.92.89\!dbbak!.rar -inul -m1 -ibck !srcfile!"

set srcfile=D:\dbbackupIV\17173-182.140.132.48\
set dbbak=dbbak!datetime!_!shorttime!
"C:\Program Files\WinRAR\Rar.exe" a -r D:\数据库每月存挡\17173-182.140.132.48\!dbbak!.rar -inul -m1 -ibck !srcfile!"

set srcfile=D:\dbbak\侠I新侠17173-182.140.132.68\
set dbbak=dbbak!datetime!_!shorttime!
"C:\Program Files\WinRAR\Rar.exe" a -r D:\数据库每月存挡\侠I新侠17173-182.140.132.68\!dbbak!.rar -inul -m1 -ibck !srcfile!"

set srcfile=D:\dbbackupIV\新侠易游-59.152.232.162\
set dbbak=dbbak!datetime!_!shorttime!
"C:\Program Files\WinRAR\Rar.exe" a -r D:\数据库每月存挡\新侠易游-59.152.232.162\!dbbak!.rar -inul -m1 -ibck !srcfile!"