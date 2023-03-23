# 解决抢不到licence，导致编译失败的问题

**思路**：还是利用标准库的`subprocess`模块，和[此前一篇](./repetDo.md)的区别是：本篇是在win10下执行powershell的命令，和此前略有不同。

```py
import os
import sys
import time
import subprocess

makefilePath = r'your_project_path'  # TODO:

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

## 缺点：无法打印编译过程中的error和warnning

原因是amk.exe自身不支持打印编译中的错误信息，并不是subprocess.run()的问题。
