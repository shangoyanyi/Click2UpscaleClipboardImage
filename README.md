# Click2UpscaleClipboardImage

**Click2UpscaleClipboardImage** 是一款專為 Windows 使用者設計的輕量工具，透過一鍵執行指令即可將剪貼簿中的圖像放大 4 倍，並回寫至剪貼簿。適合處理螢幕擷取後需要高解析度放大的工作流程。

---

## 🔧 功能特色

- 使用者可透過 **Win + Shift + S** 擷取螢幕畫面
- 執行程式後，自動：
  - 從剪貼簿取得圖片
  - 放大圖片尺寸為原圖 4 倍（bicubic 重採樣）
  - 將放大後圖片回寫至剪貼簿
- 過程中自動紀錄操作 log 至 `%LOCALAPPDATA%\Programs\Logs\Click2UpscaleClipboardImage.log`
- 無 GUI，適合搭配快捷鍵、熱鍵或右鍵選單自動化流程

---

## 📁 專案檔案說明

| 檔案名稱   | 功能說明                            |
|------------|-------------------------------------|
| `4x.py`    | 主程式，負責擷取圖片、放大並回寫   |
| `README.md`| 使用說明文件                         |

---

## ▶️ 使用方式

1. 螢幕畫面擷取：按下 `Win + Shift + S`，擷取任意區域
2. 執行 `4x.py`，即可完成放大並複製至剪貼簿
3. 在其他應用程式中（如繪圖軟體、簡報、LINE）直接貼上使用

---

## 🧠 注意事項

- 若剪貼簿中無圖像，程式會自動顯示提示於 log 中
- 目前固定為 4 倍放大，未提供其他倍率選項
- 僅適用於 Windows 系統，需安裝 Python 與 Pillow、pywin32 套件

---

## 📦 套件需求

請確保已安裝以下 Python 套件：

```bash
pip install pillow pywin32
```

---

## 🧼 Log 紀錄說明

所有操作記錄會儲存至：

```
%LOCALAPPDATA%\Programs\Logs\Click2UpscaleClipboardImage.log
```

記錄內容包含時間戳與成功／失敗訊息，有助於除錯與確認執行狀況。

---

## 📎 授權

MIT — 可自由用於個人與商業用途。
