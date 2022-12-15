#Эксперименты с русскоязычным датасетом

`data` - дамп бд

`base`

[1_ru_dataset_save.ipynb](base/1_ru_dataset_save.ipynb) - сохранение картинок, разделение на тренировочные и тестовые данные, создание файлов `train.jsonl` и `test.jsonl`

[2_ru_dataset_ocr.ipynb](base/2_ru_dataset_ocr.ipynb) - распознавание текста с помощью **easyocr**, добавдение ключа **recognized_text_easyocr**, создание файлов `train_ocr.jsonl` и `test_ocr.jsonl`

[3_ru_dataset_translate.ipynb](base/3_ru_dataset_translate.ipynb) - перевод текста с помощью модели **facebook/wmt19-ru-en**, добавдение ключа **translated_text**, создание файлов `train_trans.jsonl` и `test_trans.jsonl`

[4_clip_easyocr.ipynb](base/4_clip_easyocr.ipynb) - обучение модели с текстом на русском языке

Accuracy: 0.633	ROC AUC: 0.627

[5_clip_translated.ipynb](base/5_clip_translated.ipynb) - обучение модели с текстом переведенным на английский язык

Accuracy: 0.618	ROC AUC: 0.572
