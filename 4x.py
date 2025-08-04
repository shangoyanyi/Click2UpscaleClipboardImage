import os
import io
from datetime import datetime
from PIL import ImageGrab, Image
import win32clipboard

# 📁 Log 設定
LOG_DIR = r"C:\Users\user\AppData\Local\Programs\Logs"
LOG_FILE = os.path.join(LOG_DIR, "Click2UpscaleClipboardImage.log")

def write_log(message):
    os.makedirs(LOG_DIR, exist_ok=True)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{now}] {message}\n")

# 🧠 將圖片寫入剪貼簿（DIB格式）
def image_to_clipboard(img: Image.Image):
    try:
        output = io.BytesIO()
        img.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]  # 去掉 BMP header
        output.close()

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()
        write_log("✅ 放大後圖片已複製到剪貼簿")
    except Exception as e:
        write_log(f"⚠️ 複製圖片到剪貼簿時發生錯誤：{str(e)}")

# 📸 主功能：從剪貼簿讀取圖像 → 放大 → 回寫到剪貼簿
def upscale_clipboard_image():
    try:
        img = ImageGrab.grabclipboard()
        if img is None:
            write_log("❌ 剪貼簿中沒有圖像，請先使用 Win + Shift + S 截圖。")
            return

        # 🔍 固定放大倍率 4 倍
        width, height = img.size
        img = img.resize((width * 4, height * 4), resample=Image.BICUBIC)

        image_to_clipboard(img)
    except Exception as e:
        write_log(f"⚠️ 發生錯誤：{str(e)}")

# ▶️ 主程式入口
if __name__ == "__main__":
    upscale_clipboard_image()
