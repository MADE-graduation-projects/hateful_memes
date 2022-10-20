# Использование признаков только из картинок, без текста и с текстом через OCR

### Только картинки, без надпиcей и без текста [ноутбук](../CLIP/clip_image_no_caption.ipynb)

Accuracy: 0.582	ROC AUC: 0.618944

### Используем картинки с надписями без текста [ноутбук](../CLIP/clip_image_with_caption.ipynb)

Accuracy: 0.7	ROC AUC: 0.776048

### Картинки без надпией + текст из разметки [ноутбук](../CLIP/clip_image_no_caption_text.ipynb)

Accuracy: 0.684	ROC AUC: 0.748976

### Картинки без надпией + текст который распознали с помощью easyocr [ноутбук](../CLIP/clip_image_no_caption_text_ocr_easyocr.ipynb)

(Сократил длину строки до 50 вместо 77)

Accuracy: 0.584	ROC AUC: 0.59608

### Картинки без надпией + текст который распознали с помощью pytesseract [ноутбук](../CLIP/clip_image_no_caption_text_ocr_pytesseract.ipynb)

Accuracy: 0.652	ROC AUC: 0.69752