#=====================接口契约==============================
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from enum import Enum

# 定义消息角色的枚举：系统、用户、助手、工具
class Role(str, Enum):
    system = "system"
    user = "user"
    assistant = "assistant"
    tool = "tool"

# 单条消息结构
class Message(BaseModel):
    role: Role      # 角色
    content: str    # 消息内容

# 请求体结构（用户发来的）
class ChatRequest(BaseModel):
    messages: List[Message]          # 对话历史
    user_id: Optional[str] = None    # 用户ID（可选）
    session_id: Optional[str] = None # 会话ID（可选）
    metadata: Optional[Dict[str, Any]] = None  # 额外元数据

# 引用结构（RAG 返回的引用）
class Citation(BaseModel):
    chunk_id: str   # 引用来源的 chunk ID
    quote: str      # 引用的具体原文片段

# 最终回答结构
class Answer(BaseModel):
    final: str                      # 最终回答文本
    citations: List[Citation] = []  # 引用列表
    confidence: Optional[float] = None       # 置信度（可选）
    safety_flags: Optional[List[str]] = None # 安全标记（可选）

# 工具调用结构（Agent 使用）
class ToolCall(BaseModel):
    name: str                  # 工具名称
    arguments: Dict[str, Any]  # 工具参数
    call_id: str               # 调用ID（用于关联结果）

# 工具执行结果
class ToolResult(BaseModel):
    call_id: str                     # 对应的调用ID
    ok: bool                         # 是否成功
    data: Optional[Dict[str, Any]] = None  # 成功时返回的数据
    error: Optional[str] = None      # 失败时的错误信息

# 完整响应体（返回给前端）
class ChatResponse(BaseModel):
    answer: Answer                     # 最终答案
    request_id: str                    # 请求追踪ID
    timings: Dict[str, float]          # 各阶段耗时（毫秒）
    retrieved_ids: Optional[List[str]] = None   # 召回的 chunk ID 列表
    tool_calls: Optional[List[ToolCall]] = None   # 本次用到的工具调用
    tool_results: Optional[List[ToolResult]] = None # 工具执行结果

# 错误响应体
class ErrorResponse(BaseModel):
    code: str          # 错误码
    message: str       # 错误信息
    request_id: str    # 请求追踪ID
    retryable: bool = False  # 是否可重试