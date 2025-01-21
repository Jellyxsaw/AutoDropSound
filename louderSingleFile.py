import os
import subprocess
from pydub import AudioSegment
from pydub.utils import which

# 🚀 執行音量增強
input_mp3 = r"ur file path"
output_mp3 = os.path.splitext(input_mp3)[0] + "_loud.mp3"  # 加上 `_loud` 後綴
volume_gain_db = 15 # 自行調整音量


def amplify_mp3(input_path, output_path, volume_gain_db=volume_gain_db):
    """
    放大 MP3 檔案音量，若 MP3 有問題則嘗試修復。
    :param input_path: 原始 MP3 檔案路徑
    :param output_path: 輸出音量增強後的 MP3 檔案
    :param volume_gain_db: 增益分貝數
    """
    # 設定 FFmpeg 路徑
    AudioSegment.converter = which("ffmpeg")
    if not AudioSegment.converter:
        raise Exception("找不到 FFmpeg，請確認已安裝並加入環境變數！")

    temp_fixed_mp3 = "temp_fixed.mp3"
    temp_fixed_wav = "temp_fixed.wav"

    try:
        # 嘗試讀取 MP3 檔案
        audio = AudioSegment.from_file(input_path, format="mp3")
    except Exception:
        print(f"⚠️  MP3 讀取失敗，嘗試修復: {input_path}")

        # 1️⃣ 嘗試強制轉換 MP3
        subprocess.run(["ffmpeg", "-y", "-i", input_path, "-acodec", "libmp3lame", temp_fixed_mp3], check=False)

        if os.path.exists(temp_fixed_mp3):
            try:
                audio = AudioSegment.from_file(temp_fixed_mp3, format="mp3")
                input_path = temp_fixed_mp3  # 更新路徑
            except Exception:
                print(f"⚠️  MP3 修復失敗，改用 WAV 處理")

                # 2️⃣ MP3 仍然無法修復，轉換為 WAV
                subprocess.run(["ffmpeg", "-y", "-i", input_path, "-acodec", "pcm_s16le", temp_fixed_wav], check=False)

                if os.path.exists(temp_fixed_wav):
                    audio = AudioSegment.from_wav(temp_fixed_wav)
                    input_path = temp_fixed_wav  # 更新路徑
                else:
                    print(f"❌ 無法修復 MP3，請確認檔案是否損壞！")
                    return

    # 放大音量
    louder_audio = audio + volume_gain_db

    # 儲存新的 MP3
    louder_audio.export(output_path, format="mp3")
    print(f"✅  音量增強完成: {output_path}")

    # 清理暫存檔案
    if os.path.exists(temp_fixed_mp3):
        os.remove(temp_fixed_mp3)
    if os.path.exists(temp_fixed_wav):
        os.remove(temp_fixed_wav)


amplify_mp3(input_mp3, output_mp3)
