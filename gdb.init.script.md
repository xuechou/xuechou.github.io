# .gdbinit

[https://www.cse.unsw.edu.au/~learn/debugging/modules/gdb_init_file/](https://www.cse.unsw.edu.au/~learn/debugging/modules/gdb_init_file/)

You have to create a . gdbinit file in the home directory and every project path.

**step1** add .gdbinit file in home directory

```bash
# create .gdbinit file in home directory
vim ~/.gdbinit
# copy the following line to ~/.gdbinit
set auto-load safe-path /
```

**step2** add .gdbinit file in *project*/.gdbinit

a simple demo that remote debug with qemu

```bash
# set target arch
set architecture aarch64
# remote debug only
target remote localhost: 1234
# set object file path, like xxx.img, xxx.elf
file wrkdir/srcs/baremetal/build/qemu-aarch64-virt/baremetal.elf
# add source files path
dir ./wrkdir/srcs/bao ./wrkdir/srcs/baremetal
# set debug layout
layout split
# add breakpoint
b main
```