# docker-wechat-ipfs-middleware

将微信聊天记录通过IPFS实现分布式存储的中间层工具。

## 功能
- 实时监控微信本地文件变化并同步到IPFS
- 通过IPNS自动绑定最新文件版本，避免频繁修改路径
- 提供本地挂载点，让Docker容器直接访问IPFS中的文件

## 快速开始
1. 安装依赖：`pip install ipfshttpclient watchdog`
2. 启动IPFS节点：`ipfs daemon &`
3. 克隆本项目：`git clone https://github.com/yourusername/docker-wechat-ipfs-middleware.git`
4. 配置参数：修改 `config.py` 中的路径和IPFS节点信息
5. 启动中间层：`python main.py`
6. 调整Docker配置，挂载IPFS映射目录

## 文档
- [安装指南](installation.md)
- [使用教程](usage.md)
- [常见问题](faq.md)

## 截图


## 关联项目
- 微信容器化项目：[ricwang/docker-wechat](https://github.com/ricwang/docker-wechat)
