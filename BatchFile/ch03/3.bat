@echo off
if exist F:\Desktop\a.txt (
	echo file is find!
	del F:\Desktop\a.txt
) else (
	echo file is not find
)
pause>nul