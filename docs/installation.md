# 安装指南

## 1. 环境准备
- 安装IPFS：
  ```bash
  # 以Linux为例
  wget https://dist.ipfs.tech/go-ipfs/v0.22.0/go-ipfs_v0.22.0_linux-amd64.tar.gz
  tar -xvzf go-ipfs_v0.22.0_linux-amd64.tar.gz
  cd go-ipfs
  sudo ./install.sh
  ipfs init  # 初始化节点
