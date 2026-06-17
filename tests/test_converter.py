import unittest
from pathlib import Path

from src.converter import generate_clash_node, generate_clash_yaml, parse_vless_link


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
        self.assertEqual(parse_vless_link(self.vless_link), self.node)

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


if __name__ == "__main__":
    unittest.main()
