from flask import Blueprint, request, jsonify
import hashlib
from models.matcher import calculate_match
from utils.cache import get_cache, set_cache

match_bp = Blueprint('match', __name__)

@match_bp.route('/match', methods=['POST'])
def match_resume():
    data = request.get_json()
    if not data or 'resume_info' not in data or 'job_description' not in data:
        return jsonify({'error': 'Resume info and job description are required'}), 400
    
    try:
        resume_info = data['resume_info']
        job_description = data['job_description']
        
        # 生成缓存键
        cache_key = f"match:{hashlib.md5(str(resume_info).encode() + job_description.encode()).hexdigest()}"
        # 检查缓存
        cached_score = get_cache(cache_key)
        if cached_score is not None:
            return jsonify({'message': 'Match calculated successfully (from cache)', 'score': cached_score}), 200
        
        # 计算匹配度
        match_score = calculate_match(resume_info, job_description)
        # 设置缓存
        set_cache(cache_key, match_score)
        return jsonify({'message': 'Match calculated successfully', 'score': match_score}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500