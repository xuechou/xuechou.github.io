## 统计目标文件的RAM和ROM开销

[ref](https://sourceware.org/binutils/docs/binutils/size.html)

**问题**：怎么需要统计工程中部分代码的RAM和ROM开销 ？

`size -t a.o b.o`  -t means totoals

- default format is `Berkeley`, and .rodata section is in .text section;
- using `--format=SysV` to see more detail.
