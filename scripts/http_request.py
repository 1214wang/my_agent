import requests
# #定义你要访问的目标网址（这是一个测试网站，专门用来验证请求）
# # url="https://httpbin.liujiacai.net/get?name=小张&age=18"
# url="https://httpbin.liujiacai.net/get"
# params={
#     "name":"小李",
#     "age":19
# }
# try:
# #核心代码——用requests发一个GET请求，把结果存在变量 response 里
# # response 就是服务器给你的“回复包裹”，里面装了状态码、返回内容等所有信息
#     response=requests.get(url, params=params)
# # 打印状态码——200代表成功，404代表网址错了，500代表服务器崩了
#     if response.status_code == 200:
#         print("请求成功！")
#         print(response.json()["args"]["name"])
#     elif response.status_code==404:
#         print("地址不存在,检查网址是否写错")
#     elif response.status_code==500:
#         print("服务器连接超时，请稍后再试")
#     elif response.status_code==401:
#         print("权限不足")
# except requests.exceptions.Timeout:
#     print("请求超时")
# except requests.exceptions.ConnectionError:
#     print("网络连接失败")
# except Exception as e:
#     print("请求过程中发生了其他错误：",e)
#     print("状态码：",response.status_code)
#     print(response)
# # 打印服务器返回的文本内容
#     print("返回内容：",response.text)

#     print("返回内容：",response.json())


# POST POST POST POST POST POST POST POST POST POSTPOST POST POST POSTPOST POST POST POST
# 1. 目标接口地址
url="https://jsonplaceholder.typicode.com/posts"
# 2. 请求头：告诉服务器，我发的是JSON格式的数据
# 调用大模型时，这个请求头是必填的
headers={"Content-Type":"application/json"}
# 3. 请求体：你要发给服务器的真实数据（放在包裹里的内容）
# 格式是Python字典，后面会自动转成JSON
request_data={
    "title":"我的第一篇帖子",
    "body":"这是我的第一条post请求",
    "useid":101, 
}
try:
    response=requests.post(url,headers=headers,json=request_data,timeout=10)
    response.encoding="utf-8"
    if response.status_code==200 or response.status_code==201:
        print("发送成功")
        result=response.json()
        print("返回对应的id:",result["id"])
        print("返回对应的具体内容:",response.text)
        print(response.json())
        print(response.text)
    elif response.status_code==400:
        print("参数错误（400），检查请求体格式对不对")
except Exception as e:
    print(f"发送出现其他异常{e}")
