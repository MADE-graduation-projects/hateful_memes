# SOTA подходы

Цель - воспроизвети подходы из статьи facebook
https://ai.facebook.com/blog/hateful-memes-challenge-and-data-set/
https://arxiv.org/pdf/2005.04790v3.pdf

<picture>
  <img src="https://scontent-lhr8-1.xx.fbcdn.net/v/t39.2365-6/96772393_581552399130415_3226887050644946944_n.png?_nc_cat=100&ccb=1-7&_nc_sid=ad8a9d&_nc_ohc=mUnJHSKAv_sAX-dXGIi&_nc_ht=scontent-lhr8-1.xx&oh=00_AT-PmQA_82VlckfQC19hItmCUFgqyehQRHTzbwchdiMNuw&oe=634F8CFA"  width="350" height="200">
</picture>



## 1. MMF Visual BERT COCO [Инструкция](https://github.com/facebookresearch/mmf/tree/main/projects/hateful_memes)

Модель получилось запустить только в среде google colab [описание](mmf/visual_bert/train)


Скрипт для запуска предсказания [описание](mmf/visual_bert/predict)

<picture>
  <img src="https://github.com/MADE-graduation-projects/hateful_memes/blob/task15_mmf_visual_bert/SOTA/images/mmf_visaul_bert_metrics.png?raw=true"  width="250" height="250">
</picture>

### 1.1 Использование MMF Visual BERT COCO для извлечения признаков [ноутбук](mmf/visual_bert/feature_extractor/feature_extractor.ipynb)
 
Accuracy: 0.67	ROC AUC: 0.719472



### 1.2 Использование признаков полученных из моделей CLIP И Visual BERT [ноутбук](mmf/visual_bert/feature_extractor/feature_extractor_mmf_clip.ipynb)
 
Accuracy: 0.698	ROC AUC: 0.7452


Качество получилось хуже чем при использовании только CLIP (Accuracy: 0.732 ROC AUC: 0.798672) (ViT-L/14)
