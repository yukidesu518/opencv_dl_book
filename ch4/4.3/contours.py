import cv2
import matplotlib.pyplot as plt

img_bgr = cv2.imread('bolts.jpg')
img_bgr = cv2.resize(img_bgr, (500, 375))

# グレイスケールに変換する
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# 二値化(findContoursに渡すために必要です)
ret,img_bin = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)

# 輪郭を抽出する
# cv 2. findContours( image, mode, method[, contours[, hierarchy[, offset]]] )
#   引数 
#       image： 入力画像 
#       mode： 後述する輪郭抽出モード 
#       method： 輪郭の近似方法 
#       contours： 抽出された輪郭が格納される
#       hierarchy： 領域の親子関係が格納される
#       offset： 出力の輪郭点に加算する座標。例えば(5,10)と指定すると、出力される座標のX座標に+5、Y座標に+10が加算される
# contoursには個々の輪郭の形状(座標のリスト)が、
# hierarchyには輪郭の階層情報(親子関係)が入ります

contours, hierarchy = cv2.findContours(img_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# ノイズを取り除くために面積が一定以上の領域のみを残し残りを削除する
contours = list(filter(lambda x:cv2.contourArea(x) > 1000, contours))

# 領域の描画
result_img = cv2.drawContours(img_bgr.copy(), contours, -1, (0, 255, 0), 5)

# 個々の領域を囲む四角形(外接する矩形)を描画する
for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    result_img = cv2.rectangle(result_img, (x,y), (x+w,y+h), (255, 0, 0), 4)

titles = ['Input Image', 'Grayscale', 'cv2.threshold', 'Result']
images = [img_bgr, img_gray, img_bin, result_img]

fig = plt.figure(figsize=(24,6))

for index, (title, img) in enumerate(zip(titles, images)):
    ax = fig.add_subplot(1,len(images),index+1)
    ax.title.set_text(title)
    ax.imshow(img, 'gray')
    ax.axis('off')
plt.show()

