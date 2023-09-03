import json
import logging
import os

import requests

from chat.lib.itchat.utils import logger

os.system('chcp 65001')
cookies = {
    'CHAT2DB.LOCALE': 'zh-cn',
}

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'CHAT2DB.LOCALE=zh-cn',
    'Origin': 'http://127.0.0.1:10821',
    'Referer': 'http://127.0.0.1:10821/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
# 自然语言转sql
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

def transform_sql(databases,table_name,language,dataSourceId):
    params = {
        f'message': language,
        'promptType': 'NL_2_SQL',
        'dataSourceId': dataSourceId,
        f'databaseName': databases,
        f'tableNames': table_name,
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



# 获取所有数据库
def get_all_db():
    cookies = {
        'CHAT2DB.LOCALE': 'zh-cn',
    }

    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'CHAT2DB.LOCALE=zh-cn',
        'Referer': 'http://127.0.0.1:10821/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'pageNo': '1',
        'pageSize': '999',
    }

    response = requests.get('http://127.0.0.1:10821/api/connection/datasource/list', params=params, cookies=cookies,
                            headers=headers)
    # print(response.text)

    # 解析 JSON 数据
    data = json.loads(response.text)

    # 提取重要数据
    database_list = data['data']['data']
    output_list = []

    for database in database_list:
        output = {}
        output['id'] = database['id']
        output['alias'] = database['alias']
        output['url'] = database['url']
        output['user'] = database['user']
        output['password'] = database['password']
        output['host'] = database['host']
        output['port'] = database['port']
        output_list.append(output)

    return output_list

#



#
def get_all_databases(dataSourceId):
        cookies = {
            'CHAT2DB.LOCALE': 'zh-cn',
        }

        headers = {
            'Accept': 'application/json',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            # 'Cookie': 'CHAT2DB.LOCALE=zh-cn',
            'Referer': 'http://127.0.0.1:10821/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        extra_params = {
            "databaseType": "MYSQL",
            "dataSourceId": str(dataSourceId)
        }
        extra_params_str = json.dumps(extra_params)

        # 更新请求参数
        params = {
            'dataSourceId': dataSourceId,
            'refresh': 'false',
            'extraParams': extra_params_str,
        }

        response = requests.get('http://127.0.0.1:10821/api/rdb/database/list', params=params, cookies=cookies,
                                headers=headers)
        # 解析 JSON 数据
        data = json.loads(response.text)

        # 提取数据库名称
        database_names = [db['name'] for db in data['data']]

        return database_names

# 获取所有表名
def get_tables(databases_id,dataSourceName, databaseName):
    cookies = {
        'CHAT2DB.LOCALE': 'zh-cn',
    }

    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Referer': 'http://127.0.0.1:10821/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    base_url = 'http://127.0.0.1:10821/api/rdb/ddl/list'
    data_source_name = dataSourceName
    database_name = databaseName

    # 使用动态的连接地址和数据库名构建 URL
    url = f'{base_url}?pageNo=1&pageSize=999&dataSourceId={databases_id}&dataSourceName={data_source_name}&databaseType=MYSQL&databaseName={database_name}&schemaName&extraParams=%7B%22dataSourceId%22%3A2%2C%22dataSourceName%22%3A%22{data_source_name}%22%2C%22databaseType%22%3A%22MYSQL%22%2C%22databaseName%22%3A%22{database_name}%22%2C%22schemaName%22%3Anull%7D'

    response = requests.get(url, cookies=cookies, headers=headers)
    data = response.json()

    if data['success']:
        table_names = [table['name'] for table in data['data']['data']]
        return table_names
    else:
        print('请求失败')
        return []
