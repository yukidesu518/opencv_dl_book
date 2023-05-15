import sys
import numpy as np
import cv2

# ファイル名
filename = 'output.xml'

# 書き込みモードでファイルを開く
# cv2.FileStorage()
# cv2.FileStorage(filename, flags[, encoding])
# filename : ファイル名

#   filenameの拡張子によって形式が変わる
#   myHugeMatrix.xml.gzのように.gzを付けることで圧縮したファイルを扱うことができる

# flags : ファイル操作モードを示すフラグ
# encoding : ファイルのエンコーディング

# flagsの種類

#   READ            読込処理を表す値
#   WRITE           書き込み処理を表す値
#   Append          追記処理を表す値
#   MEMORY          ソースからのデータ読込、または内部バッファへのデータの書き込みを指定するフラグ
#   FORMAT_MASK     フォーマットフラグのためのマスク
#   FORMAT_AUTO     オートフォーマットを指定するフラグ
#   FORMAT_XML      XMLフォーマットを指定するフラグ
#   FORMAT_YAML     YAMLフォーマットを指定するフラグ
#   FORMAT_JSON     JSONフォーマットを指定するフラグ
#   BASE64          デフォルトだとBase64でrawdataを書き込むフラグ（可能であればWRITE_BASE64を使用した方がよいでしょう）
#   WRITE_BASE64    WRITEとBASE64を両方有向にするフラグ



fs = cv2.FileStorage(filename, cv2.FileStorage_WRITE)

## 以下のような書き方でもよい
## fs = cv2.FileStorage()
## fs.open(filename, cv2.FileStorage_WRITE)

# ファイルのオープンに失敗したらエラーとして終了
if fs.isOpened() is False:
    print('Failed to load XML file.')
    sys.exit(1)

# 書き出したいデータを定義
R = np.eye(3, 3)
T = np.zeros((3, 1))

# 書き出し
fs.write('R_MAT', R)
fs.write('T_MAT', T)

# コメント追記
fs.writeComment('This is comment')

# ファイルのクローズ、バッファの解放
fs.release()
