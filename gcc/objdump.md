## objdump 

> 所有二进制工具之母，能够显示目标文件的所有信息。最大作用是反汇编.text节的二进制指令。—— CSAPP

### 反汇编

ojbdump将`重定位文件`与`可执行文件`反汇编得到汇编代码。重定位文件的起始地址从0开始，但可执行文件不是。

**-d选项 反汇编**

`objdump -d hello > hello.s`    #也可以利用-d选项 --disassemble

<details>
  <summary>展开代码</summary>
  <pre><code>

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

  </code></pre>
</details>

**-S选项 混合显示C代码和汇编作为对照**

`objdump -S hello.o > hello.s`  #反汇编**重定位**文件

`objdump -S hello > hello.s`    #反汇编**可执行**文件

### 打印符号表

`objdump -t a.out`

<details>
  <summary>展开代码</summary>
  <pre><code>

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

  </code></pre>
</details>
