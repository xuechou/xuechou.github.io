# network cheat sheet

## route table

Print route table in linux : `route` or `netstat -rn`

```bash
tt@xxx:~$ route
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.79.18.1      255.255.255.255 U     1      0        0 eth0
172.16.0.0      0.0.0.0         255.255.0.0     U     256    0        0 eth0
172.16.98.137   0.0.0.0         255.255.255.255 U     256    0        0 eth0
172.16.255.255  0.0.0.0         255.255.255.255 U     256    0        0 eth0
224.0.0.0       0.0.0.0         240.0.0.0       U     256    0        0 eth0
255.255.255.255 0.0.0.0         255.255.255.255 U     256    0        0 eth0
127.0.0.0       0.0.0.0         255.0.0.0       U     256    0        0 lo
127.0.0.1       0.0.0.0         255.255.255.255 U     256    0        0 lo
127.255.255.255 0.0.0.0         255.255.255.255 U     256    0        0 lo
224.0.0.0       0.0.0.0         240.0.0.0       U     256    0        0 lo
255.255.255.255 0.0.0.0         255.255.255.255 U     256    0        0 lo
```
- 如果目的IP落在**Destination** + **Genmask** 表示的子网范围内，就用**Iface**表示的网卡，把packet转发到**Gatemask**
- 如果**Gateway=0.0.0.0**，表示无需gateway，属于同一个子网，packet可以直接转发给目标IP；
- 如果**Destination=0.0.0.0**，表示目标IP如果不适用其它路由规则，则使用该条；
  - 该条所描述的Gateway就是默认网关，不属于同一个子网，并且路由表中所有其它表项都不满足，则使用default Gateway进行转发；

## FAQ

### 超时重传 VS 快速重传

### MTU VS MSS

- maximum transmission unit (MTU): 链路层帧载荷的最大值
  - MTU of ethernet is 1500 bytes, and max size of ethernet > 1500 bytes;
- maximum segment size (MSS): TCP载荷的最大值
  - MSS = MTU - IP_header - TCP_header

![image](https://user-images.githubusercontent.com/10084724/208341065-a18d50e1-07e4-4784-bdd2-7f6e4c9a7c46.png)

image from https://www.imperva.com/learn/application-security/what-is-mtu-mss/

![image](https://user-images.githubusercontent.com/10084724/208340788-80116c87-ae1a-4aea-a18a-eff9d8acafb8.png)

####  check MTU in linux

```bash
tt@xxx:~$ ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
```
