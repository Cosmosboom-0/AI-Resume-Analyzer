from flask import Blueprint, request, jsonify
import os
import hashlib
from utils.pdf_parser import parse_pdf
from models.info_extractor import extract_info
from utils.cache import get_cache, set_cache

extract_bp = Blueprint('extract', __name__)

@extract_bp.route('/extract', methods=['POST'])
def extract_info_from_resume():
    data = request.get_json()
    if not data or 'filename' not in data:
        return jsonify({'error': 'Filename is required'}), 400
    
    filename = data['filename']
    filepath = os.path.join(os.getcwd(), 'uploads', filename)
    
    if not os.path.exists(filepath):
        return jsonify({'error': 'File not found'}), 404
    
    # 生成缓存键
    cache_key = f"resume:{filename}:info"
    # 检查缓存
    cached_info = get_cache(cache_key)
    if cached_info:
        return jsonify({'message': 'Information extracted successfully (from cache)', 'data': cached_info}), 200
    
    try:
        # 解析PDF
        text = parse_pdf(filepath)
        # 提取关键信息
        info = extract_info(text)
        # 设置缓存
        set_cache(cache_key, info)
        return jsonify({'message': 'Information extracted successfully', 'data': info}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500