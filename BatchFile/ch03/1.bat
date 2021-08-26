@echo off
rem 演示if-else 结构 判断字符串是否为规定的字符串

rem v == hello wrong,不能有空格
set v=hello 

if %v%==hello (echo ok) else (echo no)

pause>nul