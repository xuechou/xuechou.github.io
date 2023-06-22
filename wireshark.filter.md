## How to only show packets from a certain application?

There is no way to do it.

ref: https://www.wireshark.org/lists/wireshark-users/200802/msg00124.html

## useful filter in V2G(vehicle to grid) communication

1. show all TCP problems --> `tcp.analysis.flags`, same as `wireshark expert information`
2. show only one TCP stream --> right click then go down to `follow TCP stream`
3. TODO: find string in `info`  --> Ctrl + F