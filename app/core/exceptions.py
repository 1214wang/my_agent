#==================自定义异常=====================
class AppError(Exception):
    pass

class APIError(AppError):
    def __init__(self, message, retryable=False):
        self.retryable = retryable
        super().__init__(message)

class RAGError(AppError):
    pass

class ToolError(AppError):
    pass

class ParseError(AppError):
    pass