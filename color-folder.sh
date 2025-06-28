#!/bin/bash

# 檢查參數數量
if [ "$#" -ne 2 ]; then
    echo "用法: $0 <資料夾路徑> <顏色>"
    echo "可用顏色: red, orange, yellow, green, blue, purple, gray, none"
    exit 1
fi

FOLDER_PATH="$1"
COLOR_NAME=$(echo "$2" | tr '[:upper:]' '[:lower:]')

# 檢查資料夾是否存在
if [ ! -d "$FOLDER_PATH" ]; then
    echo "錯誤: 資料夾 '$FOLDER_PATH' 不存在。"
    exit 1
fi

# 找到此腳本所在的目錄
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
ICON_DIR="$SCRIPT_DIR/icons"

# --- fileicon 工具 --- #
# 這是一個小型的 Swift command-line tool，可以設定檔案或資料夾的圖示。
# 為了方便，我將它的原始碼直接嵌入到這個腳本中。
# 當腳本第一次執行時，它會自動編譯這個工具。

FILEICON_TOOL="$SCRIPT_DIR/fileicon"


# --- 主要邏輯 --- #

ICON_PATH="$ICON_DIR/${COLOR_NAME}.icns"

# 檢查對應的圖示檔是否存在
if [ ! -f "$ICON_PATH" ]; then
    echo "錯誤: 找不到圖示檔 '$ICON_PATH'。"
    echo "請先執行 ./generate_icons.sh 來產生所有顏色的圖示。"
    exit 1
fi

# 設定圖示
"$FILEICON_TOOL" set "$FOLDER_PATH" "$ICON_PATH"
sleep 1 # Add a short delay
if [ $? -eq 0 ]; then
    echo "成功！已將 '$FOLDER_PATH' 的圖示更換為 $COLOR_NAME。"
else
    echo "錯誤: 設定圖示失敗。"
    exit 1
fi
