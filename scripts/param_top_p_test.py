#===================核采样参数测试=====================
from core.llm_client import generate_response
if __name__=="__main__":
    message=[{"role" : "user","content":"什么是幸福,50个字"}]
    response_1=generate_response(message,top_p=0.8)
    response_2=generate_response(message,top_p=0.2)


    print(response_1)
    print("\n")
    print(response_2)