def generate_clash_node(node):
    # 使用字符串拼接生成 YAML，避免引入第三方 YAML 依赖。
    return "\n".join(
        [
            f"- name: {node['name']}",
            "  type: vless",
            f"  server: {node['server']}",
            f"  port: {node['port']}",
            f"  uuid: {node['uuid']}",
        ]
    )


def generate_clash_yaml(node):
    # 在单个节点 YAML 外层增加 proxies 根节点，形成完整 Clash 配置片段。
    clash_node = generate_clash_node(node)

    # 节点挂在 proxies 列表下面，所以每一行都需要额外缩进两个空格。
    indented_node = "\n".join(f"  {line}" for line in clash_node.splitlines())
    return f"proxies:\n{indented_node}"
