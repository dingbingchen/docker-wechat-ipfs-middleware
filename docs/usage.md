# 使用教程

## 1. 配置参数
修改 `src/config.py` 中的核心路径：
```python
# 本地微信目录（需与Docker挂载路径一致）
LOCAL_WECHAT_PATH = "/home/yourname/.xwechat"

# IPFS挂载点（供Docker访问）
IPFS_MOUNT_POINT = "/home/yourname/ipfs-wechat"
