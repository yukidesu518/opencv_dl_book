import numpy as np
import cv2

x = np.uint8([250])
y = np.uint8([5])
# cv2.add()は2つの画像に対してピクセルごとに値を加算する。
# cv2.add(src1, src2, [dst [, mask [, dtype]]])
# src1 : 入力画像1
# src2 : 入力画像2
# dst  : 出力画像
# mask : 処理対象とする画素を指定す津ための8bit深度、1チャンネルのマスク画像
# dtype: 出力画像のデータ型
z = cv2.add(x, y) # 250 + 5 = 255
print(f'z = {z}')
