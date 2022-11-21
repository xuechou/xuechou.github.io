# armv8 cheat sheet

## Execution state, Exception level and Security States

![image](https://user-images.githubusercontent.com/10084724/202102813-68651cab-0ce8-4d9c-919c-bb048b871dcd.png)

- When in `AArch64` state, the processor executes the `A64` instruction set and use 64-bit wide general-purpose registers;
- When in `AArch32` state, the processor executes the `A32` or `T32` instruction set and use 32-bit wide general-purpose registers;

## jump between ELx

![image](https://user-images.githubusercontent.com/10084724/202984945-0a4adb77-fab4-4319-bfc6-d496984e939b.png)

## AArch64 register

### AArch64 general-purpose registers

![image](https://user-images.githubusercontent.com/10084724/202106102-31153931-ba3a-4bb8-93d0-19e58fefa19c.png)

![image](https://user-images.githubusercontent.com/10084724/202125695-ae6840b3-dff6-4e6b-a88c-5f9e44e8b6fd.png)

![image](https://user-images.githubusercontent.com/10084724/202126401-2db7bc26-cd42-4827-8b4d-c3557798092b.png)

### AArch64 special registers

![image](https://user-images.githubusercontent.com/10084724/202105028-b2a77e2c-0344-42a4-b341-514334360c40.png)

## cache

### 3 levels cache

- L1 cache has 2 types : data cache and instruction cache;
- L1 cache is inside core, every core has data cache and instruction cache;
- L2 cache is shared by all cores in same cluster, and only have 1 type : unified cache;
- L3 cache is shared by all cluster, and only have 1 type : unified cache;

![image](https://user-images.githubusercontent.com/10084724/202107354-708bd0ba-40e4-468d-ad3e-54bdeca43806.png)

###  Cache terminology

if we devide cache into m set, and 1 set = k cache line, so call it `k-way set associative`.

![image](https://user-images.githubusercontent.com/10084724/202107485-df0ed001-2154-4540-80d5-f48502390630.png)

## MMU

![image](https://user-images.githubusercontent.com/10084724/202107825-180afef8-7246-4101-aaa4-7822903487ce.png)

### address translation

![image](https://user-images.githubusercontent.com/10084724/202108168-b07aaefe-b49b-42bf-b00d-baaf7c726623.png)

### 2 stage translation

![image](https://user-images.githubusercontent.com/10084724/202108758-dbfd071e-3625-4f00-b157-b4aca3b01219.png)

## exception

### exception types

![image](https://user-images.githubusercontent.com/10084724/202137939-9015e502-84c9-42ea-bd55-92df8b51ee64.png)

### exception vector table

![image](https://user-images.githubusercontent.com/10084724/202944101-cec261fc-b747-4c49-8fc0-d8160029f25a.png)

## GIC

![image](https://user-images.githubusercontent.com/10084724/202635723-ec661713-d727-45d9-8b47-fa5bf792b814.png)

### interrupt state machine

![image](https://user-images.githubusercontent.com/10084724/202636007-fbe5012c-ed52-4633-b61e-d154209fff48.png)


