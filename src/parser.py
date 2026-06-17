from urllib.parse import parse_qs, unquote, urlparse


def parse_vless_link(link):
    # 使用 urllib.parse 拆解 VLESS URL，保留查询参数给后续任务扩展。
    parsed = urlparse(link)
    query_params = parse_qs(parsed.query)

    # TASK-001 只需要提取 uuid、server、port、name；缺少核心字段时直接报错。
    if parsed.scheme != "vless":
        raise ValueError("link must use vless scheme")
    if not parsed.username:
        raise ValueError("link must include uuid")
    if not parsed.hostname:
        raise ValueError("link must include server")
    if parsed.port is None:
        raise ValueError("link must include port")

    node = {
        "uuid": unquote(parsed.username),
        "server": parsed.hostname,
        "port": parsed.port,
        "name": unquote(parsed.fragment),
    }

    # Reality 参数来自 URL query，parse_qs 会把每个参数解析成列表，这里取第一个值。
    query_field_map = {
        "type": "network",
        "encryption": "encryption",
        "security": "security",
        "pbk": "pbk",
        "fp": "fp",
        "sni": "sni",
        "sid": "sid",
        "flow": "flow",
    }
    for query_key, node_key in query_field_map.items():
        if query_key in query_params and query_params[query_key]:
            node[node_key] = query_params[query_key][0]

    return node
