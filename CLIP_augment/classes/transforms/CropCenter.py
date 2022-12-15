class CropCenter(object):
    def __init__(self, size):
        self.size = size

    def __call__(self, sample):
        img = sample
        h, w, _ = img.shape
        margin_h = (h - self.size) // 2
        margin_w = (w - self.size) // 2
        sample = img[margin_h:margin_h + self.size, margin_w:margin_w + self.size]
      
        return sample