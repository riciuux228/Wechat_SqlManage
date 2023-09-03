import json
import os

import requests

# 设置控制台编码为 UTF-8
os.system('chcp 65001')
cookies = {
    'CHAT2DB.LOCALE': 'zh-cn',
}

headers = {
    'Accept': 'text/event-stream',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    # 'Cookie': 'CHAT2DB.LOCALE=zh-cn',
    'DBHUB': 'null',
    'Referer': 'http://127.0.0.1:10821/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'uid': '069461a3-5edb-4718-917c-e9226cd85bf2',
}
def transform_sql(databases,table_name,language):
    params = {
        f'message': {language},
        'promptType': 'NL_2_SQL',
        'dataSourceId': '3',
        f'databaseName': {databases},
        f'tableNames': {table_name},
    }

    response = requests.get('http://127.0.0.1:10821/api/ai/chat', params=params, cookies=cookies, headers=headers)
    data = response.content.decode('utf-8')

    # print(response.text)
    #data = str(response.text)

    # 按行分割输出结果
    # 解析数据并提取 content 字段的内容
    content_list = []
    for line in data.split('\n'):
        if line.startswith('data:'):
            # print(line)
            if 'content' in line:
                # print(line)
                content_list.append(line)

    # print(content_list)

    content = ""
    for item in content_list:
        st = json.loads(item.replace('data:', '')).get('content', '')
        content += st
    # content += ';'
    # if ';' not in content:
    #     content += ';'

    return content

if __name__ == '__main__':

  print(transform_sql('aurora', 't_about', '查询全部数据'))