#!/bin/bash
set -x

# Activate virtual environment
source "$SCRIPT_DIR/venv/bin/activate"

# Install Pillow if not already installed
python3 -m pip install Pillow


# 這個腳本會產生一組彩色的 .icns 圖示檔
# 並將它們儲存在與此腳本相同目錄下的 "icons" 子資料夾中

# 顏色列表 (名稱和對應的十六進位色碼)
COLORS=(
    "red #FF3B30"
    "orange #FF9500"
    "yellow #FFCC00"
    "green #34C759"
    "blue #007AFF"
    "purple #AF52DE"
    "gray #8E8E93"
    "white #FFFFFF"
)

# 找到此腳本所在的目錄
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
ICON_DIR="$SCRIPT_DIR/icons"
BASE_FOLDER_ICON_ICNS="$ICON_DIR/folder.icns" # 使用用戶提供的 folder.icns
BASE_FOLDER_ICON_PNG="/tmp/base_folder_icon.png"
BASE_FOLDER_ALPHA_MASK="/tmp/base_folder_alpha_mask.png"

# 檢查 icons 資料夾是否存在
if [ ! -d "$ICON_DIR" ]; then
    echo "錯誤: 'icons' 資料夾不存在。請先建立它。"
    exit 1
fi

# 檢查用戶提供的 folder.icns 是否存在
if [ ! -f "$BASE_FOLDER_ICON_ICNS" ]; then
    echo "錯誤: 找不到用戶提供的圖示 '$BASE_FOLDER_ICON_ICNS'。"
    echo "請確保您已將 folder.icns 放置在 icons 資料夾中。"
    exit 1
fi

echo "正在準備基礎圖示..."
# 從 .icns 中提取最大的 PNG 版本
sips -s format png "$BASE_FOLDER_ICON_ICNS" --out "$BASE_FOLDER_ICON_PNG" -Z 512

if [ $? -ne 0 ]; then
    echo "錯誤: 無法從 '$BASE_FOLDER_ICON_ICNS' 提取 PNG 圖像。"
    exit 1
fi

# 從基礎 PNG 提取 alpha 通道作為遮罩
magick "$BASE_FOLDER_ICON_PNG" -channel A -separate "$BASE_FOLDER_ALPHA_MASK"

# 將 BASE_FOLDER_ICON_PNG 複製到工作目錄，以便檢查
cp "$BASE_FOLDER_ICON_PNG" "$SCRIPT_DIR/base_folder_icon_for_inspection.png"
cp "$BASE_FOLDER_ALPHA_MASK" "$SCRIPT_DIR/base_folder_alpha_mask_for_inspection.png"

echo "正在產生圖示，請稍候..."

# 為每種顏色產生一個圖示
for color_entry in "${COLORS[@]}"; do
    color_name=$(echo "$color_entry" | awk '{print $1}')
    hex_color=$(echo "$color_entry" | awk '{print $2}')
    
    # 使用 Python 腳本生成帶有顏色和陰影的 PNG
    COLORED_PNG="/tmp/${color_name}_colored.png"
    "$SCRIPT_DIR/venv/bin/python3" "$SCRIPT_DIR/generate_single_icon.py" "$BASE_FOLDER_ICON_PNG" "$hex_color" "$COLORED_PNG"
    
    # 建立一個 iconset 資料夾
    ICONSET_DIR="/tmp/${color_name}.iconset"
    mkdir -p "$ICONSET_DIR"
    
    # 使用 sips 工具來產生 iconset 所需的不同尺寸圖片
    sips -z 16 16     "$COLORED_PNG" --out "$ICONSET_DIR/icon_16x16.png" > /dev/null
    sips -z 32 32     "$COLORED_PNG" --out "$ICONSET_DIR/icon_16x16@2x.png" > /dev/null
    sips -z 32 32     "$COLORED_PNG" --out "$ICONSET_DIR/icon_32x32.png" > /dev/null
    sips -z 64 64     "$COLORED_PNG" --out "$ICONSET_DIR/icon_32x32@2x.png" > /dev/null
    sips -z 128 128   "$COLORED_PNG" --out "$ICONSET_DIR/icon_128x128.png" > /dev/null
    sips -z 256 256   "$COLORED_PNG" --out "$ICONSET_DIR/icon_128x128@2x.png" > /dev/null
    sips -z 256 256   "$COLORED_PNG" --out "$ICONSET_DIR/icon_256x256.png" > /dev/null
    sips -z 512 512   "$COLORED_PNG" --out "$ICONSET_DIR/icon_256x256@2x.png" > /dev/null
    sips -z 512 512   "$COLORED_PNG" --out "$ICONSET_DIR/icon_512x512.png" > /dev/null
    cp "$COLORED_PNG" "$ICONSET_DIR/icon_512x512@2x.png"

    # 使用 iconutil 將 iconset 轉換為 .icns 檔案
    iconutil -c icns "$ICONSET_DIR" -o "$ICON_DIR/${color_name}.icns"
    
    # 清理臨時檔案
    rm -rf "$COLORED_PNG" "$ICONSET_DIR"
    
    echo "已產生 ${color_name}.icns"
done

# 清理基礎 PNG 檔案
rm -f "$BASE_FOLDER_ICON_PNG"

echo "所有圖示已成功產生並儲存於 '$ICON_DIR'！"
