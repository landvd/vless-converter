# **VLESS Converter Tasks**

## **TASK-001**

名称：

解析 VLESS 链接

目标：

输入：

vless://uuid@server:443?...#name

输出：

{
    "uuid": "7e4d608f-2061-4eea-bba6-0b46c39c13fe",
    "server": "bwg-five.us.fengqi0216.top",
    "port": 443,
    "name": "test-node"
}

验收标准：

能够正确解析 VLESS 链接

状态：

TODO

------

## **TASK-002**

名称：

生成 Clash 节点

依赖：

TASK-001

状态：

TODO