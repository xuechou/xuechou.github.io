
**撤销所有修改，回到HEAD版本**

git reset --hard HEAD


**撤销所有修改，回到HEAD版本,并且删除untracked file,此方法可以保证workspace clean**

git reset --hard HEAD
git clean -df -x ./


**检查已经修改内容**

git status


**列出所有分支**

git branch -a


**查看日志**

git log


**新增提交**

git add *
git commit -m "bala"


**追加提交,或者修改当前提交的Log**

git commit --amend

**push to github** 

git push origin master:master


**using ssh**

修改当前仓库的config文件中的url,eg

```
#url = https://github.com/xuechou/interpreter.git
url = git@github.com:xuechou/interpreter.git
```
