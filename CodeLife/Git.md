---
title: Git常用操作总结
date: 2019-11-20 18:34:34
tags: Git
---

​		Git是目前世界上最先进的**分布式版本控制系统**

<!-- more -->

## 1. Introduction

- Git是目前世界上最先进的**分布式版本控制系统**
- Git**管理**的是**修改**
- 工作区(working tree)
- ---add---> 
- 暂存区(stage)
- ---commit---> 
- 本地仓库(local repository) 
- ---push---> 
- 远程仓库(remote repository)

## 2. Basic Setting

### 2.1 账户设置

```
$ git config --global user.name "Your Name"
$ git config --global user.email "email@example.com"
```

全局配置文件通常在C:\Users\Administrator\\ .gitconfig。想更改这些信息时，可以直接编辑这个设置文件 

```
[user]
    name = Firstname Lastname
    email = your_email@example.com	
```

### 2.2 提高可读性 

```
$ git config --global color.ui auto
```

"~/.gitconfig”中会增加下面一行。

```
[color]
	ui = auto
```

### 2.3 ssh认证

用于认证客户端真实性

#### 2.3.1 创建SSH Key

```
ssh-keygen -t rsa -C "your_email@example.com"
```

#### 2.3.2 填写id_rsa

登陆GitHub，打开“Account settings”，“SSH Keys”页面，填写id_rsa.pub

#### 2.3.3 是否认证成功

```
ssh -T git@github.com
```

## 3. Local Repository

```
git init
# 生成.git文件。  .git目录里的内容称为“附属于该仓库的工作树”
```

## 4. Working Tree to Stage

```
git add readme.txt licence.txt
```

## 5. Stage to Repository

```
git commit -m 'wrote a readme file'
# 一次性将stage中的所有文件修改提交到本地仓库中
```

## 6. Status

```
git status
```

## 7. Different

```
git diff # 查看工作树和暂存区的差别
“+”号标出的是新添加的行
“-”号标出的是被删除的行

git diff HEAD # 查看暂存区和版本库的差别， HEAD 是指向当前分支中最新一次提交的指针
```

在执行 git commit命令之前先执行git diff HEAD命令，查看本次提交与上次提交之间有什么差别 

## 8. Commit Log

```
git log # 只能查看以当前状态为终点的历史日志
git log --pretty=oneline # 只显示提交信息的第一行
git log README.md # 只显示指定目录、文件的日志

git commit --amend  # 修改提交信息
```

## 9. Version Rollback

要让仓库的 HEAD、暂存区、当前工作树回溯到指定状态 

```
git reset --hard HEAD^  # 回退到上一个版本
git reset --hard HEAD^^  # 回退到上上个版本
git reset --hard HEAD~100  # 回退到上100个版本

git reset --hard hash_code  # hash_code 只取前几位数就好
# 暂存区的修改撤销掉（unstage），重新放回工作区
git reset HEAD <file>
```

## 10. Reflog

```
git reflog
```

## 11. Undo

### 11.1 场景1

当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令

​	`git checkout -- file`

### 11.2场景2
当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步
​	`git reset HEAD <file>`，就回到了场景1，
​	第二步按场景1操作。`git checkout -- file` 

### 11.3场景3
已经提交了不合适的修改到版本库时，想要撤销本次提交，参考版本回退一节，不过前提是没有推送到远程库

## 12. Remove

### 12.1 删除版本库中的文件

```
1. git rm <file>
2. git commit -m 'remove' 
```

### 12.2 恢复删除的文件

```git
git checkout -- <file>
```

## 13. Tag

为版本库打上标签代替commit id, 标签都只存储在本地，不会自动推送到远程。所以，打错的标签可以在本地安全删除

```
git tag  可以查看所有标签

1. 为当前版本库打上标签
   `git tag v1.0`

2. 为历史版本库打上标签
   `git tag v0.9 <commit id>`

3. 查看标签信息
   `git show <tagname>`

4. 创建带有说明的标签，用-a指定标签名，-m指定说明文字
   `git tag -a v0.1 -m "version 0.1 released" 1094adb`

5. 删除标签
   `git tag -d v0.1`

6. 将标签推送到远程
   `git push origin v1.0`

7. 一次性推送全部尚未推送到远程的本地标签
   `git push origin --tags`

8. 删除远程标签
   先从本地删除
   `git tag -d v0.9`

然后，从远程删除。删除命令也是push，但是格式如下：
`git push origin :refs/tags/v0.9`
```

## 14. Branch

```
git branch # 显示分支一览表 

# git checkout -- 创建、切换分支 
git checkout -b feature-A # 切换到 feature-A 分支并进行提交 
----等同于下面两条命令----
git branch feature-A  # 创建feature-A 分支
git checkout feature-A  # 切换到 feature-A 分支

git checkout master  # 切换到 master 分支
git checkout -  # 切换至上一个分支

git merge --no-ff feature-A  # 合并分支

git log --graph  # 以图表形式查看分支

git branch -a命令查看当前分支的相关信息。添加 -a 参数可以同时显示本地仓库和远程仓库的分支信息。
```

特性（ Topic）分支 : 集中实现单一特性（主题），除此之外不进行任何作业的分支。 在日常开发中，往往会创建数个特性分支，同时在此之外再保留一个随时可以发布软件的稳定分支。稳定分支的角色通常由 master 分支担当 

主干分支 : 主干分支是刚才我们讲解的特性分支的原点，同时也是合并的终点。

## 15. Ignore

- 编写`.gitignore`文件，将想要忽略的文件填写在`.gitignore`文件中，将该文件提交到版本库中
- 强制将忽略的文件提交到版本库中
  `git add -f App.class`

## 16. Origin

remote repository 

### 16.1 Create

点击 New Repository

- Initialize this repository with a README  
- 勾选：直接可以clone到本地
- 不勾选：用于push已有的本地仓库

### 16.2 Clone 

```
git clone git@github.com:MiloYxy/Hello-World.git
```

### 16.3. Push

```
git remote add origin https://github.com/MiloYxy/learngit.git
# 加上了-u参数，-u参数可以在推送的同时，将 origin 仓库的 master 分支设置为本地仓库当前分支的
# upstream（上游） ，在以后的推送或者拉取时就可以简化命令

git push -u origin master`
```

### 16.4 同时删除remote repository 和local repository 中的文件

```
# 进入本地文件夹中相应的文件夹，删除需要删除的文件/文件夹
git add * 
git commit -m 'delete file'
git push origin master
```

### 16.5 只删除远程仓库的文件，不删除本地仓库

```
git pull origin master  # 将项目从远程库拉下来
git rm -r --cached 1.txt  # 删除指定文件，多个文件之间空格隔开
git commit -m '删除1.txt'
git push -u origin master
```





 