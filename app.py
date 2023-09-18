from flask import Flask
import redis
import yaml

app = Flask(__name__)

# 读取配置文件
with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

# 从配置文件中获取Redis配置
redis_config = config['Redis']
redis_host = redis_config['host']
redis_port = redis_config['port']
redis_password = redis_config['password']
redis_db = int(redis_config.get('db', 0))  # 默认为0，如果未指定则使用默认值

# 连接到Redis服务器并选择所选的数据库
redis_client = redis.StrictRedis(
    host=redis_host,
    port=redis_port,
    password=redis_password,
    db=redis_db,  # 使用所选的数据库
    decode_responses=True  # 可选，如果希望返回的数据是解码后的字符串
)

@app.route('/')
def index():
    count = redis_client.incr('counter')
    return f'Total Visits: {count}'

if __name__ == '__main__':
    app.run("0.0.0.0")
