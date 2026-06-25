#===================结构化日志=========================
import logging
import json
import sys
from datetime import datetime

# 自定义日志格式：输出 JSON 格式的日志，便于采集和分析
class JSONFormatter(logging.Formatter):
    def format(self, record):
        # 构建日志记录字典
        log_record = {
            "timestamp": datetime.utcnow().isoformat(),  # UTC 时间戳
            "level": record.levelname,                  # 日志级别
            "message": record.getMessage(),              # 日志消息
            "module": record.module,                     # 模块名
            "function": record.funcName,                 # 函数名
            "line": record.lineno,                       # 行号
        }
        # 如果有 request_id 属性，一并记录（用于链路追踪）
        if hasattr(record, "request_id"):
            log_record["request_id"] = record.request_id
        return json.dumps(log_record)  # 转为 JSON 字符串

def get_logger(name: str):
    """获取一个配置好的 logger 实例"""
    logger = logging.getLogger(name)
    if not logger.handlers:  # 避免重复添加 handler
        handler = logging.StreamHandler(sys.stdout)  # 输出到标准输出
        handler.setFormatter(JSONFormatter())        # 使用 JSON 格式
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)                # 默认日志级别 INFO
    return logger