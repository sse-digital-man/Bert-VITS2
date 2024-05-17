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