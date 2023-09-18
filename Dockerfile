# 使用官方 Python 3 镜像作为基础镜像
FROM python:3

# 设置工作目录
WORKDIR /app

# 复制当前目录中的所有文件到工作目录中
COPY app.py .

# 安装依赖项
RUN pip install -r requirements.txt

# 暴露应用程序运行的端口
EXPOSE 5000

# 启动应用程序
CMD ["python", "app.py"]
