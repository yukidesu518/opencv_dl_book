import os
import queue
import threading

import cv2

# シングルスレッドのコードだと重い処理をしている間は動画のでコードが行われず、
# cap.read()が呼ばれた時にはじめて１フレームを読み込むため遅くなる。
# それを解決するため、別プロセスでcap.read()を走らせるプログラム

class MovieLoader:
    def __init__(self, src_path, max_queue_size=256):
        # src_pathが文字列でないまたは、指定されたパスが存在しない場合にエラーを送出
        if type(src_path) == str and (not os.path.exists(src_path)):
            raise FileNotFoundError(f'No such file {src_path}')

        # 動画の読込
        self.video = cv2.VideoCapture(src_path)
        # 繰り返し変数
        self.stopped = False
        # 一定の順番で複数のデータの挿入、取り出しが行えるライブラリ
        self._q = queue.Queue(maxsize=max_queue_size)

        # pythonの標準ライブラリ
        # 新しいスレッドを作成する：指定した関数が別のスレッド（非同期）で実行される
        # daemonはデーモンスレッドとしてスレッドを実行するかどうかを制御するパラメータ
        # デーモンスレッドは、メインスレッドが終了した場合に自動的に終了する
        self._thread = threading.Thread(target=self.update, daemon=True)
        self._thread.start()


    # 非同期で実行する関数
    def update(self):
        while True:
            # 動画の最後に達した場合はbreak
            if self.stopped:
                break

            # 正常に読み込めていない場合はbreak
            if not self.video.isOpened():
                break

            # 今のフレーム数が総フレーム数に達するかつ、総フレーム数が0以上でbreak
            if self.pos_frames >= self.frame_count and self.frame_count > 0:
                break

            # キューが満杯でない時に実行
            if not self._q.full():
                # frameに1フレームの画像が格納される
                # okはフレームの読取りが成功したかどうかが格納
                ok, frame = self.video.read()

                # フレームの読取りに失敗または何らかの理由でフレームが読み込めなかった場合にcontinue
                if (not ok) or (frame is None):
                    continue
                else:
                    # 正常に読み込めたらキューにフレームを追加
                    self._q.put(frame)

        self.stopped = True

    # キューにたまっているフレームを1つ取得
    def read(self, block=True, timeout=None):
        return self._q.get(block, timeout)

    # 繰り返し用変数をTrue
    def stop(self):
        self.stopped = True

    # メモリの解放
    def release(self):
        self.stopped = True
        self.video.release()

    # 正常に読み込めているかを判定
    def isOpened(self):
        return self.video.isOpened()

    # 指定した動画のプロパティを取得
    def get(self, key):
        return self.video.get(key)

    # カメラの設定を変更
    def set(self, key, value):
        return self.video.set(key, value)

    # 動画のwidthを取得
    @property
    def frame_width(self):
        return int(self.get(cv2.CAP_PROP_FRAME_WIDTH))

    # 動画のheightを取得
    @property
    def frame_height(self):
        return int(self.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 総フレーム数を取得
    @property
    def frame_count(self):
        return self.get(cv2.CAP_PROP_FRAME_COUNT)

    # FPSを取得
    @property
    def fps(self):
        return self.get(cv2.CAP_PROP_FPS)

    # 動画の現在の経過時間[ミリ秒]を取得
    @property
    def pos_msec(self):
        return self.get(cv2.CAP_PROP_POS_MSEC)

    # 動画の現在のフレームを取得
    @property
    def pos_frames(self):
        return self.get(cv2.CAP_PROP_POS_FRAMES)


if __name__ == '__main__':

    cap = MovieLoader('test.mp4')
    #cap = MovieLoader(0) # Webカメラからの読み取り

    # cap.stoppedがTrueの間繰り返す（動画のフレーム数分）
    while not cap.stopped:
        # キューにたまっているフレームを1つ取得
        frame = cap.read(timeout=1)

        # フレーム数をテキストで表示
        cv2.putText(frame,
                f'{int(cap.pos_frames)}/{int(cap.frame_count)}',
                (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.0,
                (0, 0, 255),
                thickness=2)

        # 表示
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == 27: # ESCキーで終了
            break

