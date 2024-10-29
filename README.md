# 树莓派 OCR 内容对比工具

本项目使用树莓派与 Tesseract OCR 实现内容对比功能，提供一个 Web 端和一个 GUI 端的用户界面。项目使用 Python 语言开发，支持图像文字识别与内容对比，可用于图像中的文字抽取和文字内容的差异对比。

## 功能

- **OCR 文字识别**：使用 Tesseract OCR 识别图像中的文字。
- **内容对比**：通过对比不同图像的文字内容，识别出差异。
- **Web 界面**：通过 Flask 实现一个简单的 Web 端操作界面。
- **GUI 界面**：使用 Tkinter 提供一个直观的桌面 GUI 操作界面。

## 环境要求

- 树莓派设备（推荐树莓派 4 或更高版本）
- 安装 Python 3.x
- 安装 Tesseract OCR
- 依赖库：Flask、Tkinter、Pillow

## 安装

1. **安装 Tesseract OCR**
   ```bash
   sudo apt update
   sudo apt install tesseract-ocr
   ```
2. **安装 Python 依赖**
   ```bash
   pip install Flask Pillow
   ```

## 运行

## Web 端

1. **进入项目目录。**
   ```bash
   cd <项目目录>
   ```
2. **启动 Flask 服务**
   ```bash
   nohup python3 main.py &
   ```
3. **在浏览器中打开 http://<树莓派 IP>:5000。**

## GUI 端

1. **进入项目目录。**
   ```bash
   cd <项目目录>
   ```
2. **运行 GUI 程序。**
   ```bash
   nohup python3 app.py &
   ```

## 文件结构

```
.
├── README.md           # 项目说明文档
├── web/amin.py         # Web 界面主程序
└── client/app.py       # GUI 界面主程序
```

## 使用说明

## Web 端

1. **上传图片进行 OCR 识别。**
2. **对比两张图片中的文字内容。**
3. **查看差异化对比结果。**

## GUI 端

1. **通过文件选择框选择图像文件。**
2. **点击“开始识别”以识别文字并进行对比。**
3. **在 GUI 界面中查看对比结果。**

## 使用许可

[MIT](https://opensource.org/licenses/MIT) © liujl
