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