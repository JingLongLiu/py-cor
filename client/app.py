import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import pytesseract as ts
from PIL import Image

# 设置语言
lang = 'chi_sim'

# 创建主窗口
root = tk.Tk()
root.title("OCR 图片识别和对比")
root.geometry("800x600")

# 定义全局变量来保存识别结果
text_result1 = ""
text_result2 = ""


def upload_image(text_widget, image_num):
    # 选择图片文件，指定文件类型为常见图片格式
    file_path = filedialog.askopenfilename(
        title="选择图片文件",
        filetypes=[("JPEG Files", "*.jpg"), ("JPEG Files", "*.jpeg"), ("PNG Files", "*.png"), ("BMP Files", "*.bmp"),
                   ("All Files", "*.*")]
    )
    if file_path:
        # 使用 Tesseract 识别图片内容
        img = Image.open(file_path)
        text_result = ts.image_to_string(img, lang=lang)

        # 显示识别结果在指定的文本框中
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, text_result)

        # 更新全局识别结果变量
        if image_num == 1:
            global text_result1
            text_result1 = text_result
        else:
            global text_result2
            text_result2 = text_result


def compare_text():
    if text_result1 == text_result2:
        messagebox.showinfo("比较结果", "内容相同！")
    else:
        # 如果内容不相同，找到不同的部分并展示在提示框中
        differences = find_differences(text_result1, text_result2)
        messagebox.showinfo("比较结果", f"内容不相同！\n不相同的部分:\n{differences}")


def find_differences(text1, text2):
    result = ""
    maxLength = max(len(text1), len(text2))
    for i in range(maxLength):
        char1 = text1[i] if i < len(text1) else ""
        char2 = text2[i] if i < len(text2) else ""
        if char1 != char2:
            result += f"[{char1} / {char2}] "
    return result


# 设置界面布局
frame1 = tk.Frame(root)
frame1.pack(side=tk.LEFT, padx=20, pady=20)

frame2 = tk.Frame(root)
frame2.pack(side=tk.RIGHT, padx=20, pady=20)

# 图片1区域
label1 = tk.Label(frame1, text="图片1")
label1.pack()
text1 = scrolledtext.ScrolledText(frame1, width=40, height=15)
text1.pack()
button1 = tk.Button(frame1, text="上传图片1", command=lambda: upload_image(text1, 1))
button1.pack(pady=10)

# 图片2区域
label2 = tk.Label(frame2, text="图片2")
label2.pack()
text2 = scrolledtext.ScrolledText(frame2, width=40, height=15)
text2.pack()
button2 = tk.Button(frame2, text="上传图片2", command=lambda: upload_image(text2, 2))
button2.pack(pady=10)

# 比较按钮
compare_button = tk.Button(root, text="比较内容", command=compare_text)
compare_button.pack(pady=20)

# 运行主循环
root.mainloop()
