import argparse
import sys
from pathlib import Path


# 直接执行 python3 src/cli.py 时，把项目根目录加入导入路径。
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.converter import convert_vless_links


def main():
    # 使用 argparse 定义命令行参数：输入文件必填，输出文件可选。
    parser = argparse.ArgumentParser(description="Convert VLESS links to Clash YAML.")
    parser.add_argument("input", help="VLESS links text file")
    parser.add_argument("output", nargs="?", help="optional output YAML file")
    args = parser.parse_args()

    input_path = Path(args.input)
    clash_yaml = convert_vless_links(input_path.read_text(encoding="utf-8"))

    if args.output:
        # 传入输出路径时写入文件。
        Path(args.output).write_text(clash_yaml, encoding="utf-8")
    else:
        # 未传入输出路径时打印到标准输出，方便管道处理。
        sys.stdout.write(clash_yaml)
        if sys.stdout.isatty() and not clash_yaml.endswith("\n"):
            sys.stdout.write("\n")


if __name__ == "__main__":
    main()
