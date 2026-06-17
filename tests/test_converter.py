import unittest
from pathlib import Path

from src.converter import (
    convert_vless_links,
    generate_clash_node,
    generate_clash_yaml,
    parse_vless_link,
)


class ConverterTest(unittest.TestCase):
    def setUp(self):
        # 从 samples/sample.txt 读取统一的 VLESS 示例，避免测试数据分散。
        sample_path = Path(__file__).resolve().parents[1] / "samples" / "sample.txt"
        self.vless_link = sample_path.read_text(encoding="utf-8").strip()
        self.node = {
            "uuid": "7e4d608f-2061-4eea-bba6-0b46c39c13fe",
            "server": "bwg-five.us.fengqi0216.top",
            "port": 443,
            "name": "test-node",
        }

    def test_parse_vless_link(self):
        # 验证 VLESS 链接能解析成后续生成 YAML 所需的字段。
        parsed_node = parse_vless_link(self.vless_link)

        for key, value in self.node.items():
            self.assertEqual(parsed_node[key], value)

    def test_parse_vless_link_with_reality_params(self):
        # 验证 Reality 相关 URL 参数会被解析到节点字典中。
        reality_link = (
            "vless://7e4d608f-2061-4eea-bba6-0b46c39c13fe@"
            "bwg-five.us.fengqi0216.top:443?"
            "type=tcp&encryption=none&security=reality&"
            "pbk=2A4OL5PWDBcY8-QmrqlHft06j3iqRg5g3kgUd185mQg&"
            "fp=chrome&sni=emby.vickypig.com&sid=341d&"
            "flow=xtls-rprx-vision#test-node"
        )
        expected = {
            "uuid": "7e4d608f-2061-4eea-bba6-0b46c39c13fe",
            "server": "bwg-five.us.fengqi0216.top",
            "port": 443,
            "name": "test-node",
            "network": "tcp",
            "encryption": "none",
            "security": "reality",
            "pbk": "2A4OL5PWDBcY8-QmrqlHft06j3iqRg5g3kgUd185mQg",
            "fp": "chrome",
            "sni": "emby.vickypig.com",
            "sid": "341d",
            "flow": "xtls-rprx-vision",
        }

        self.assertEqual(parse_vless_link(reality_link), expected)

    def test_generate_clash_node(self):
        # 验证单个 Clash 节点 YAML 的字段和缩进。
        expected = "\n".join(
            [
                "- name: test-node",
                "  type: vless",
                "  server: bwg-five.us.fengqi0216.top",
                "  port: 443",
                "  uuid: 7e4d608f-2061-4eea-bba6-0b46c39c13fe",
            ]
        )

        self.assertEqual(generate_clash_node(self.node), expected)

    def test_generate_clash_node_with_reality_params(self):
        # 验证 Reality VLESS 节点会输出 Clash 所需的 Reality 字段。
        reality_node = {
            "uuid": "7e4d608f-2061-4eea-bba6-0b46c39c13fe",
            "server": "bwg-five.us.fengqi0216.top",
            "port": 443,
            "name": "test-node",
            "network": "tcp",
            "encryption": "none",
            "security": "reality",
            "pbk": "2A4OL5PWDBcY8-QmrqlHft06j3iqRg5g3kgUd185mQg",
            "fp": "chrome",
            "sni": "emby.vickypig.com",
            "sid": "341d",
            "flow": "xtls-rprx-vision",
        }
        expected = "\n".join(
            [
                "- name: test-node",
                "  type: vless",
                "  server: bwg-five.us.fengqi0216.top",
                "  port: 443",
                "  uuid: 7e4d608f-2061-4eea-bba6-0b46c39c13fe",
                "  network: tcp",
                "  tls: true",
                "  client-fingerprint: chrome",
                "  servername: emby.vickypig.com",
                "  flow: xtls-rprx-vision",
                "  reality-opts:",
                "    public-key: 2A4OL5PWDBcY8-QmrqlHft06j3iqRg5g3kgUd185mQg",
                "    short-id: 341d",
            ]
        )

        self.assertEqual(generate_clash_node(reality_node), expected)

    def test_generate_clash_yaml(self):
        # 验证完整 Clash YAML 包含 proxies 根节点和节点列表。
        expected = "\n".join(
            [
                "proxies:",
                "  - name: test-node",
                "    type: vless",
                "    server: bwg-five.us.fengqi0216.top",
                "    port: 443",
                "    uuid: 7e4d608f-2061-4eea-bba6-0b46c39c13fe",
            ]
        )

        self.assertEqual(generate_clash_yaml(self.node), expected)

    def test_convert_vless_links(self):
        # 验证多行 VLESS 文本会忽略空行，并生成多个 proxies 节点。
        second_link = self.vless_link.replace("#test-node", "#backup-node")
        vless_text = f"\n{self.vless_link}\n\n{second_link}\n"
        expected = "\n".join(
            [
                "proxies:",
                "  - name: test-node",
                "    type: vless",
                "    server: bwg-five.us.fengqi0216.top",
                "    port: 443",
                "    uuid: 7e4d608f-2061-4eea-bba6-0b46c39c13fe",
                "  - name: backup-node",
                "    type: vless",
                "    server: bwg-five.us.fengqi0216.top",
                "    port: 443",
                "    uuid: 7e4d608f-2061-4eea-bba6-0b46c39c13fe",
            ]
        )

        self.assertEqual(convert_vless_links(vless_text), expected)


if __name__ == "__main__":
    unittest.main()
