# src/utils.py
import logging
import ipfshttpclient
from config import IPFS_NODE_URL, LOG_FILE_PATH

def init_ipfs_client():
    """初始化IPFS客户端并返回连接"""
    try:
        return ipfshttpclient.connect(IPFS_NODE_URL)
    except Exception as e:
        raise ConnectionError(f"IPFS节点连接失败: {str(e)}，请确保ipfs daemon已启动")

def init_logger():
    """初始化日志配置"""
    logger = logging.getLogger("ipfs-wechat-middleware")
    logger.setLevel(logging.INFO)
    
    # 避免重复添加处理器
    if logger.handlers:
        return logger
    
    # 文件处理器
    file_handler = logging.FileHandler(LOG_FILE_PATH)
    # 控制台处理器
    console_handler = logging.StreamHandler()
    
    # 日志格式
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger

def get_ipns_key_id(client, key_name):
    """获取IPNS密钥ID（若不存在则创建）"""
    keys = client.key.list()
    for key in keys:
        if key["Name"] == key_name:
            return key["Id"]
    # 创建新密钥
    return client.key.gen(key_name, "rsa")["Id"]
