from src.generator import generate_clash_node, generate_clash_yaml
from src.parser import parse_vless_link


def convert_vless_links(text):
    # 批量读取多行 VLESS 文本，忽略空行后逐行解析。
    links = [line.strip() for line in text.splitlines() if line.strip()]
    nodes = [parse_vless_link(link) for link in links]

    # 交给生成器输出包含多个 proxies 节点的 Clash YAML。
    return generate_clash_yaml(nodes)


# converter.py 作为统一入口，集中导出解析和生成函数。
__all__ = [
    "parse_vless_link",
    "generate_clash_node",
    "generate_clash_yaml",
    "convert_vless_links",
]
