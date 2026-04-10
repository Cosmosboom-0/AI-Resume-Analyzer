import redis
import json
import os

# 连接Redis
REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
try:
    redis_client = redis.from_url(REDIS_URL)
    # 测试连接
    redis_client.ping()
    CACHE_ENABLED = True
except:
    # 如果Redis连接失败，禁用缓存
    CACHE_ENABLED = False
    redis_client = None

def get_cache(key):
    """
    从缓存中获取数据
    :param key: 缓存键
    :return: 缓存的数据，如果不存在返回None
    """
    if not CACHE_ENABLED:
        return None
    try:
        data = redis_client.get(key)
        if data:
            return json.loads(data)
        return None
    except:
        return None

def set_cache(key, value, expire=3600):
    """
    设置缓存
    :param key: 缓存键
    :param value: 缓存值
    :param expire: 过期时间（秒）
    """
    if not CACHE_ENABLED:
        return
    try:
        redis_client.setex(key, expire, json.dumps(value))
    except:
        pass

def delete_cache(key):
    """
    删除缓存
    :param key: 缓存键
    """
    if not CACHE_ENABLED:
        return
    try:
        redis_client.delete(key)
    except:
        pass