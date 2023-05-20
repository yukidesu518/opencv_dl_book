import cv2
import numpy as np
from matplotlib import pyplot as plt

# 100*100[px]のカラー画像を生成
width, height = 100, 100
src_img = np.full((width, height, 3), 128, dtype=np.uint8)
cv2.rectangle(src_img, (10,10), (width-10, height-10), (255,255,255), -1) #枠をつける
# 文字を描画する
cv2.putText(src_img, 'CV', (30,60), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 4, cv2.LINE_4)

plt.imshow(src_img, 'gray')
plt.show()


# アフィン変換
# cv2.warpAffne(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]])
# 引数
#   src: 入力画像
#   M: 2×3の変換行列
#   dsize: 出力画像のサイズ
#   flags: 補間方法（デフォルトはINTER_LINEAR)
#   borderMode: 元の画像の領域外をどう処理するか
#   borderValue: 元の画像の領域外を埋める値

# 補間方法の指定
#   cv2.INTER_NEAREST: 最近傍法で補完
#   cv2.INTER_LINEAR: バイリニア補間。周辺の画素から線形補間するイメージ。高速でそこそこの結果
#   cv2.INTER_CUBIC: バイキュービック補間。バイリニアより多くの画素から補間した値を使う
#   cv2.INTER_AREA: 画像を縮小するとモアレと呼ばれる特有の模様が発生することがあるが、これを緩和できる方法
#   cv2.INTER_LANCZOS4: ランチョス法。きれいな結果が得られるが、計算の負荷が高い


#
# 平行移動
# 画像を+x, +y方向に移動する
#
x = 50
y = -10
M_shift = [[1, 0, x],
           [0, 1, y]]
M_shift = np.array(M_shift, dtype=np.float32)
sheer_img = cv2.warpAffine(src_img, M_shift, dsize=(width,height))
plt.imshow(sheer_img, 'gray')
plt.show()

#
# 回転
# 画像をcenterを中心にangle度回転させる
#
angle = 45
# 回転はやや煩雑だが、getRotationMatrix2Dを使うと変換行列を求めてくれる
M_rotate = cv2.getRotationMatrix2D(center=(width//2, height//2), angle=angle, scale=1.0)
rotation_img = cv2.warpAffine(src_img, M_rotate, dsize=(width,height))
plt.imshow(rotation_img, 'gray')
plt.show()

#
# せん断(シアー)
#
a = 0.2
b = 0.0
M_shear = [[1, a, 0],
           [b, 1, 0]]
M_shear = np.array(M_shear, dtype=np.float32)
shear_img = cv2.warpAffine(src_img, M_shear, dsize=(width,height))
plt.imshow(shear_img, 'gray')
plt.show()

