@echo off
rem program for add new user

echo %1
echo %2

rem use: & '.\net user add.bat'  admin 123
net user %1 %2 /add
pause