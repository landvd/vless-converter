不要写复杂架构。

先写：

# **Architecture**

## **目录结构**

src/

核心业务代码

tests/

测试代码

samples/

示例数据

docs/

项目文档

------

## **第一阶段**

VLESS URL

↓

解析器

↓

Python对象

↓

Clash YAML

## **模块**

converter.py

负责：

- URL解析
- 数据转换
- YAML输出