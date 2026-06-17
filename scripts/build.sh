#!/bin/bash

set -e

# 每次构建前清理旧产物，确保 dist 目录只包含本次生成的 ZIP。
rm -rf dist
mkdir -p dist

# 打包发布所需目录和文件，并排除 Python 运行时缓存。
zip -r dist/vless-converter.zip \
    src \
    docs \
    samples \
    tests \
    README.md \
    -x "*/__pycache__/*" \
    -x "*.pyc"
