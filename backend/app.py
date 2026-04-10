from flask import Flask
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# 配置上传文件目录
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB 限制

# 导入路由
from routes.upload import upload_bp
from routes.extract import extract_bp
from routes.match import match_bp

# 注册蓝图
app.register_blueprint(upload_bp, url_prefix='/api')
app.register_blueprint(extract_bp, url_prefix='/api')
app.register_blueprint(match_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)