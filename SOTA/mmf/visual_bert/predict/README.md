# Запуск предсказания 

[Для работы требуется репозиторий](https://github.com/facebookresearch/mmf)

В конфиге нужно поменять:
```
data_dir C:\Users\notebook\.cache\torch\mmf\data\datasets
env:
cache_dir C:\Users\notebook\.cache\torch\mmf
data_dir: C:\Users\notebook\.cache\torch\mmf\data
save_dir: E:\mmf\save
```

[Веса обученной модели](https://drive.google.com/file/d/1HQYg-3I6szTQdqjRBGm4_-D4SGJuXFga)

Команда для запуска:
```
>python E:\coding\mmf\mmf_cli\predict.py \
	config=config.yaml \
	model=visual_bert \
	checkpoint.resume_file=E:\coding\MADE-graduation-projects\hateful_memes3\SOTA\mmf\visual_bert\predict\visual_bert.ckpt \
	checkpoint.resume_pretrained=False \
	run_type=val \
	dataset=hateful_memes
```

После выполнения должен появиться файл csv
Проверить качество можно с помощью [ноутбука](check_scv.ipynb). Нужно заменить путь в датасету

