# src/config.py
import os

# 本地路径配置
LOCAL_WECHAT_PATH = os.getenv("LOCAL_WECHAT_PATH", "/path/to/local/.xwechat")  # Docker挂载的本地目录
IPFS_MOUNT_POINT = os.getenv("IPFS_MOUNT_POINT", "/path/to/ipfs/mount")        # IPFS本地挂载点

# IPFS配置
IPFS_NODE_URL = os.getenv("IPFS_NODE_URL", "/ip4/127.0.0.1/tcp/5001/http")  # IPFS节点API地址
IPNS_KEY_NAME = os.getenv("IPNS_KEY_NAME", "wechat-backup")                # IPNS密钥名称
LOG_FILE_PATH = os.getenv("LOG_FILE_PATH", "ipfs_wechat_middleware.log")    # 日志文件路径
