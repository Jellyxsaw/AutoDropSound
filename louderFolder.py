import os
import subprocess
from pydub import AudioSegment
from pydub.utils import which

# 設定資料夾
input_folder = r"ur folder path"  # Windows
output_folder = r"ur output folder path"  # Windows
volume_gain_db = 15  # 自行調整音量

# 確保輸出資料夾存在
os.makedirs(output_folder, exist_ok=True)

# 設定 FFmpeg 路徑
AudioSegment.converter = which("ffmpeg")
if not AudioSegment.converter:
    raise Exception("找不到 FFmpeg，請確認已安裝並加入環境變數！")



# 處理所有 mp3 檔案
for filename in os.listdir(input_folder):
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, filename)  # 保持原始名稱

    temp_fixed_mp3 = os.path.join(output_folder, "temp_fixed.mp3")
    temp_fixed_wav = os.path.join(output_folder, "temp_fixed.wav")

    try:
        # 嘗試讀取 MP3 檔案
        audio = AudioSegment.from_file(input_path, format="mp3")
    except Exception as e:
        print(f"⚠️  MP3 讀取失敗，嘗試修復: {filename}")

        # 1️⃣ 嘗試強制轉換 MP3
        subprocess.run(["ffmpeg", "-y", "-i", input_path, "-acodec", "libmp3lame", temp_fixed_mp3], check=False)

        if os.path.exists(temp_fixed_mp3):
            try:
                audio = AudioSegment.from_file(temp_fixed_mp3, format="mp3")
                input_path = temp_fixed_mp3  # 更新路徑
            except Exception:
                print(f"⚠️  MP3 修復失敗，改用 WAV 處理: {filename}")

                # 2️⃣ MP3 仍然無法修復，轉換為 WAV
                subprocess.run(["ffmpeg", "-y", "-i", input_path, "-acodec", "pcm_s16le", temp_fixed_wav], check=False)

                if os.path.exists(temp_fixed_wav):
                    audio = AudioSegment.from_wav(temp_fixed_wav)
                    input_path = temp_fixed_wav  # 更新路徑
                else:
                    print(f"❌ 仍然無法修復 MP3，跳過: {filename}")
                    continue

    # 放大音量
    louder_audio = audio + volume_gain_db

    # 儲存新的 MP3 到輸出資料夾
    louder_audio.export(output_path, format="mp3")
    print(f"✅  已處理: {filename} → {output_path}")

    # 清理暫存檔案
    if os.path.exists(temp_fixed_mp3):
        os.remove(temp_fixed_mp3)
    if os.path.exists(temp_fixed_wav):
        os.remove(temp_fixed_wav)

print("🎵 所有 MP3 檔案已處理完成！")
