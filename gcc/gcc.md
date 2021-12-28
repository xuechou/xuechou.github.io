# gcc

## 最简单用法

gcc hello.c -o hello

## gcc分步骤使用

gcc -E hello.c -o hello.i   #预处理

    gcc -S hello.i -o hello.s   #编译

        gcc -c hello.s -o hello.o #汇编

            gcc hello.o -o hello    #链接


## 常用的选项

TODO:
- 添加头文件 -i
- 添加源文件
- 指定链接顺序
- 生成32位版本 -m32
- 带调式信息 -g
- 生产静态库
- 生产动态库



# gcc中处理目标文件的工具

**目标文件的三种：**

- 可重定位目标文件；
- 可执行目标文件；
- 共享目标文件；


example c code

```c
#include <stdio.h>

int main(int argc, char const *argv[])
{
	printf("Hello World!\n");
	return 0;
}
```

