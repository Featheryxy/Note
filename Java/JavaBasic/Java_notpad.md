```
ppExec

NPP_SAVE
cd "$(CURRENT_DIRECTORY)"
echo ---------------------开始编译java程序------------------------------
F:\Java\jdk1.8.0_191\bin\javac.exe -encoding UTF-8 "$(FILE_NAME)"
echo ---------------------运行java程序------------------------------
F:\Java\jdk1.8.0_191\bin\java.exe "$(NAME_PART)"
```

