import numpy as np
import cv2

# 画像ファイルをカラーで読み込み
src1 = cv2.imread('yorkie.png', cv2.IMREAD_COLOR)

# マスク画像を生成する
height, width, channels = src1.shape[:3]
src2 = np.zeros((height, width, channels), np.uint8)
# バウンディングボックス（オブジェクトの周囲を囲む矩形の境界線）を描画する
cv2.rectangle(src2, (150, 135), (290, 315), (255, 255, 255), thickness=-1)

# ピクセルごとにAND演算を行う
# 2つの画像に対してピクセルごとにAND演算を行う
# cv2.bitwise_and(src1, src2[, dst[, mask]])
dst = cv2.bitwise_and(src1, src2)

# 画像をウィンドウ表示する
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
