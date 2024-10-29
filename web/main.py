from flask import Flask, render_template, request, jsonify
import pytesseract as ts
from PIL import Image
import os

# 设置语言
lang = 'chi_sim'

app = Flask(__name__)

# 上传文件保存的临时目录
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 确保上传目录存在
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/', methods=['GET'])
def index():
    return render_template("ocr.html")


@app.route('/upload/<int:image_num>', methods=['POST'])
def upload(image_num):
    image_file = request.files.get("image")

    if image_file:
        # 将上传的文件保存到服务器
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
        image_file.save(file_path)

        # 使用 Tesseract 识别图片内容
        img = Image.open(file_path)
        text_result = ts.image_to_string(img, lang=lang)

        # 可选：删除临时文件
        os.remove(file_path)

        # 返回识别结果和文本框 ID 给前端
        return jsonify({"text": text_result, "image_num": image_num})

    return jsonify({"text": "", "image_num": image_num})


if __name__ == '__main__':
    app.run(debug=True)
