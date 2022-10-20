@echo off

echo 1.a
echo 2.b
echo 3.c
echo 4.d

:first
echo Enter you option:
rem 设置变量，使用opt接受用户的输入
set /p opt=
if %opt%==1 goto one
if %opt%==2 goto two
if %opt%==3 goto three
if %opt%==4 goto four
echo Invalid option
goto first

:one
echo your choose one
pause>nul
exit


:two
echo your choose teo
pause>nul
exit

:three
echo your choose three
pause>nul
exit

:four
echo your choose four
pause>nul
exit