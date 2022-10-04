 # Предобработка данных
 
## 1. Удаление надписей с картинки

 1. С помощью модуля easyocr находим на изображении области с надписями. Создается файл `ocr.json` с содержимым такого вида:
 ```
 ([[81, 2], [441, 2], [441, 43], [81, 43]], 'when you"re feeling [orty', 0.1467968358049227), 
 
 ([[27, 41], [539, 41], [539, 79], [27, 79]], 'asilbugou (abibi[s 0. [erfods llets (yagoad', 0.15825469926049332)])
 ```
 
 
 2. Пересохраняем файл в другом формате, создается файл `ocr.box.json`
 ```
 [[[81, 2, 441, 43], 'when you"re feeling [orty', 0.1467968358049227], [[27, 41, 539, 79], 'asilbugou (abibi[s 0. [erfods llets (yagoad', 0.15825469926049332]]
 ```
 
 
 3. Затираем область с тестом и создаем файл с маской текста. Файлы сохраняются в папке `img_mask_3px`

<picture>
  <img src="https://github.com/MADE-graduation-projects/hateful_memes/blob/task13_data_preprocessing/competitions/HimariO/1_prepare_data/images/1.3/01235.png"  width="300" height="300">
</picture> -> 
<picture>
  <img src="https://github.com/MADE-graduation-projects/hateful_memes/blob/task13_data_preprocessing/competitions/HimariO/1_prepare_data/images/1.3/01235_2.png"  width="300" height="300">
</picture> +
<picture>
  <img src="https://github.com/MADE-graduation-projects/hateful_memes/blob/task13_data_preprocessing/competitions/HimariO/1_prepare_data/images/1.3/01235.mask.png"  width="300" height="300">
</picture>




 4. С помощью DeepFillV2 из модулей mmcv и mmedit удаляем надписи. Результат сохраняется в папку `img_clean`
 
<picture>
  <img src="https://github.com/MADE-graduation-projects/hateful_memes/blob/task13_data_preprocessing/competitions/HimariO/1_prepare_data/images/1.4/01235.png"  width="300" height="300">
</picture>



## 2. Поиск объектов на изображении

С помощью InceptionV2 OID находим на изображениях объекты и принадлежащие им области. Создается файл `box_annos.json`
```
[{'ymin': 0.26804885268211365,
  'xmin': 0.3950812816619873,
  'ymax': 0.6153359413146973,
  'xmax': 0.5982983112335205,
  'score': 0.9718632102012634,
  'class_name': 'Human face',
  'class_id': 502},
 {'ymin': 0.1488388329744339,
  'xmin': 0.36896005272865295,
  'ymax': 0.3470507562160492,
  'xmax': 0.6266028881072998,
  'score': 0.32622191309928894,
  'class_name': 'Hat',
  'class_id': 161},]
```
<picture>
  <img src="https://github.com/MADE-graduation-projects/hateful_memes/blob/task13_data_preprocessing/competitions/HimariO/1_prepare_data/images/2/01235.png"  width="300" height="300">
</picture>


## 3. Разделение изображений представленных комиксом на отдельные картинки

С помощью Res2Net Patch Detector делим изображение. Создается файл `split_img_clean_boxes.json`. Файлы сохраняются в папке `split_img_clean`

<picture>
  <img src="https://github.com/MADE-graduation-projects/hateful_memes/blob/task13_data_preprocessing/competitions/HimariO/1_prepare_data/images/3/01576.png"  width="300" height="300">
</picture> -> 
<picture>
  <img src="https://github.com/MADE-graduation-projects/hateful_memes/blob/task13_data_preprocessing/competitions/HimariO/1_prepare_data/images/3/01576.0.png"  width="300" height="300">
</picture> +
<picture>
  <img src="https://github.com/MADE-graduation-projects/hateful_memes/blob/task13_data_preprocessing/competitions/HimariO/1_prepare_data/images/3/01576.1.png"  width="300" height="300">
</picture>


## 4. Определение расы и пола людей на изображении

Используется библиотека dlib

### 4.1 
Пример результата:
  ```
{'img_name': '01235.png', 'boxes_and_score': [{'ymin': 0.2707633674144745, 'xmin': 0.39449542760849, 'ymax': 0.618645429611206, 'xmax': 0.5975348353385925, 'score': 0.9788097739219666, 'class_name': 'Human face', 'class_id': 502}, {'ymin': 0.1195806935429573, 'xmin': 0.050002746284008026, 'ymax': 0.9922588467597961, 'xmax': 0.9625630378723145, 'score': 0.9190647006034851, 'class_name': 'Man', 'class_id': 308}, {'ymin': 0.49269676208496094, 'xmin': 0.07834305614233017, 'ymax': 0.9805120229721069, 'xmax': 0.9698421359062195, 'score': 0.7085372805595398, 'class_name': 'Clothing', 'class_id': 433}, {'ymin': 0.45603710412979126, 'xmin': 0.020553115755319595, 'ymax': 0.9691803455352783, 'xmax': 0.3579131066799164, 'score': 0.21738770604133606, 'class_name': 'Human arm', 'class_id': 503}]}
Find 1 faces
119 (210, 79) (328, 197)
Middle Eastern Male
[4.1799635e-02 1.0545440e-03 9.6204944e-02 2.5493049e-05 1.0217457e-04
 4.1344479e-01 4.4736835e-01] [9.9996126e-01 3.8761355e-05]

{'01235.png': {'face_boxes': [[210, 79, 328, 197]],
  'face_race': ['Middle Eastern'],
  'face_gender': ['Male']}}
  ```

### 4.2 
Пример результата:
```
#{"img_name": "01235.png", "boxes_and_score": [
#{"ymin": 0.2707633674144745, "xmin": 0.39449542760849, "ymax": 0.618645429611206, "xmax": 0.5975348353385925, "score": 0.9788097739219666, "class_name": "Human face", "class_id": 502, "race": null, "gender": null},
#{"ymin": 0.1195806935429573, "xmin": 0.050002746284008026, "ymax": 0.9922588467597961, "xmax": 0.9625630378723145, "score": 0.9190647006034851, "class_name": "Man", "class_id": 308, "race": "Middle Eastern", "gender": "Male"},
#{"ymin": 0.49269676208496094, "xmin": 0.07834305614233017, "ymax": 0.9805120229721069, "xmax": 0.9698421359062195, "score": 0.7085372805595398, "class_name": "Clothing", "class_id": 433, "race": null, "gender": null},
#{"ymin": 0.45603710412979126, "xmin": 0.020553115755319595, "ymax": 0.9691803455352783, "xmax": 0.3579131066799164, "score": 0.21738770604133606, "class_name": "Human arm", "class_id": 503, "race": null, "gender": null}]}, 
```