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
![images](images/1.3/01235.png =100x100) -> ![images](images/1.3/01235_2.png =100x100) + ![images](images/1.3/01235.mask.png =100x100)

 4. С помощью DeepFillV2 из модулей mmcv и mmedit удаляем надписи. Результат сохраняется в папку `img_clean`
 
 ![images](images/2/01235.png =100x100)
 
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
## 3. Разделение изображений представленных комиксом на отдельные картинки

С помощью Res2Net Patch Detector делим изображение. Создается файл `split_img_clean_boxes.json`. Файлы сохраняются в папке `split_img_clean`

<picture>
  <img src="https://github.com/MADE-graduation-projects/hateful_memes/blob/task13_data_preprocessing/competitions/HimariO/1_prepare_data/images/3/01576.png"  width="50" height="50">
</picture> -> 
<picture>
  <img src="https://github.com/MADE-graduation-projects/hateful_memes/blob/task13_data_preprocessing/competitions/HimariO/1_prepare_data/images/3/01576.0.png"  width="50" height="50">
</picture> +
<picture>
  <img src="https://github.com/MADE-graduation-projects/hateful_memes/blob/task13_data_preprocessing/competitions/HimariO/1_prepare_data/images/3/01576.1.png"  width="50" height="50">
</picture>