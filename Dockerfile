# 基础CUDA镜像
FROM cnstark/pytorch:2.0.1-py3.10.11-cuda11.8.0-ubuntu22.04

LABEL maintainer="1581690775@qq.com"
LABEL version="dev-20240525"
LABEL description="Docker api image for Bert-Vits2"

# 安装第三方包
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC
# 最后清理包缓存以减小镜像体积
RUN apt-get update && \
    apt-get install -y --no-install-recommends tzdata ffmpeg libsox-dev parallel aria2 && \
    rm -rf /var/lib/apt/lists/* 

# 复制并安装python依赖
WORKDIR /workspace
COPY requirements.txt /workspace/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install chardet
RUN pip install torch==2.1.1+cu118 torchvision==0.16.1+cu118 torchaudio==2.1.1+cu118 --extra-index-url https://download.pytorch.org/whl/cu118

# 复制剩余的应用
COPY . /workspace
# 暴露端口
EXPOSE 5000

CMD ["python", "hiyoriUI.py"]
