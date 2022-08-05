# symbol table VS debug symbols

[wiki link](https://en.wikipedia.org/wiki/Debug_symbol)

`symbol table` : one symbol is a address of data or function.

`debug symbol` : *A debug symbol is a special kind of symbol that attaches additional information to the symbol table of an object file.*

So, the debug symbol is within the symbol table.

## view symbol table

**objdump -t**

```bash
tt@ZHANGKAIWEN01:~$ objdump a.out -t

a.out:     file format elf64-x86-64

SYMBOL TABLE:
0000000000000318 l    d  .interp        0000000000000000              .interp
0000000000000338 l    d  .note.gnu.property     0000000000000000              .note.gnu.property
0000000000000358 l    d  .note.gnu.build-id     0000000000000000              .note.gnu.build-id
000000000000037c l    d  .note.ABI-tag  0000000000000000              .note.ABI-tag
...
...
```
## view debug symbols

**grep .debug in symbol table**

```bash
tt@xxx:~$ objdump a.out -t | grep .debug
0000000000000000 l    d  .debug_aranges 0000000000000000              .debug_aranges
0000000000000000 l    d  .debug_info    0000000000000000              .debug_info
0000000000000000 l    d  .debug_abbrev  0000000000000000              .debug_abbrev
0000000000000000 l    d  .debug_line    0000000000000000              .debug_line
0000000000000000 l    d  .debug_str     0000000000000000              .debug_str
```

## Check if there is a debug symbol using file command

```bash
# no debug symbols, build with `gcc hello.c`
tt@xxx:~$ file a.out
a.out: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=30bd96750c22e4e2f8ff3e214318aa17dc80a900, for GNU/Linux 3.2.0, not stripped
```

```bash
# there is debug symbols, build with `gcc hello.c -g`
tt@xxx:~$ file a.out
a.out: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=a1c6d8cf4ac556b017cd1de27cba47f98dd0ac25, for GNU/Linux 3.2.0, with debug_info, not stripped
```

- `not stripped` shows only there is a symbol table in a.out, no infomation about debug symbols.
- If build object with `gcc -g`, there is `with debug_info` in file command output.

