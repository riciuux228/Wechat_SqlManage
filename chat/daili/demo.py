from pprint import pprint

import pymysql
import requests

from chat.lib.itchat.utils import logger


def connect_mysql():
    try:
        # 创建连接对象
        connection = pymysql.connect(
            host='localhost',  # 数据库主机地址
            user="root",  # 数据库用户名
            password="root",  # 数据库密码
            database='wechat_server',  # 数据库名称
            charset='utf8'
        )

        # 创建游标对象
        cursor = connection.cursor()
        return cursor
    except Exception as e:
        logger.info(f'数据库连接失败{e}')


cursor = connect_mysql()

quiry = "SELECT * FROM schedule ;"

cursor.execute(quiry)

result = cursor.fetchall()

for r in result:
    print(r)

quiry = "SELECT NOW()"

cursor.execute(quiry)

result = cursor.fetchall()
print(str(result))

cursor.close()

# 随机从mysql数据库word表中获取一条数据
def  get_random_word():
    cursor = connect_mysql()
    quiry = "SELECT * FROM words ORDER BY RAND() LIMIT 1"
    cursor.execute(quiry)
    result = cursor.fetchone()
    cursor.close()
    return result

r = get_random_word()
print(r)

# 爬取百度翻译
def get_baidu_translate(word):
    url = f'https://fanyi.baidu.com/sug'
    data = {
        'kw': word
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
    response = requests.post(url, data=data, headers=headers)
    return response.json()

# 生成一条英文句子用于翻译测试


word = 'world'
result = get_baidu_translate(word)
print(result)

# 生成一条中文句子用于翻译测试

word = '你好,世界'
result = get_baidu_translate(word)
print(result)





