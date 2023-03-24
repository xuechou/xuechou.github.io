# 解决抢不到licence，导致编译失败的问题

## 1st version

**思路**：还是利用python标准库的`subprocess`模块，和[此前一篇](./repetDo.md)的区别是：本篇是在win10下执行powershell的命令，和此前略有不同。

```py
import os
import sys
import time
import subprocess

makefilePath = r'your_project_path'  # Debug directory that contains makefile

# cd to makefile path
os.chdir(makefilePath)
print('\n\tCurrent Path:{}\n'.format(os.getcwd()))
startTime = time.time()

# call make utility to build project
cmd = r"& 'C:\Program Files (x86)\TASKING\TriCore v6.2r2\ctc\bin\amk.exe' -j20 all"

while True:
    result = subprocess.run(
        ["powershell", "-Command", cmd], capture_output=True)
    if result.returncode != 0:
        print(result.stderr)
    else:
        print("\n\tSuccessful build project, which used {} s.\n".format(
            time.time()-startTime))
        sys.exit(0)
```

### 缺点：无法打印编译过程中的error和warnning

只能根据returncode的逻辑值判断编译过程是成功，还是失败。但是失败原因既可能是没有证书，也可能是语法错误。

## 2nd version

**思路**直接在Powershell中调用amk.exe，关键的命令如下：

```powershell
& 'C:\Program Files (x86)\TASKING\TriCore v6.2r2\ctc\bin\amk.exe' -G 'C:\project_path\Debug' -j16 all
# -G : change directory
```

