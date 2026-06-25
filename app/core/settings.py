#==============================统一配置===========================
import os
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()

class Settings:
    # DashScope（阿里云百炼）API Key
    DASHSCOPE_API_KEY: str = os.getenv("DASHSCOPE_API_KEY", "")
    # 使用的模型名称
    MODEL_NAME: str = os.getenv("MODEL_NAME", "qwen-plus")
    # API 基础地址
    BASE_URL: str = os.getenv("BASE_URL", "https://dashscope.aliyuncs.com/api/v1")
    # 是否开启追踪（调试用）
    TRACE_ENABLED: bool = os.getenv("TRACE_ENABLED", "false").lower() == "true"
    # 最大重试次数
    MAX_RETRIES: int = int(os.getenv("MAX_RETRIES", "3"))
    # 单次请求超时时间（秒）
    TIMEOUT: float = float(os.getenv("TIMEOUT", "30.0"))

# 全局配置实例（其他模块导入使用）
settings = Settings()