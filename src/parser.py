from urllib.parse import unquote, urlparse


def parse_vless_link(link):
    # 使用 urllib.parse 拆解 VLESS URL，保留查询参数给后续任务扩展。
    parsed = urlparse(link)

    # TASK-001 只需要提取 uuid、server、port、name；缺少核心字段时直接报错。
    if parsed.scheme != "vless":
        raise ValueError("link must use vless scheme")
    if not parsed.username:
        raise ValueError("link must include uuid")
    if not parsed.hostname:
        raise ValueError("link must include server")
    if parsed.port is None:
        raise ValueError("link must include port")

    return {
        "uuid": unquote(parsed.username),
        "server": parsed.hostname,
        "port": parsed.port,
        "name": unquote(parsed.fragment),
    }
