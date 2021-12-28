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

# 目标文件的全部内容有哪些？

## 重定位目标文件的内容

## 可执行文件的内容

## 符号表

# gcc中处理目标文件的工具

**目标文件的三种：**

- 可重定位目标文件；
- 可执行目标文件；
- 共享目标文件；

? 默认下列的二进制工具支持上述三种目标文件

example c code

```c
#include <stdio.h>

int main(int argc, char const *argv[])
{
	printf("Hello World!\n");
	return 0;
}
```


## ar

> 创建静态库，插入，删除，列出和提取成员。—— CSAPP


## strip

> 从目标文件中删除符号表信息。

<details>
  <summary>展开代码</summary>
  <pre><code>

```bash
t@DESKTOP-NVJJKJO:~/githubCode/xuechou.github.io$ strip helloWorld
t@DESKTOP-NVJJKJO:~/githubCode/xuechou.github.io$ objdump -t helloWorld

helloWorld:     file format elf64-x86-64

SYMBOL TABLE:
no symbols


t@DESKTOP-NVJJKJO:~/githubCode/xuechou.github.io$
```

  </code></pre>
</details>

## ldd

> 列出可执行文件在运行时所需的共享库。

<details>
  <summary>展开代码</summary>
  <pre><code>
  
```bash
t@DESKTOP-NVJJKJO:~/githubCode/xuechou.github.io$ ldd helloWorld
        linux-vdso.so.1 (0x00007fffc1513000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f986cc40000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f986ce56000)
t@DESKTOP-NVJJKJO:~/githubCode/xuechou.github.io$
```

  </code></pre>
</details>