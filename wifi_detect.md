## step 0: Install Kali Linux in VMware workstation

KALI官网提供了虚拟机中的镜像，直接下载并导入VM就OK.

如果报错，用VM升级一下镜像

## step 1: 把USB无线网卡连接到虚拟机

## step 2: 捕获握手的网络包 -- wifite2

wifite2仓库链接 https://github.com/derv82/wifite2

wifite2捕获握手网络包的视频 https://www.youtube.com/watch?v=qpnpI_mF3Aw

```bash
sudo wifite --kill
```

## step 3: 暴力破解握手包 -- hashcat 

https://hashcat.net/hashcat/

### 先转换网络包格式

https://hashcat.net/cap2hashcat/

### 生成密码字典

https://weakpass.com/

https://github.com/conwnet/wpa-dictionary

phone number generator https://github.com/asaotomo/makephonedict

[python script](./script/phoneNumberGenerator.py)

### 跑包

```ps
.\hashcat.exe -a 0 -m 22000 -o result.txt ..\672949_1694932864.hc22000 ..\phone_number_sh.txt
```

## FAQ 

### Why wifite2 can't scan any AP(the Access Point is a router)?

Reboot the Kali linux

### hashcat

```
hiprtcCompileProgram is missing from HIPRTC shared library.
```
可以用，但是不知道用的是GPU，还是CPU?


## Useful Resources
