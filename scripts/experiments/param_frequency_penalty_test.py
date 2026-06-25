#=========================频率惩罚参数测试=========================
#范围一般是 -2.0 到 2.0
from app.llm.client import generate_response
if __name__=="__main__":
    message=[{"role" : "user","content":"什么是幸福,100个字"}]
    response_1=generate_response(message,frequency_penalty=1.0)
    response_2=generate_response(message,frequency_penalty=-1.0)
    response_3=generate_response(message,frequency_penalty=2.0)

    print(response_1)
    print(response_2)
    print(response_3)
