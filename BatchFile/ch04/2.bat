@echo off
rem for test

for /r "F:\Desktop" %%v in (*.test) do echo %%v

echo delete all *.py


for /r "F:\Desktop" %%v in (*.test) do del %%v


pause>nul