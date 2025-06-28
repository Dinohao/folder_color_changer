# Folder Color Changer for macOS
# macOS 資料夾顏色變換器

This is a macOS application designed to allow users to easily change the color icons of their folders. It provides an intuitive Graphical User Interface (GUI) and also supports Command Line Interface (CLI) operations, convenient for advanced users or for automation tasks.

這是一個 macOS 應用程式，旨在讓使用者輕鬆地更改資料夾的顏色圖示。它提供了一個直觀的圖形使用者介面 (GUI)，同時也支援命令列介面 (CLI) 操作，方便進階使用者或自動化任務。

## Features
## 功能

*   **Graphical User Interface (GUI)**: Easily select a folder and apply a preset color icon with simple clicks.
    **圖形使用者介面 (GUI)**：透過簡單的點擊操作，選擇資料夾並應用預設顏色圖示。
*   **Command Line Interface (CLI)**: Supports scripting operations, allowing quick changes to folder colors or removal of icons via commands.
    **命令列介面 (CLI)**：支援腳本化操作，可透過指令快速更改資料夾顏色或移除圖示。
*   **Multiple Color Options**: Provides various preset colors (red, orange, yellow, green, blue, purple, gray, white) to choose from.
    **多種顏色選擇**：提供多種預設顏色（紅、橙、黃、綠、藍、紫、灰、白）供選擇。
*   **Automatic Icon Tool Compilation**: Includes a lightweight Swift tool `fileicon` that compiles automatically on first run, used for setting or removing folder icons.
    **自動編譯圖示工具**：內建一個輕量級的 Swift 工具 `fileicon`，首次執行時會自動編譯，用於設定或移除資料夾圖示。
*   **Remove Custom Icon**: Allows restoring a folder to its default icon.
    **移除自訂圖示**：可將資料夾恢復為預設圖示。

## How to Use
## 如何使用

### 1. GUI Application (Recommended)
### 1. GUI 應用程式 (推薦)

This is the simplest and most intuitive way to use the application.
這是最簡單、最直觀的使用方式。

1.  **Activate Virtual Environment**:
    In your terminal, navigate to the project root directory and execute the following command to activate the Python virtual environment:
    **啟用虛擬環境**：
    在終端機中，導航到專案根目錄並執行以下指令來啟用 Python 虛擬環境：
    ```bash
    source venv/bin/activate
    ```

2.  **Launch GUI Application**:
    Execute the following command to start the graphical interface:
    **啟動 GUI 應用程式**：
    執行以下指令來啟動圖形介面：
    ```bash
    python gui_app.py
    ```
    The application window will pop up. You can select a folder, choose a color, and then click "Apply Color" or "Remove Icon" through the window.
    應用程式視窗將會彈出。您可以透過視窗選擇資料夾、選擇顏色，然後點擊「Apply Color」或「Remove Icon」。

### 2. Command Line Interface (CLI)
### 2. 命令列介面 (CLI)

### 3. Packaged Executable
### 3. 打包執行檔

For a standalone application that doesn't require Python or virtual environment setup, you can use the packaged executable.
對於不需要 Python 或虛擬環境設定的獨立應用程式，您可以使用打包好的執行檔。

1.  **Locate the Executable**:
    The executable can be found in the `dist` directory after the application has been built. The path will typically be `dist/Folder Color Changer/Folder Color Changer`.
    **找到執行檔**：
    執行檔在應用程式建置後會位於 `dist` 目錄中。路徑通常是 `dist/Folder Color Changer/Folder Color Changer`。

2.  **Run the Application**:
    You can run the application directly by double-clicking it in Finder, or by executing it from the terminal:
    **執行應用程式**：
    您可以直接在 Finder 中雙擊執行應用程式，或從終端機執行：
    ```bash
    /Users/dino/Desktop/folder_color_changer/dist/Folder\ Color\ Changer/Folder\ Color\ Changer
    ```
    This will launch the GUI application.
    這將會啟動 GUI 應用程式。

---

For users who need automation or prefer command-line operations, the `color-folder.sh` script can be used.
對於需要自動化或偏好命令列操作的使用者，可以使用 `color-folder.sh` 腳本。

1.  **Grant Execute Permissions** (if not already set):
    **給予執行權限** (如果尚未設定)：
    ```bash
    chmod +x color-folder.sh
    ```

2.  **Usage**:
    **使用方式**：
    ```bash
    ./color-folder.sh <folder_path> <color>
    ```
    *   `<folder_path>`: The absolute path to the folder whose icon you want to change.
        `<資料夾路徑>`：您要更改圖示的資料夾的絕對路徑。
    *   `<color>`: The name of the color to apply. Available colors include: `red`, `orange`, `yellow`, `green`, `blue`, `purple`, `gray`, `white`.
        `<顏色>`：要應用的顏色名稱。可用的顏色包括：`red`, `orange`, `yellow`, `green`, `blue`, `purple`, `gray`, `white`。
    *   To remove a custom icon, use `none` as the color:
        若要移除自訂圖示，請使用 `none` 作為顏色：
        ```bash
        ./color-folder.sh <folder_path> none
        ```

    **Examples**:
    **範例**：
    ```bash
    ./color-folder.sh /Users/yourname/Documents/MyProject blue
    ./color-folder.sh /Users/yourname/Downloads none
    ```

## Requirements
## 需求

*   macOS operating system (due to the use of macOS-specific icon setting functions and Swift compiler).
    macOS 作業系統 (因為使用了 macOS 特定的圖示設定功能和 Swift 編譯器)。
*   Python 3.x (for the GUI application).
    Python 3.x (用於 GUI 應用程式)。
*   Xcode Command Line Tools (for compiling the built-in Swift `fileicon` tool). If not installed, you might be prompted to install them when `color-folder.sh` is run for the first time.
    Xcode Command Line Tools (用於編譯內建的 Swift `fileicon` 工具)。如果尚未安裝，當 `color-folder.sh` 首次執行時，可能會提示您安裝。

## Icon Generation
## 圖示生成

The icons for this project are located in the `icons/` directory. These icons are generated using the `generate_icons.sh` script and the `generate_single_icon.py` Python script. If you need to customize icons or regenerate them, you can examine these scripts.

本專案的圖示位於 `icons/` 目錄中。這些圖示是透過 `generate_icons.sh` 腳本和 `generate_single_icon.py` Python 腳本生成的。如果您需要自訂圖示或重新生成，可以研究這些腳本。

## Acknowledgements
## 致謝

*   `fileicon` tool: This project incorporates a lightweight Swift command-line tool for setting and removing file/folder icons on macOS. The inspiration and some code for this tool may come from contributions within the open-source community.
    `fileicon` 工具：此專案內建了一個輕量級的 Swift 命令列工具，用於在 macOS 上設定和移除檔案/資料夾圖示。這個工具的靈感和部分程式碼可能來自於開源社群的貢獻。
