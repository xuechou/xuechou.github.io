## 参考gitlab的目录结构

https://about.gitlab.com/images/press/git-cheat-sheet.pdf

## 5个位置

`Stash` <-->  `Workspace` <--> `Index` <--> `Local Repository` <--> `Upstream Repository`

## 01 安装git后的第一次配置

**using ssh**

修改当前仓库的config文件中的url

```
#url = https://github.com/xuechou/interpreter.git
url = git@github.com:xuechou/interpreter.git
```

## 02 新建或者克隆git仓库

**递归克隆仓库，针对包含sub-module的仓库**

- git clone --recurse-submodules *url*


## 03 日常工作,使用的最多

**检查已修改内容**

- git status

**撤销所有修改，回到HEAD版本,并且删除untracked file,此方法可以保证workspace clean**

- git reset --hard HEAD
- git clean -df -x ./

**新增提交**

- git add *
- git commit -m "balabala"

**删除提交中的某个文件**

- git restore --staged *someFile*

**追加提交,或者修改当前提交的Log**

- git commit --amend

## 04 分支模型

**列出所有分支**

- git branch -a

## 05 查看日志

`git log -1` 查看最近1次的提交记录

`git log -1 --name-status` 显示最近提交的文件变更列表

`git log --author=xxx` 只查看某个人的提交

## 08 仓库间的同步

**建议push之前，先进行rebase操作，避免push失败**

- git fetch
- git rebase
- 解决合并中*冲突的文件*
- git add  *冲突的文件*
- git rebase --continue

- `git push origin master:master`

## 10 添加子模块——submudule

**在已有的仓库中添加子模块**，初始化配置仓库，只用一次

- git submodule add *url*

**克隆包含子模块的仓库**

- git clone --recurse-submodules *url* *set_path_for_summodule*

**更新仓库中的子模块的步骤**

- git submodule update --remote   `拉取子模块的更新到本地仓库，还需要提交一次才能在远程仓库生效`
- git status; git add *; git commit -m "xx"; git push;

**保持workspace clean，包括子模块**

```
git clean -xfd
git submodule foreach --recursive git clean -xfd
git reset --hard
git submodule foreach --recursive git reset --hard
git submodule update --init --recursive
```

## FAQ