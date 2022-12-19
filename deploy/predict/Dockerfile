FROM python:3.6-slim-stretch

RUN apt-get update
RUN apt install -y git
RUN python -m pip install --upgrade pip
RUN pip install torch==1.7.1+cpu torchvision==0.8.2+cpu torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install git+https://github.com/openai/CLIP.git

COPY clip_image_clip_text_sa_features_classifier_9_0.678.ckpt /clip_image_clip_text_sa_features_classifier_9_0.678.ckpt
COPY main.py /main.py
COPY utils.py /utils.py

WORKDIR .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