# sql,2,database,id
def select_data(sql,dataSourceId,databases_name,consoleId):
    url = 'http://127.0.0.1:10821/api/rdb/dml/execute'

    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Cookie': 'CHAT2DB.LOCALE=zh-cn',
        'Origin': 'http://127.0.0.1:10821',
        'Referer': 'http://127.0.0.1:10821/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }



    # sql = 'SELECT * FROM timetask;'

    payload = {
        'sql': sql,
        'pageNo': 1,
        'pageSize': 200,
        'total': 0,
        'hasNextPage': True,
        'initDDL': '',
        'databaseName': databases_name,
        'dataSourceId': dataSourceId,
        'type': 'MYSQL',
        'schemaName': None,
        'consoleId': consoleId,
        'consoleName': 'new console'
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # 检查请求是否成功
    if response.status_code == 200:
        # 解析JSON数据
        parsed_data = json.loads(response.text)
        print(parsed_data)
        # 提取有用信息
        sql = parsed_data['data'][0]['sql']
        header_list = parsed_data['data'][0]['headerList']
        data_list = parsed_data['data'][0]['dataList']
        content = ""
        # 格式化输出
        # print("SQL语句:", sql)
        # print("数据:")
        sql = f"SQL 语句：{sql}\n"
        content += sql
        if header_list != None:
            print(f"headList = {header_list}")
            for item in header_list:
                print(item['name'],end=' ')
                content += item['name']+' '
            print('\n')
            content += '\n'
                    #content += line['name'] +'  '
        if data_list != None:
            for row in data_list:

                for line in row:
                    content += str(line) +" "
                content += '\n'
                content += "---------------------------------------------\n"
            return content
        else:
            return content

    else:
        return f'连接失败{sql}'

create_list = []

def create(name, dataSourceId, databaseName):
    # 检查 create_list 中是否已经存在相同的 dataSourceId
    for item in create_list:
        if item['dataSourceId'] == dataSourceId:
            print(f"DataSourceId {dataSourceId} already exists. Skipping creation.")
            return

    cookies = {
        'CHAT2DB.LOCALE': 'zh-cn',
    }

    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'http://127.0.0.1:10821',
        'Referer': 'http://127.0.0.1:10821/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'name': name,
        'ddl': '',
        'dataSourceId': dataSourceId,
        'databaseName': databaseName,
        'schemaName': None,
        'type': 'MYSQL',
        'status': 'DRAFT',
        'tabOpened': 'y',
    }
    dict_id_name = {
        'name': name,
        'dataSourceId': dataSourceId,
        'databasesName': databaseName
    }
    create_list.append(dict_id_name)
    response = requests.post('http://127.0.0.1:10821/api/operation/saved/create', cookies=cookies, headers=headers,
                             json=json_data)

    print(response.text)


def select_console(dataSourceId,dataSourceName,databaseName):
    cookies = {
        'CHAT2DB.LOCALE': 'zh-cn',
    }

    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'CHAT2DB.LOCALE=zh-cn',
        'Referer': 'http://127.0.0.1:10821/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get(
        f'http://127.0.0.1:10821/api/operation/saved/list?pageNo=1&pageSize=999&tabOpened=y&dataSourceId={dataSourceId}&dataSourceName=%40{dataSourceName}&databaseType=MYSQL&databaseName={databaseName}&schemaName',
        cookies=cookies,
        headers=headers,
    )
    # print(response.text)
    # 解析响应内容为 JSON 格式
    response_json = json.loads(response.text)

    # 提取 name 信息
    data = response_json['data']['data']
    names = [item['name'] for item in data]
    id = [item['id'] for item in data]
    logger.info(id)
    return id[0]

def update_id(id):
    cookies = {
        'CHAT2DB.LOCALE': 'zh-cn',
    }

    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'CHAT2DB.LOCALE=zh-cn',
        'Origin': 'http://127.0.0.1:10821',
        'Referer': 'http://127.0.0.1:10821/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'id': id,
        'tabOpened': 'n',
    }

    response = requests.post('http://127.0.0.1:10821/api/operation/saved/update', cookies=cookies, headers=headers,
                             json=json_data)
    print(response.text)

def find_database(id_or_name, db_list):
    result = []
    for line in db_list:

        if line['id'] == id_or_name:

            result.append(line['id'])
            result.append(line['alias'])
    return result

if __name__ == '__main__':
    all_db = get_all_db()
    print(f"all_db----->{all_db}")
    # 获取所有id和数据库名
    database_info = [(db['id'], db['alias']) for db in all_db]
    print(database_info)
    database_id = find_database(2,all_db)
    print(database_id)
    all_databases = get_all_databases(database_id[0])
    print(all_databases)
    all_tables = get_tables(database_id[0],database_id[1],all_databases[5])
    print(all_tables)
    table = all_tables[1]
    database = all_databases[5]

    print(table)
    print(database)

    # print(transform_sql('aurora', 't_about', '查询前十条数据'))
    sql = transform_sql("wechat_server",'schedule',"查询前十条数据",2)
    print(sql)
    create('new console',2,"wechat_server")
    id = select_console(2,'localhost','wechat_server')
    print(id)
    # print(database_id)
    # print(database)
    ret = select_data(sql,2,"wechat_server",id)
    print(ret)

    update_id(id)



    # all_databases = get_all_databases()
    # use_sql_list = get_all_databases(3)
    # print(use_sql_list)
    # tables = get_tables(2,'localhost','wechat_server')
    # print(tables)
    #get_tables(3,'154.7.177.80','aurora')