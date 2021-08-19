# gcc

## gcc直接生成可执行文件，最简单用法

gcc hello.c -o hello

## gcc分步骤使用

gcc -E hello.c -o hello.i   #预处理

    gcc -S hello.i -o hello.s   #编译

        gcc -c hello.s -o hello.o #汇编

            gcc hello.o -o hello    #链接


## 常用的选项

TODO:
- 添加头文件
- 添加源文件
- 指定链接顺序
- 生成32位版本
- 带调式信息
- 生产静态库
- 生产动态库


# objdump

ojbdump将`重定位文件`与`可执行文件`反汇编得到汇编代码。重定位文件的起始地址从0开始，但可执行文件不是。

**用法**:  -S选项 添加C代码作为对照 

`objdump -S hello.o > hello.s`  #反汇编**重定位**文件

`objdump -S hello > hello.s`    #反汇编**可执行**文件

`objdump -d hello > hello.s`    #也可以利用-d选项

