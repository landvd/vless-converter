def generate_clash_node(node):
    # 使用字符串拼接生成 YAML，避免引入第三方 YAML 依赖。
    lines = [
        f"- name: {node['name']}",
        "  type: vless",
        f"  server: {node['server']}",
        f"  port: {node['port']}",
        f"  uuid: {node['uuid']}",
    ]

    reality_fields = ["network", "fp", "sni", "flow", "pbk", "sid"]
    if node.get("security") == "reality" and all(field in node for field in reality_fields):
        # Reality 节点需要额外输出 Clash 识别的 TLS、指纹、SNI 和 reality-opts 字段。
        lines.extend(
            [
                f"  network: {node['network']}",
                "  tls: true",
                f"  client-fingerprint: {node['fp']}",
                f"  servername: {node['sni']}",
                f"  flow: {node['flow']}",
                "  reality-opts:",
                f"    public-key: {node['pbk']}",
                f"    short-id: {node['sid']}",
            ]
        )

    return "\n".join(lines)


def generate_clash_yaml(node):
    # 支持单个节点或多个节点，统一生成 proxies 根节点。
    nodes = node if isinstance(node, list) else [node]
    clash_nodes = [generate_clash_node(item) for item in nodes]

    # 节点挂在 proxies 列表下面，所以每一行都需要额外缩进两个空格。
    indented_nodes = []
    for clash_node in clash_nodes:
        indented_nodes.extend(f"  {line}" for line in clash_node.splitlines())
    return "proxies:\n" + "\n".join(indented_nodes)
