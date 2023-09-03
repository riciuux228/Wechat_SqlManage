import json

import requests

def chat_gpt():

    url = 'https://www.qlwechat.cn/api/openai/v1/chat/completions'  # 替换为你的请求 URL

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ak-wjl',  # 替换为你的授权信息
    }

    data = {
        # 根据 API 的要求，构造请求的数据
        # 如果需要在请求中传递额外的参数，请根据 API 的文档进行相应的设置
    'messages': [
            {
                'role': 'system',
                'content': '\nYou are ChatGPT, a large language model trained by OpenAI.\nKnowledge cutoff: 2021-09\nCurrent model: gpt-3.5-turbo-16k\nCurrent time: 2023/8/2 21:37:23\n',
            },
            {
                'role': 'user',
                'content': '你好',
            },
        ],
        'stream': True,
        'model': 'gpt-3.5-turbo-16k',
        'temperature': 0.5,
        'presence_penalty': 0,
        'frequency_penalty': 0,
        'top_p': 1,
    }


    response = requests.post(url, headers=headers, json=data)

    # 检查相映是否成功，流式获取响应的json内容
    if response.status_code == 200:
        lines = []  # 创建一个空列表用于存储响应行

        for line in response.iter_lines():
            if line:
                line = line.decode('utf-8')  # 将字节字符串转换为字符串
                line = line.replace('\n', '')  # 去掉换行符
                line = line.replace("data: ", "")
                line = line.replace("[DONE]", "")

                lines.append(line)  # 将每行数据添加到列表中

        # 去除最后一条数据
        lines = lines[:-1]
        all_data = []
        for line in lines:
            # print(line)

            # 解析JSON数据
            data = json.loads(line)
            if data['choices'][0]['delta']:

                print(data['choices'][0]['delta']['content'])






    else:
        print('请求失败，状态码:', response.status_code)



def chat_gpt_nos_tream ():
    url = 'https://www.qlwechat.cn/api/openai/v1/chat/completions'  # 替换为你的请求 URL

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ak-wjl',  # 替换为你的授权信息
    }

    data = {
        # 根据 API 的要求，构造请求的数据
        # 如果需要在请求中传递额外的参数，请根据 API 的文档进行相应的设置
        'messages': [
            {
                'role': 'system',
                'content': '\nYou are ChatGPT, a large language model trained by OpenAI.\nKnowledge cutoff: 2021-09\nCurrent model: gpt-3.5-turbo-16k\nCurrent time: 2023/8/2 21:37:23\n',
            },
            {
                'role': 'user',
                'content': '你好',
            },
        ],
        'stream': False,  # 设置为 False，表示非流式获取响应
        'model': 'gpt-3.5-turbo-16k',
        'temperature': 0.5,
        'presence_penalty': 0,
        'frequency_penalty': 0,
        'top_p': 1,
    }

    response = requests.post(url, headers=headers, json=data)

    # 检查响应是否成功
    if response.status_code == 200:
        print('请求成功，响应为:', response.text)

    else:
        print('请求失败，状态码:', response.status_code)

chat_gpt_nos_tream()



