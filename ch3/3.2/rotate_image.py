import cv2

# 画像ファイルをカラーで読み込み
src = cv2.imread('yorkie.png', cv2.IMREAD_COLOR)

# 画像原点O(0, 0)を中心にして画像を時計回りに90度回転
# cv2.rotate(src, rotateCode[, dst])
# ROTATE_90_CLOCKWISE           時計回りに90度回転
# ROTATE_180                    時計回りに180度回転
# ROTATE_90_COUNTERCLOCKWISE    反時計回りに90度回転
rotated = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)

# 画像をウィンドウ表示する
cv2.imshow('src', src)
cv2.imshow('rotated', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
