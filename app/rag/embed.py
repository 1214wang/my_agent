# app/rag/embed.py
# 功能：封装百炼的 Embedding 模型，将文本转化为向量

from langchain_community.embeddings import DashScopeEmbeddings
from app.core.settings import settings  # 从配置中读取 API Key

def get_embedding_model():
    """
    返回一个 DashScopeEmbeddings 实例。
    使用 text-embedding-v4 模型（规划要求）。
    如果不可用，请根据百炼控制台实际模型名调整。
    """
    return DashScopeEmbeddings(
        model="text-embedding-v4",          # 百炼 Embedding 模型名
        dashscope_api_key=settings.DASHSCOPE_API_KEY  # API Key
    )