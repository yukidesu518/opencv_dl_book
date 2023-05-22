# 5.1

| スクリプトファイル名  | 概要                              | 
| --------------------- | --------------------------------- | 
| load_movie.py         | 動画を読み込んで表示するサンプル  | 
| movie.py              | 動画を読み込んで表示するサンプル2 | 
| load_frames.py        | 連番画像を動画として扱うサンプル  | 
| movieloader.py        | 高速に動画を読み込むサンプル      | 


## 静止画を読み込む
```python:静止画を読み込む
cv2.imread(filename[, flags])
```
| flags                | 説明                                     |
| -------------------- | -------------------------------------- |
| cv2.IMREADCOLOR      | BGRの3チャンネルの画像として読み込む                   |
| cv2.IMREAD_GRAYSCALE | グレースケールとして読み込む。フルカラーの画像であってもグレースケールになる |
| cv2.IMREAD_UNCHANGED | 画像をそのまま読み込む。透過度情報も読み込む。何チャンネルの画像が読み込まれたのかはベット調べる必要がある                                       |

## 動画の読込
```python:動画の読込
cv2.VideoCapture()
cv2.VideoCapture(filename[, apiPreference])
cv2.VideoCapture(index[, apiPreference])
```

| 引数            | 説明                                                             |
| ------------- | -------------------------------------------------------------- |
| filename      | 読み込む動画のファイルパス（動画ファイルから読み込みたいとき）                                |
| index         | カメラID（USBカメラなどから読み込みたいとき）                                      |
| apiPreference | OpenCVのバックエンドで、どのAPIを利用するか（デフォルトはcv2.CAP_ANYで、自動的に最適なものが選択される） |
| 戻り値           | VideoCaptureオブジェクトが返される                                        |

## 静止画の書き込み(imwrite)
```python:静止画の書き込み(imwrite)
cv2.imwrite(filename, img[, params])
```

| 引数       | 説明         |
| -------- | ---------- |
| filename | 出力画像のファイル名 |
| img      | 出力する画像     |
| params   | 出力フォーマットに応じて指定できるパラメータ           |

## 動画の書き込み(VideoWriter)

```python:動画の書き込み(VideoWriter)
cv2.VideoWriter(filename, fourcc, fps, frameSize[, isColor])
```

| 引数       | 説明         |
| -------- | ---------- |
| filename | 出力動画のファイル名 |
| fourcc   | コーデック      |
| fps      | フレームレート    |
| isColor  | Trueならカラー、Falseならグレースケールで出力           |