# 配置conda环境：
1. `conda create -n BV2 python=3.11`
2. `pip install -r requirements.txt`
3. `conda install pytorch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1 pytorch-cuda=11.8 -c pytorch -c nvidia`

# 前置工作
1. 根目录新建Data文件夹并将模型文件夹放入其中，结构如图：
   Data:
        |-- models
        |   |-- model
        |   |   |-- .pth
        |config.json
2. 配置config.yml, 主要需要配置server段

# 运行
WebUI:`python webui.py`
WebAPI: `python hiyoriUI.py`

# 训练
1. `python webui_preprocess.py`查看训练指南,根据训练指南来生成训练数据即可
- 对于[AI-Hobbyist/Genshin_Datasets: Genshin Datasets For SVC/SVS/TTS](https://github.com/AI-Hobbyist/Genshin_Datasets)的数据集，可以使用`transcribe.py`得到esd.list文件

2. 正式训练：`python train_ms.py`
- 需要修改config.yml文件

# Docker
pull image: `docker pull kingkia/bert-vits2-api`
run: `docker run -it --rm --gpus=all --shm-size="16G" --name bert-vits2-container -v D:\SIP\BV2\Data:/workspace/Data -v D:\SIP\BV2\bert:/workspace/bert -p 5000:5000 bert-vits2-api  /bin/bash`
> 根据需要修改volume路径，必须写的包括Data、bert两个文件夹
