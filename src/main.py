# src/main.py
import os
import time
import subprocess
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from config import LOCAL_WECHAT_PATH, IPFS_MOUNT_POINT, IPNS_KEY_NAME
from utils import init_ipfs_client, init_logger, get_ipns_key_id

logger = init_logger()
ipfs_client = init_ipfs_client()
ipns_key_id = get_ipns_key_id(ipfs_client, IPNS_KEY_NAME)

class WechatIPFSEventHandler(FileSystemEventHandler):
    """处理文件变化并同步到IPFS"""
    def __sync_directory(self):
        """同步整个目录到IPFS并更新IPNS"""
        try:
            # 上传目录并获取根CID
            res = ipfs_client.add(LOCAL_WECHAT_PATH, recursive=True, pin=True)
            root_cid = res[-1]["Hash"]
            
            # 更新IPNS指向
            ipfs_client.name.publish(root_cid, key=IPNS_KEY_NAME)
            logger.info(f"同步成功，新CID: {root_cid}，IPNS: /ipns/{ipns_key_id}")
            return root_cid
        except Exception as e:
            logger.error(f"同步失败: {str(e)}")
            return None

    def on_modified(self, event):
        if not event.is_directory:
            logger.info(f"文件修改: {event.src_path}")
            self.__sync_directory()

    def on_created(self, event):
        logger.info(f"文件创建: {event.src_path}")
        self.__sync_directory()

    def on_deleted(self, event):
        logger.info(f"文件删除: {event.src_path}")
        self.__sync_directory()

    def on_moved(self, event):
        logger.info(f"文件移动: {event.src_path} -> {event.dest_path}")
        self.__sync_directory()

def mount_ipfs_directory():
    """挂载IPNS目录到本地"""
    Path(IPFS_MOUNT_POINT).mkdir(parents=True, exist_ok=True)
    
    # 先卸载已存在的挂载
    subprocess.run(["umount", IPFS_MOUNT_POINT], check=False, capture_output=True)
    
    # 挂载IPNS目录
    mount_cmd = [
        "ipfs", "mount",
        IPFS_MOUNT_POINT,
        f"/ipns/{ipns_key_id}"
    ]
    result = subprocess.run(mount_cmd, capture_output=True, text=True)
    if result.returncode == 0:
        logger.info(f"IPFS挂载成功: {IPFS_MOUNT_POINT} -> /ipns/{ipns_key_id}")
        return True
    else:
        logger.error(f"挂载失败: {result.stderr}")
        return False

def main():
    # 首次同步并挂载
    if not mount_ipfs_directory():
        logger.error("初始化挂载失败，程序退出")
        return
    
    # 全量同步初始文件
    logger.info("开始首次全量同步...")
    WechatIPFSEventHandler()._WechatIPFSEventHandler__sync_directory()
    
    # 启动文件监控
    observer = Observer()
    observer.schedule(
        WechatIPFSEventHandler(),
        path=LOCAL_WECHAT_PATH,
        recursive=True
    )
    observer.start()
    logger.info(f"开始监控目录: {LOCAL_WECHAT_PATH}")

    try:
        while True:
            time.sleep(3600)  # 每小时检查一次挂载状态
            if not os.path.ismount(IPFS_MOUNT_POINT):
                logger.warning("挂载已断开，尝试重新挂载...")
                mount_ipfs_directory()
    except KeyboardInterrupt:
        observer.stop()
        logger.info("程序已停止")
    observer.join()

if __name__ == "__main__":
    main()
