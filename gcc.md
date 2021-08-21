- [gcc](#gcc)
	- [最简单用法](#最简单用法)
	- [gcc分步骤使用](#gcc分步骤使用)
	- [常用的选项](#常用的选项)
- [目标文件的全部内容有哪些？](#目标文件的全部内容有哪些)
	- [重定位目标文件的内容](#重定位目标文件的内容)
	- [可执行文件的内容](#可执行文件的内容)
	- [符号表](#符号表)
- [gcc中处理目标文件的工具](#gcc中处理目标文件的工具)
	- [objdump](#objdump)
		- [反汇编](#反汇编)
		- [打印符号表](#打印符号表)
	- [readelf](#readelf)
	- [ar](#ar)
	- [strings](#strings)
	- [strip](#strip)
	- [ldd](#ldd)

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
## objdump 

> 所有二进制工具之母，能够显示目标文件的所有信息。最大作用是反汇编.text节的二进制指令。—— CSAPP

### 反汇编

ojbdump将`重定位文件`与`可执行文件`反汇编得到汇编代码。重定位文件的起始地址从0开始，但可执行文件不是。

**-d选项 反汇编**

`objdump -d hello > hello.s`    #也可以利用-d选项 --disassemble

```bash
t@DESKTOP-NVJJKJO:~/githubCode/xuechou.github.io$ objdump -d helloWorld

helloWorld:     file format elf64-x86-64


Disassembly of section .init:

0000000000001000 <_init>:
    1000:       f3 0f 1e fa             endbr64
    1004:       48 83 ec 08             sub    $0x8,%rsp
    1008:       48 8b 05 d9 2f 00 00    mov    0x2fd9(%rip),%rax        # 3fe8 <__gmon_start__>
    100f:       48 85 c0                test   %rax,%rax
    1012:       74 02                   je     1016 <_init+0x16>
    1014:       ff d0                   callq  *%rax
    1016:       48 83 c4 08             add    $0x8,%rsp
    101a:       c3                      retq

Disassembly of section .plt:

0000000000001020 <.plt>:
    1020:       ff 35 9a 2f 00 00       pushq  0x2f9a(%rip)        # 3fc0 <_GLOBAL_OFFSET_TABLE_+0x8>
    1026:       f2 ff 25 9b 2f 00 00    bnd jmpq *0x2f9b(%rip)        # 3fc8 <_GLOBAL_OFFSET_TABLE_+0x10>
    102d:       0f 1f 00                nopl   (%rax)
    1030:       f3 0f 1e fa             endbr64
    1034:       68 00 00 00 00          pushq  $0x0
    1039:       f2 e9 e1 ff ff ff       bnd jmpq 1020 <.plt>
    103f:       90                      nop

Disassembly of section .plt.got:

0000000000001040 <__cxa_finalize@plt>:
    1040:       f3 0f 1e fa             endbr64
    1044:       f2 ff 25 ad 2f 00 00    bnd jmpq *0x2fad(%rip)        # 3ff8 <__cxa_finalize@GLIBC_2.2.5>
    104b:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

Disassembly of section .plt.sec:

0000000000001050 <puts@plt>:
    1050:       f3 0f 1e fa             endbr64
    1054:       f2 ff 25 75 2f 00 00    bnd jmpq *0x2f75(%rip)        # 3fd0 <puts@GLIBC_2.2.5>
    105b:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

Disassembly of section .text:

0000000000001060 <_start>:
    1060:       f3 0f 1e fa             endbr64
    1064:       31 ed                   xor    %ebp,%ebp
    1066:       49 89 d1                mov    %rdx,%r9
    1069:       5e                      pop    %rsi
    106a:       48 89 e2                mov    %rsp,%rdx
    106d:       48 83 e4 f0             and    $0xfffffffffffffff0,%rsp
    1071:       50                      push   %rax
    1072:       54                      push   %rsp
    1073:       4c 8d 05 66 01 00 00    lea    0x166(%rip),%r8        # 11e0 <__libc_csu_fini>
    107a:       48 8d 0d ef 00 00 00    lea    0xef(%rip),%rcx        # 1170 <__libc_csu_init>
    1081:       48 8d 3d c1 00 00 00    lea    0xc1(%rip),%rdi        # 1149 <main>
    1088:       ff 15 52 2f 00 00       callq  *0x2f52(%rip)        # 3fe0 <__libc_start_main@GLIBC_2.2.5>
    108e:       f4                      hlt
    108f:       90                      nop

0000000000001090 <deregister_tm_clones>:
    1090:       48 8d 3d 79 2f 00 00    lea    0x2f79(%rip),%rdi        # 4010 <__TMC_END__>
    1097:       48 8d 05 72 2f 00 00    lea    0x2f72(%rip),%rax        # 4010 <__TMC_END__>
    109e:       48 39 f8                cmp    %rdi,%rax
    10a1:       74 15                   je     10b8 <deregister_tm_clones+0x28>
    10a3:       48 8b 05 2e 2f 00 00    mov    0x2f2e(%rip),%rax        # 3fd8 <_ITM_deregisterTMCloneTable>
    10aa:       48 85 c0                test   %rax,%rax
    10ad:       74 09                   je     10b8 <deregister_tm_clones+0x28>
    10af:       ff e0                   jmpq   *%rax
    10b1:       0f 1f 80 00 00 00 00    nopl   0x0(%rax)
    10b8:       c3                      retq
    10b9:       0f 1f 80 00 00 00 00    nopl   0x0(%rax)

00000000000010c0 <register_tm_clones>:
    10c0:       48 8d 3d 49 2f 00 00    lea    0x2f49(%rip),%rdi        # 4010 <__TMC_END__>
    10c7:       48 8d 35 42 2f 00 00    lea    0x2f42(%rip),%rsi        # 4010 <__TMC_END__>
    10ce:       48 29 fe                sub    %rdi,%rsi
    10d1:       48 89 f0                mov    %rsi,%rax
    10d4:       48 c1 ee 3f             shr    $0x3f,%rsi
    10d8:       48 c1 f8 03             sar    $0x3,%rax
    10dc:       48 01 c6                add    %rax,%rsi
    10df:       48 d1 fe                sar    %rsi
    10e2:       74 14                   je     10f8 <register_tm_clones+0x38>
    10e4:       48 8b 05 05 2f 00 00    mov    0x2f05(%rip),%rax        # 3ff0 <_ITM_registerTMCloneTable>
    10eb:       48 85 c0                test   %rax,%rax
    10ee:       74 08                   je     10f8 <register_tm_clones+0x38>
    10f0:       ff e0                   jmpq   *%rax
    10f2:       66 0f 1f 44 00 00       nopw   0x0(%rax,%rax,1)
    10f8:       c3                      retq
    10f9:       0f 1f 80 00 00 00 00    nopl   0x0(%rax)

0000000000001100 <__do_global_dtors_aux>:
    1100:       f3 0f 1e fa             endbr64
    1104:       80 3d 05 2f 00 00 00    cmpb   $0x0,0x2f05(%rip)        # 4010 <__TMC_END__>
    110b:       75 2b                   jne    1138 <__do_global_dtors_aux+0x38>
    110d:       55                      push   %rbp
    110e:       48 83 3d e2 2e 00 00    cmpq   $0x0,0x2ee2(%rip)        # 3ff8 <__cxa_finalize@GLIBC_2.2.5>
    1115:       00
    1116:       48 89 e5                mov    %rsp,%rbp
    1119:       74 0c                   je     1127 <__do_global_dtors_aux+0x27>
    111b:       48 8b 3d e6 2e 00 00    mov    0x2ee6(%rip),%rdi        # 4008 <__dso_handle>
    1122:       e8 19 ff ff ff          callq  1040 <__cxa_finalize@plt>
    1127:       e8 64 ff ff ff          callq  1090 <deregister_tm_clones>
    112c:       c6 05 dd 2e 00 00 01    movb   $0x1,0x2edd(%rip)        # 4010 <__TMC_END__>
    1133:       5d                      pop    %rbp
    1134:       c3                      retq
    1135:       0f 1f 00                nopl   (%rax)
    1138:       c3                      retq
    1139:       0f 1f 80 00 00 00 00    nopl   0x0(%rax)

0000000000001140 <frame_dummy>:
    1140:       f3 0f 1e fa             endbr64
    1144:       e9 77 ff ff ff          jmpq   10c0 <register_tm_clones>

0000000000001149 <main>:
    1149:       f3 0f 1e fa             endbr64
    114d:       55                      push   %rbp
    114e:       48 89 e5                mov    %rsp,%rbp
    1151:       48 83 ec 10             sub    $0x10,%rsp
    1155:       89 7d fc                mov    %edi,-0x4(%rbp)
    1158:       48 89 75 f0             mov    %rsi,-0x10(%rbp)
    115c:       48 8d 3d a1 0e 00 00    lea    0xea1(%rip),%rdi        # 2004 <_IO_stdin_used+0x4>
    1163:       e8 e8 fe ff ff          callq  1050 <puts@plt>
    1168:       b8 00 00 00 00          mov    $0x0,%eax
    116d:       c9                      leaveq
    116e:       c3                      retq
    116f:       90                      nop

0000000000001170 <__libc_csu_init>:
    1170:       f3 0f 1e fa             endbr64
    1174:       41 57                   push   %r15
    1176:       4c 8d 3d 3b 2c 00 00    lea    0x2c3b(%rip),%r15        # 3db8 <__frame_dummy_init_array_entry>
    117d:       41 56                   push   %r14
    117f:       49 89 d6                mov    %rdx,%r14
    1182:       41 55                   push   %r13
    1184:       49 89 f5                mov    %rsi,%r13
    1187:       41 54                   push   %r12
    1189:       41 89 fc                mov    %edi,%r12d
    118c:       55                      push   %rbp
    118d:       48 8d 2d 2c 2c 00 00    lea    0x2c2c(%rip),%rbp        # 3dc0 <__do_global_dtors_aux_fini_array_entry>
    1194:       53                      push   %rbx
    1195:       4c 29 fd                sub    %r15,%rbp
    1198:       48 83 ec 08             sub    $0x8,%rsp
    119c:       e8 5f fe ff ff          callq  1000 <_init>
    11a1:       48 c1 fd 03             sar    $0x3,%rbp
    11a5:       74 1f                   je     11c6 <__libc_csu_init+0x56>
    11a7:       31 db                   xor    %ebx,%ebx
    11a9:       0f 1f 80 00 00 00 00    nopl   0x0(%rax)
    11b0:       4c 89 f2                mov    %r14,%rdx
    11b3:       4c 89 ee                mov    %r13,%rsi
    11b6:       44 89 e7                mov    %r12d,%edi
    11b9:       41 ff 14 df             callq  *(%r15,%rbx,8)
    11bd:       48 83 c3 01             add    $0x1,%rbx
    11c1:       48 39 dd                cmp    %rbx,%rbp
    11c4:       75 ea                   jne    11b0 <__libc_csu_init+0x40>
    11c6:       48 83 c4 08             add    $0x8,%rsp
    11ca:       5b                      pop    %rbx
    11cb:       5d                      pop    %rbp
    11cc:       41 5c                   pop    %r12
    11ce:       41 5d                   pop    %r13
    11d0:       41 5e                   pop    %r14
    11d2:       41 5f                   pop    %r15
    11d4:       c3                      retq
    11d5:       66 66 2e 0f 1f 84 00    data16 nopw %cs:0x0(%rax,%rax,1)
    11dc:       00 00 00 00

00000000000011e0 <__libc_csu_fini>:
    11e0:       f3 0f 1e fa             endbr64
    11e4:       c3                      retq

Disassembly of section .fini:

00000000000011e8 <_fini>:
    11e8:       f3 0f 1e fa             endbr64
    11ec:       48 83 ec 08             sub    $0x8,%rsp
    11f0:       48 83 c4 08             add    $0x8,%rsp
    11f4:       c3                      retq
t@DESKTOP-NVJJKJO:~/githubCode/xuechou.github.io$
```

**-S选项 混合显示C代码和汇编作为对照**

`objdump -S hello.o > hello.s`  #反汇编**重定位**文件

`objdump -S hello > hello.s`    #反汇编**可执行**文件

### 打印符号表

`objdump -t a.out`

```bash
t@DESKTOP-NVJJKJO:~/githubCode/xuechou.github.io$ objdump -t helloWorld

helloWorld:     file format elf64-x86-64

SYMBOL TABLE:
0000000000000318 l    d  .interp        0000000000000000              .interp
0000000000000338 l    d  .note.gnu.property     0000000000000000              .note.gnu.property
0000000000000358 l    d  .note.gnu.build-id     0000000000000000              .note.gnu.build-id
000000000000037c l    d  .note.ABI-tag  0000000000000000              .note.ABI-tag
00000000000003a0 l    d  .gnu.hash      0000000000000000              .gnu.hash
00000000000003c8 l    d  .dynsym        0000000000000000              .dynsym
0000000000000470 l    d  .dynstr        0000000000000000              .dynstr
00000000000004f2 l    d  .gnu.version   0000000000000000              .gnu.version
0000000000000500 l    d  .gnu.version_r 0000000000000000              .gnu.version_r
0000000000000520 l    d  .rela.dyn      0000000000000000              .rela.dyn
00000000000005e0 l    d  .rela.plt      0000000000000000              .rela.plt
0000000000001000 l    d  .init  0000000000000000              .init
0000000000001020 l    d  .plt   0000000000000000              .plt
0000000000001040 l    d  .plt.got       0000000000000000              .plt.got
0000000000001050 l    d  .plt.sec       0000000000000000              .plt.sec
0000000000001060 l    d  .text  0000000000000000              .text
00000000000011e8 l    d  .fini  0000000000000000              .fini
0000000000002000 l    d  .rodata        0000000000000000              .rodata
0000000000002014 l    d  .eh_frame_hdr  0000000000000000              .eh_frame_hdr
0000000000002058 l    d  .eh_frame      0000000000000000              .eh_frame
0000000000003db8 l    d  .init_array    0000000000000000              .init_array
0000000000003dc0 l    d  .fini_array    0000000000000000              .fini_array
0000000000003dc8 l    d  .dynamic       0000000000000000              .dynamic
0000000000003fb8 l    d  .got   0000000000000000              .got
0000000000004000 l    d  .data  0000000000000000              .data
0000000000004010 l    d  .bss   0000000000000000              .bss
0000000000000000 l    d  .comment       0000000000000000              .comment
0000000000000000 l    df *ABS*  0000000000000000              crtstuff.c
0000000000001090 l     F .text  0000000000000000              deregister_tm_clones
00000000000010c0 l     F .text  0000000000000000              register_tm_clones
0000000000001100 l     F .text  0000000000000000              __do_global_dtors_aux
0000000000004010 l     O .bss   0000000000000001              completed.8060
0000000000003dc0 l     O .fini_array    0000000000000000              __do_global_dtors_aux_fini_array_entry
0000000000001140 l     F .text  0000000000000000              frame_dummy
0000000000003db8 l     O .init_array    0000000000000000              __frame_dummy_init_array_entry
0000000000000000 l    df *ABS*  0000000000000000              helloWorld.c
0000000000000000 l    df *ABS*  0000000000000000              crtstuff.c
000000000000215c l     O .eh_frame      0000000000000000              __FRAME_END__
0000000000000000 l    df *ABS*  0000000000000000
0000000000003dc0 l       .init_array    0000000000000000              __init_array_end
0000000000003dc8 l     O .dynamic       0000000000000000              _DYNAMIC
0000000000003db8 l       .init_array    0000000000000000              __init_array_start
0000000000002014 l       .eh_frame_hdr  0000000000000000              __GNU_EH_FRAME_HDR
0000000000003fb8 l     O .got   0000000000000000              _GLOBAL_OFFSET_TABLE_
0000000000001000 l     F .init  0000000000000000              _init
00000000000011e0 g     F .text  0000000000000005              __libc_csu_fini
0000000000000000  w      *UND*  0000000000000000              _ITM_deregisterTMCloneTable
0000000000004000  w      .data  0000000000000000              data_start
0000000000000000       F *UND*  0000000000000000              puts@@GLIBC_2.2.5
0000000000004010 g       .data  0000000000000000              _edata
00000000000011e8 g     F .fini  0000000000000000              .hidden _fini
0000000000000000       F *UND*  0000000000000000              __libc_start_main@@GLIBC_2.2.5
0000000000004000 g       .data  0000000000000000              __data_start
0000000000000000  w      *UND*  0000000000000000              __gmon_start__
0000000000004008 g     O .data  0000000000000000              .hidden __dso_handle
0000000000002000 g     O .rodata        0000000000000004              _IO_stdin_used
0000000000001170 g     F .text  0000000000000065              __libc_csu_init
0000000000004018 g       .bss   0000000000000000              _end
0000000000001060 g     F .text  000000000000002f              _start
0000000000004010 g       .bss   0000000000000000              __bss_start
0000000000001149 g     F .text  0000000000000026              main
0000000000004010 g     O .data  0000000000000000              .hidden __TMC_END__
0000000000000000  w      *UND*  0000000000000000              _ITM_registerTMCloneTable
0000000000000000  w    F *UND*  0000000000000000              __cxa_finalize@@GLIBC_2.2.5


t@DESKTOP-NVJJKJO:~/githubCode/xuechou.github.io$
```

## readelf

> 显示一个目标文件的完整结构，包括ELF头中编码的所有信息。包括SIZE和NM的功能。

```bash
t@DESKTOP-NVJJKJO:~/githubCode/xuechou.github.io$ readelf helloWorld -all
ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00
  Class:                             ELF64
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              DYN (Shared object file)
  Machine:                           Advanced Micro Devices X86-64
  Version:                           0x1
  Entry point address:               0x1060
  Start of program headers:          64 (bytes into file)
  Start of section headers:          14720 (bytes into file)
  Flags:                             0x0
  Size of this header:               64 (bytes)
  Size of program headers:           56 (bytes)
  Number of program headers:         13
  Size of section headers:           64 (bytes)
  Number of section headers:         31
  Section header string table index: 30

Section Headers:
  [Nr] Name              Type             Address           Offset
       Size              EntSize          Flags  Link  Info  Align
  [ 0]                   NULL             0000000000000000  00000000
       0000000000000000  0000000000000000           0     0     0
  [ 1] .interp           PROGBITS         0000000000000318  00000318
       000000000000001c  0000000000000000   A       0     0     1
  [ 2] .note.gnu.propert NOTE             0000000000000338  00000338
       0000000000000020  0000000000000000   A       0     0     8
  [ 3] .note.gnu.build-i NOTE             0000000000000358  00000358
       0000000000000024  0000000000000000   A       0     0     4
  [ 4] .note.ABI-tag     NOTE             000000000000037c  0000037c
       0000000000000020  0000000000000000   A       0     0     4
  [ 5] .gnu.hash         GNU_HASH         00000000000003a0  000003a0
       0000000000000024  0000000000000000   A       6     0     8
  [ 6] .dynsym           DYNSYM           00000000000003c8  000003c8
       00000000000000a8  0000000000000018   A       7     1     8
  [ 7] .dynstr           STRTAB           0000000000000470  00000470
       0000000000000082  0000000000000000   A       0     0     1
  [ 8] .gnu.version      VERSYM           00000000000004f2  000004f2
       000000000000000e  0000000000000002   A       6     0     2
  [ 9] .gnu.version_r    VERNEED          0000000000000500  00000500
       0000000000000020  0000000000000000   A       7     1     8
  [10] .rela.dyn         RELA             0000000000000520  00000520
       00000000000000c0  0000000000000018   A       6     0     8
  [11] .rela.plt         RELA             00000000000005e0  000005e0
       0000000000000018  0000000000000018  AI       6    24     8
  [12] .init             PROGBITS         0000000000001000  00001000
       000000000000001b  0000000000000000  AX       0     0     4
  [13] .plt              PROGBITS         0000000000001020  00001020
       0000000000000020  0000000000000010  AX       0     0     16
  [14] .plt.got          PROGBITS         0000000000001040  00001040
       0000000000000010  0000000000000010  AX       0     0     16
  [15] .plt.sec          PROGBITS         0000000000001050  00001050
       0000000000000010  0000000000000010  AX       0     0     16
  [16] .text             PROGBITS         0000000000001060  00001060
       0000000000000185  0000000000000000  AX       0     0     16
  [17] .fini             PROGBITS         00000000000011e8  000011e8
       000000000000000d  0000000000000000  AX       0     0     4
  [18] .rodata           PROGBITS         0000000000002000  00002000
       0000000000000011  0000000000000000   A       0     0     4
  [19] .eh_frame_hdr     PROGBITS         0000000000002014  00002014
       0000000000000044  0000000000000000   A       0     0     4
  [20] .eh_frame         PROGBITS         0000000000002058  00002058
       0000000000000108  0000000000000000   A       0     0     8
  [21] .init_array       INIT_ARRAY       0000000000003db8  00002db8
       0000000000000008  0000000000000008  WA       0     0     8
  [22] .fini_array       FINI_ARRAY       0000000000003dc0  00002dc0
       0000000000000008  0000000000000008  WA       0     0     8
  [23] .dynamic          DYNAMIC          0000000000003dc8  00002dc8
       00000000000001f0  0000000000000010  WA       7     0     8
  [24] .got              PROGBITS         0000000000003fb8  00002fb8
       0000000000000048  0000000000000008  WA       0     0     8
  [25] .data             PROGBITS         0000000000004000  00003000
       0000000000000010  0000000000000000  WA       0     0     8
  [26] .bss              NOBITS           0000000000004010  00003010
       0000000000000008  0000000000000000  WA       0     0     1
  [27] .comment          PROGBITS         0000000000000000  00003010
       000000000000002a  0000000000000001  MS       0     0     1
  [28] .symtab           SYMTAB           0000000000000000  00003040
       0000000000000618  0000000000000018          29    46     8
  [29] .strtab           STRTAB           0000000000000000  00003658
       0000000000000208  0000000000000000           0     0     1
  [30] .shstrtab         STRTAB           0000000000000000  00003860
       000000000000011a  0000000000000000           0     0     1
Key to Flags:
  W (write), A (alloc), X (execute), M (merge), S (strings), I (info),
  L (link order), O (extra OS processing required), G (group), T (TLS),
  C (compressed), x (unknown), o (OS specific), E (exclude),
  l (large), p (processor specific)

There are no section groups in this file.

Program Headers:
  Type           Offset             VirtAddr           PhysAddr
                 FileSiz            MemSiz              Flags  Align
  PHDR           0x0000000000000040 0x0000000000000040 0x0000000000000040
                 0x00000000000002d8 0x00000000000002d8  R      0x8
  INTERP         0x0000000000000318 0x0000000000000318 0x0000000000000318
                 0x000000000000001c 0x000000000000001c  R      0x1
      [Requesting program interpreter: /lib64/ld-linux-x86-64.so.2]
  LOAD           0x0000000000000000 0x0000000000000000 0x0000000000000000
                 0x00000000000005f8 0x00000000000005f8  R      0x1000
  LOAD           0x0000000000001000 0x0000000000001000 0x0000000000001000
                 0x00000000000001f5 0x00000000000001f5  R E    0x1000
  LOAD           0x0000000000002000 0x0000000000002000 0x0000000000002000
                 0x0000000000000160 0x0000000000000160  R      0x1000
  LOAD           0x0000000000002db8 0x0000000000003db8 0x0000000000003db8
                 0x0000000000000258 0x0000000000000260  RW     0x1000
  DYNAMIC        0x0000000000002dc8 0x0000000000003dc8 0x0000000000003dc8
                 0x00000000000001f0 0x00000000000001f0  RW     0x8
  NOTE           0x0000000000000338 0x0000000000000338 0x0000000000000338
                 0x0000000000000020 0x0000000000000020  R      0x8
  NOTE           0x0000000000000358 0x0000000000000358 0x0000000000000358
                 0x0000000000000044 0x0000000000000044  R      0x4
  GNU_PROPERTY   0x0000000000000338 0x0000000000000338 0x0000000000000338
                 0x0000000000000020 0x0000000000000020  R      0x8
  GNU_EH_FRAME   0x0000000000002014 0x0000000000002014 0x0000000000002014
                 0x0000000000000044 0x0000000000000044  R      0x4
  GNU_STACK      0x0000000000000000 0x0000000000000000 0x0000000000000000
                 0x0000000000000000 0x0000000000000000  RW     0x10
  GNU_RELRO      0x0000000000002db8 0x0000000000003db8 0x0000000000003db8
                 0x0000000000000248 0x0000000000000248  R      0x1

 Section to Segment mapping:
  Segment Sections...
   00
   01     .interp
   02     .interp .note.gnu.property .note.gnu.build-id .note.ABI-tag .gnu.hash .dynsym .dynstr .gnu.version .gnu.version_r .rela.dyn .rela.plt
   03     .init .plt .plt.got .plt.sec .text .fini
   04     .rodata .eh_frame_hdr .eh_frame
   05     .init_array .fini_array .dynamic .got .data .bss
   06     .dynamic
   07     .note.gnu.property
   08     .note.gnu.build-id .note.ABI-tag
   09     .note.gnu.property
   10     .eh_frame_hdr
   11
   12     .init_array .fini_array .dynamic .got

Dynamic section at offset 0x2dc8 contains 27 entries:
  Tag        Type                         Name/Value
 0x0000000000000001 (NEEDED)             Shared library: [libc.so.6]
 0x000000000000000c (INIT)               0x1000
 0x000000000000000d (FINI)               0x11e8
 0x0000000000000019 (INIT_ARRAY)         0x3db8
 0x000000000000001b (INIT_ARRAYSZ)       8 (bytes)
 0x000000000000001a (FINI_ARRAY)         0x3dc0
 0x000000000000001c (FINI_ARRAYSZ)       8 (bytes)
 0x000000006ffffef5 (GNU_HASH)           0x3a0
 0x0000000000000005 (STRTAB)             0x470
 0x0000000000000006 (SYMTAB)             0x3c8
 0x000000000000000a (STRSZ)              130 (bytes)
 0x000000000000000b (SYMENT)             24 (bytes)
 0x0000000000000015 (DEBUG)              0x0
 0x0000000000000003 (PLTGOT)             0x3fb8
 0x0000000000000002 (PLTRELSZ)           24 (bytes)
 0x0000000000000014 (PLTREL)             RELA
 0x0000000000000017 (JMPREL)             0x5e0
 0x0000000000000007 (RELA)               0x520
 0x0000000000000008 (RELASZ)             192 (bytes)
 0x0000000000000009 (RELAENT)            24 (bytes)
 0x000000000000001e (FLAGS)              BIND_NOW
 0x000000006ffffffb (FLAGS_1)            Flags: NOW PIE
 0x000000006ffffffe (VERNEED)            0x500
 0x000000006fffffff (VERNEEDNUM)         1
 0x000000006ffffff0 (VERSYM)             0x4f2
 0x000000006ffffff9 (RELACOUNT)          3
 0x0000000000000000 (NULL)               0x0

Relocation section '.rela.dyn' at offset 0x520 contains 8 entries:
  Offset          Info           Type           Sym. Value    Sym. Name + Addend
000000003db8  000000000008 R_X86_64_RELATIVE                    1140
000000003dc0  000000000008 R_X86_64_RELATIVE                    1100
000000004008  000000000008 R_X86_64_RELATIVE                    4008
000000003fd8  000100000006 R_X86_64_GLOB_DAT 0000000000000000 _ITM_deregisterTMClone + 0
000000003fe0  000300000006 R_X86_64_GLOB_DAT 0000000000000000 __libc_start_main@GLIBC_2.2.5 + 0
000000003fe8  000400000006 R_X86_64_GLOB_DAT 0000000000000000 __gmon_start__ + 0
000000003ff0  000500000006 R_X86_64_GLOB_DAT 0000000000000000 _ITM_registerTMCloneTa + 0
000000003ff8  000600000006 R_X86_64_GLOB_DAT 0000000000000000 __cxa_finalize@GLIBC_2.2.5 + 0

Relocation section '.rela.plt' at offset 0x5e0 contains 1 entry:
  Offset          Info           Type           Sym. Value    Sym. Name + Addend
000000003fd0  000200000007 R_X86_64_JUMP_SLO 0000000000000000 puts@GLIBC_2.2.5 + 0

The decoding of unwind sections for machine type Advanced Micro Devices X86-64 is not currently supported.

Symbol table '.dynsym' contains 7 entries:
   Num:    Value          Size Type    Bind   Vis      Ndx Name
     0: 0000000000000000     0 NOTYPE  LOCAL  DEFAULT  UND
     1: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_deregisterTMCloneTab
     2: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND puts@GLIBC_2.2.5 (2)
     3: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND __libc_start_main@GLIBC_2.2.5 (2)
     4: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND __gmon_start__
     5: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_registerTMCloneTable
     6: 0000000000000000     0 FUNC    WEAK   DEFAULT  UND __cxa_finalize@GLIBC_2.2.5 (2)

Symbol table '.symtab' contains 65 entries:
   Num:    Value          Size Type    Bind   Vis      Ndx Name
     0: 0000000000000000     0 NOTYPE  LOCAL  DEFAULT  UND
     1: 0000000000000318     0 SECTION LOCAL  DEFAULT    1
     2: 0000000000000338     0 SECTION LOCAL  DEFAULT    2
     3: 0000000000000358     0 SECTION LOCAL  DEFAULT    3
     4: 000000000000037c     0 SECTION LOCAL  DEFAULT    4
     5: 00000000000003a0     0 SECTION LOCAL  DEFAULT    5
     6: 00000000000003c8     0 SECTION LOCAL  DEFAULT    6
     7: 0000000000000470     0 SECTION LOCAL  DEFAULT    7
     8: 00000000000004f2     0 SECTION LOCAL  DEFAULT    8
     9: 0000000000000500     0 SECTION LOCAL  DEFAULT    9
    10: 0000000000000520     0 SECTION LOCAL  DEFAULT   10
    11: 00000000000005e0     0 SECTION LOCAL  DEFAULT   11
    12: 0000000000001000     0 SECTION LOCAL  DEFAULT   12
    13: 0000000000001020     0 SECTION LOCAL  DEFAULT   13
    14: 0000000000001040     0 SECTION LOCAL  DEFAULT   14
    15: 0000000000001050     0 SECTION LOCAL  DEFAULT   15
    16: 0000000000001060     0 SECTION LOCAL  DEFAULT   16
    17: 00000000000011e8     0 SECTION LOCAL  DEFAULT   17
    18: 0000000000002000     0 SECTION LOCAL  DEFAULT   18
    19: 0000000000002014     0 SECTION LOCAL  DEFAULT   19
    20: 0000000000002058     0 SECTION LOCAL  DEFAULT   20
    21: 0000000000003db8     0 SECTION LOCAL  DEFAULT   21
    22: 0000000000003dc0     0 SECTION LOCAL  DEFAULT   22
    23: 0000000000003dc8     0 SECTION LOCAL  DEFAULT   23
    24: 0000000000003fb8     0 SECTION LOCAL  DEFAULT   24
    25: 0000000000004000     0 SECTION LOCAL  DEFAULT   25
    26: 0000000000004010     0 SECTION LOCAL  DEFAULT   26
    27: 0000000000000000     0 SECTION LOCAL  DEFAULT   27
    28: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS crtstuff.c
    29: 0000000000001090     0 FUNC    LOCAL  DEFAULT   16 deregister_tm_clones
    30: 00000000000010c0     0 FUNC    LOCAL  DEFAULT   16 register_tm_clones
    31: 0000000000001100     0 FUNC    LOCAL  DEFAULT   16 __do_global_dtors_aux
    32: 0000000000004010     1 OBJECT  LOCAL  DEFAULT   26 completed.8060
    33: 0000000000003dc0     0 OBJECT  LOCAL  DEFAULT   22 __do_global_dtors_aux_fin
    34: 0000000000001140     0 FUNC    LOCAL  DEFAULT   16 frame_dummy
    35: 0000000000003db8     0 OBJECT  LOCAL  DEFAULT   21 __frame_dummy_init_array_
    36: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS helloWorld.c
    37: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS crtstuff.c
    38: 000000000000215c     0 OBJECT  LOCAL  DEFAULT   20 __FRAME_END__
    39: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS
    40: 0000000000003dc0     0 NOTYPE  LOCAL  DEFAULT   21 __init_array_end
    41: 0000000000003dc8     0 OBJECT  LOCAL  DEFAULT   23 _DYNAMIC
    42: 0000000000003db8     0 NOTYPE  LOCAL  DEFAULT   21 __init_array_start
    43: 0000000000002014     0 NOTYPE  LOCAL  DEFAULT   19 __GNU_EH_FRAME_HDR
    44: 0000000000003fb8     0 OBJECT  LOCAL  DEFAULT   24 _GLOBAL_OFFSET_TABLE_
    45: 0000000000001000     0 FUNC    LOCAL  DEFAULT   12 _init
    46: 00000000000011e0     5 FUNC    GLOBAL DEFAULT   16 __libc_csu_fini
    47: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_deregisterTMCloneTab
    48: 0000000000004000     0 NOTYPE  WEAK   DEFAULT   25 data_start
    49: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND puts@@GLIBC_2.2.5
    50: 0000000000004010     0 NOTYPE  GLOBAL DEFAULT   25 _edata
    51: 00000000000011e8     0 FUNC    GLOBAL HIDDEN    17 _fini
    52: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND __libc_start_main@@GLIBC_
    53: 0000000000004000     0 NOTYPE  GLOBAL DEFAULT   25 __data_start
    54: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND __gmon_start__
    55: 0000000000004008     0 OBJECT  GLOBAL HIDDEN    25 __dso_handle
    56: 0000000000002000     4 OBJECT  GLOBAL DEFAULT   18 _IO_stdin_used
    57: 0000000000001170   101 FUNC    GLOBAL DEFAULT   16 __libc_csu_init
    58: 0000000000004018     0 NOTYPE  GLOBAL DEFAULT   26 _end
    59: 0000000000001060    47 FUNC    GLOBAL DEFAULT   16 _start
    60: 0000000000004010     0 NOTYPE  GLOBAL DEFAULT   26 __bss_start
    61: 0000000000001149    38 FUNC    GLOBAL DEFAULT   16 main
    62: 0000000000004010     0 OBJECT  GLOBAL HIDDEN    25 __TMC_END__
    63: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_registerTMCloneTable
    64: 0000000000000000     0 FUNC    WEAK   DEFAULT  UND __cxa_finalize@@GLIBC_2.2

Histogram for `.gnu.hash' bucket list length (total of 2 buckets):
 Length  Number     % of total  Coverage
      0  1          ( 50.0%)
      1  1          ( 50.0%)    100.0%

Version symbols section '.gnu.version' contains 7 entries:
 Addr: 0x00000000000004f2  Offset: 0x0004f2  Link: 6 (.dynsym)
  000:   0 (*local*)       0 (*local*)       2 (GLIBC_2.2.5)   2 (GLIBC_2.2.5)
  004:   0 (*local*)       0 (*local*)       2 (GLIBC_2.2.5)

Version needs section '.gnu.version_r' contains 1 entry:
 Addr: 0x0000000000000500  Offset: 0x000500  Link: 7 (.dynstr)
  000000: Version: 1  File: libc.so.6  Cnt: 1
  0x0010:   Name: GLIBC_2.2.5  Flags: none  Version: 2

Displaying notes found in: .note.gnu.property
  Owner                Data size        Description
  GNU                  0x00000010       NT_GNU_PROPERTY_TYPE_0
      Properties: x86 feature: IBT, SHSTK

Displaying notes found in: .note.gnu.build-id
  Owner                Data size        Description
  GNU                  0x00000014       NT_GNU_BUILD_ID (unique build ID bitstring)
    Build ID: 7d708a123254121ca824515da17457100696ad11

Displaying notes found in: .note.ABI-tag
  Owner                Data size        Description
  GNU                  0x00000010       NT_GNU_ABI_TAG (ABI version tag)
    OS: Linux, ABI: 3.2.0
t@DESKTOP-NVJJKJO:~/githubCode/xuechou.github.io$
```

## ar

> 创建静态库，插入，删除，列出和提取成员。—— CSAPP

## strings

> 列出一个目标文件中所有可打印的字符串。

```bash
t@DESKTOP-NVJJKJO:~/githubCode/xuechou.github.io$ strings helloWorld
/lib64/ld-linux-x86-64.so.2
libc.so.6
puts
__cxa_finalize
__libc_start_main
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
u+UH
[]A\A]A^A_
Hello World!
:*3$"
GCC: (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.8060
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
helloWorld.c
__FRAME_END__
__init_array_end
_DYNAMIC
__init_array_start
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
__libc_csu_fini
_ITM_deregisterTMCloneTable
puts@@GLIBC_2.2.5
_edata
__libc_start_main@@GLIBC_2.2.5
__data_start
__gmon_start__
__dso_handle
_IO_stdin_used
__libc_csu_init
__bss_start
main
__TMC_END__
_ITM_registerTMCloneTable
__cxa_finalize@@GLIBC_2.2.5
.symtab
.strtab
.shstrtab
.interp
.note.gnu.property
.note.gnu.build-id
.note.ABI-tag
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rela.dyn
.rela.plt
.init
.plt.got
.plt.sec
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.dynamic
.data
.bss
.comment
t@DESKTOP-NVJJKJO:~/githubCode/xuechou.github.io$
```

## strip

> 从目标文件中删除符号表信息。

## ldd

> 列出可执行文件在运行时所需的共享库。

```bash
t@DESKTOP-NVJJKJO:~/githubCode/xuechou.github.io$ ldd helloWorld
        linux-vdso.so.1 (0x00007fffc1513000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f986cc40000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f986ce56000)
t@DESKTOP-NVJJKJO:~/githubCode/xuechou.github.io$
```