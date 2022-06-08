## 统计目标文件的RAM和ROM开销

[ref](https://sourceware.org/binutils/docs/binutils/size.html)

**问题**：怎么统计工程中部分代码的RAM开销和ROM开销 ？

e.g., the total ram and rom usage in a.o and b.o ?

`size -t a.o b.o`

- -t means totoals;
- talk more about **output format**
    - default ouput format is `Berkeley`;
        - .rodata section is in .text section;
    - using `--format=SysV` to see more detail;
