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
- 启动 IPFS 节点：
  ```bash
  ipfs daemon &  # 后台运行
## 2. 安装中间层程序
  ```bash
  # 克隆代码
  git clone https://github.com/你的用户名/docker-wechat-ipfs-middleware.git
  cd docker-wechat-ipfs-middleware

  # 安装依赖
  pip install -r requirements.txt

