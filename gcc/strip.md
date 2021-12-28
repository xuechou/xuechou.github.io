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