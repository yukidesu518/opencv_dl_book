import numpy as np
import cv2

img = np.array([[0, 1, 2, 3, 4, 5, 6]])

# 1から5の範囲で値をクリッピングする
# numpy.ndarray.clipの第1引数に最小値、第2引数に最大値を指定する
# 片方だけいていしたい場合は指定しないほうにNoneを設定する
clip1 = img.clip(1, 5)
print(f'clip1 = {clip1}')

# 最大値を5として値をクリッピングする
clip2 = img.clip(None, 5)
print(f'clip2 = {clip2}')
