from chat.lib.itchat.utils import logger


def cal_time(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        logger.info("函数名：%s\t执行时间：%s", func.__name__, str(end - start))
        # print("执行时间：", end - start)
        return res

    return wrapper