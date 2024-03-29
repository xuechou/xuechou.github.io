**参考**

https://wizardforcel.gitbooks.io/100-gdb-tips/content/index.html


# gdb基本使用

step1:启动gdb的两种方法

    方法1) `gdb hello`
    方法2) `gdb`
       `file hello`

step2:设置断点

    在函数入口设置断点: `break main`
    按照行号设置断点：`break hello.c:3`

step3:启动程序并运行到断点 `run` `r`

step4:**查看当前状态**

    查看**程序指针寄存器eip**的值 `i r eip` 表示下一条指令的位置
    查看所有**通用寄存器**的值 `i r` 或者全拼`info register`

通过地址，查看**内存单元**  `x命令`

	`x/8xb 0x4011b2`从地址0x4011b2开始，显示8个存储单元，16进制显示 ，每个存储单元对应1字节
		|||__一个存储单元对应一个字节
		||__按16进制显示
		|__显示8个内存单元

```sh
(gdb) x/8xb 0x4011b2
0x4011b2 <main+25>:     0x83    0xec    0x0c    0x8d    0x90    0x08    0xe0    0xff
```  

`x/2dw 0x4011b2`从地址0x4011b2开始，显示2个32位的存储单元内容，并以10进制显示

```sh
(gdb) x/2dw 0x4011b2
0x4011b2 <main+25>:     -1928532861     -2094960
```

查看**栈帧**

查看栈帧范围`i r esp ebp`
计算栈帧的总字节数y=ebp-esp+4,z=y/4  
显示当前栈帧

`x/yxb $esp`    #y是上面计算出来的字节数,每字节用16进制打印内存单元
`x/zxw $esp`    #z=y/4，,每32位用16进制打印每个内存单元

step5:继续执行下一条指令或语句

    执行一条机器指令：`si`
    执行一条C语句：`s`

step6: 退出gdb `quit`

## 补充gdb命令

**p命令带自动补全功能**
p everything

**info命令**

- 查看所有全局和静态变量 `info variables`  注意会显示很多
- 查看当前栈帧的局部变量 `info locals`
- 查看当前函数的参数 `info args`


**设置命令行参数**

`set args arg1 arg2`


**查看断点**

`info breakpoints`
