import numpy as np
import cv2

img1 = np.array([[1, 2, 3, 4, 5]])
img2 = np.array([[5, 4, 3, 2, 1]])

# ピクセルごとに差分の絶対値を計算する
# cv2.absdiff(src1, src2[, dst])
diff = cv2.absdiff(img1, img2)

# abs(1-5) = 4
# abs(2-4) = 2
# abs(3-3) = 0
# abs(4-2) = 2
# abs(5-1) = 4

print(diff)
