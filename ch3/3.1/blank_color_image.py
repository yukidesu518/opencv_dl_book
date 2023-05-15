import numpy as np
import cv2

width = 200
height = 100
channels = 3
value = (255, 0, 255) # 画素値(B=0, G=0, R=255)順番がRGBではないので注意！

# width=200、height=100、3チャンネルとも画素値0で埋めたカラー画像を生成
img1 = np.zeros((height, width, channels), np.uint8)

# width=200、height=100、画素値(B=0, G=0, R=255)で埋めたカラー画像を生成
img2 = np.full((height, width, channels), value, np.uint8)

# 画像をウィンドウ表示する
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
