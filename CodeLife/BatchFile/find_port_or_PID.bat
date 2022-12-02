@echo off
echo Please enter the port id or PID which you want to find?
set /p portId=portId: 
echo %portId%
if %portId%=="" goto

netstat -ano | findstr %portId%

echo Please enter the PID which you want to find?
set /p PID=PID: 
tasklist|findstr %PID%

echo Which task do you want to kill? Please enter the PID;
set /p PID=PID: 
if %PID%=="" goto
taskkill /T /F /PID %PID% 
pause
