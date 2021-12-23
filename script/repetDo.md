# 重复执行某个命令，直到成功

要解决的问题是：github仓库的代码克隆经常失败，需要重复多次才能成功；

## 第一版

使用标准库的`subprocess`模块

```py
#! /usr/bin/python3
import subprocess

# cmd shall be a list
cmd = ['git', 'clone','https://github.com/bao-project/freertos-over-bao']

while True:
    result = subprocess.run(cmd)
    
    if result.returncode == 0:
        break
```

## 第二版——避免硬编码

```py
#! /usr/bin/python3
import sys
import subprocess
assert len(sys.argv) > 1, "Empty command!"

cmd = sys.argv  # Do not sys.argv.pop()!
cmd.pop(0)  # Remove script's name
print('command: ', cmd)

success = 0
while subprocess.run(cmd).returncode != success:
    pass
```

- 调用：`./script_name git clone url`

## 第三版——加入命令行参数的解析

todo