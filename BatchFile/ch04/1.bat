@echo off
rem for test

for /d %%a in (F:\Desktop\*) do if %%a==test rd %%a

for /d %%a in (F:\Desktop\*) do echo %%a

pause>nul