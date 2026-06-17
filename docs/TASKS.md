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

目标:

把解析出来的 VLESS 信息转换成 Clash YAML 节点

示例输入：

{
  "uuid": "...",
  "server": "bwg-five.us.fengqi0216.top",
  "port": 443,
  "name": "test-node"
}

目标输出：

- name: test-node
  type: vless
  server: bwg-five.us.fengqi0216.top
  port: 443
  uuid: 7e4d608f-2061-4eea-bba6-0b46c39c13fe

依赖：

TASK-001

状态：

TODO

## **TASK-003**

名称：

生成完整 Clash YAML

目标：

输出完整 Clash 配置结构

示例：

proxies:

- name: test-node
   type: vless
   server: example.com
   port: 443
   uuid: xxxxx

验收标准：

生成合法 YAML

包含 proxies 节点

状态：

TODO