import re

def calculate_match(resume_info, job_description):
    """
    计算简历与岗位需求的匹配度
    :param resume_info: 简历信息
    :param job_description: 岗位需求描述
    :return: 匹配度评分（0-100）
    """
    # 提取关键词
    job_keywords = extract_keywords(job_description)
    resume_keywords = extract_resume_keywords(resume_info)
    
    # 计算技能匹配率
    skill_match_rate = calculate_skill_match(job_keywords, resume_keywords)
    
    # 计算工作经验相关性
    experience_match = calculate_experience_match(resume_info, job_description)
    
    # 综合评分
    total_score = (skill_match_rate * 0.6) + (experience_match * 0.4)
    
    return round(total_score, 2)

def extract_keywords(text):
    """提取文本中的关键词"""
    # 简单的关键词提取，去除停用词
    stop_words = {'的', '了', '和', '是', '在', '有', '为', '以', '我', '他', '她', '它'}
    words = re.findall(r'\b\w+\b', text.lower())
    keywords = [word for word in words if word not in stop_words and len(word) > 1]
    return set(keywords)

def extract_resume_keywords(resume_info):
    """提取简历中的关键词"""
    resume_text = ''
    # 合并简历中的所有信息
    for category, items in resume_info.items():
        for key, value in items.items():
            resume_text += str(value) + ' '
    return extract_keywords(resume_text)

def calculate_skill_match(job_keywords, resume_keywords):
    """计算技能匹配率"""
    if not job_keywords:
        return 100.0
    # 计算交集
    matched_keywords = job_keywords.intersection(resume_keywords)
    match_rate = (len(matched_keywords) / len(job_keywords)) * 100
    return match_rate

def calculate_experience_match(resume_info, job_description):
    """计算工作经验相关性"""
    # 简单的工作经验匹配
    work_years = resume_info.get('background_info', {}).get('work_years', '')
    if '年' in work_years:
        # 提取工作年限数字
        years_match = re.search(r'(\d+)', work_years)
        if years_match:
            years = int(years_match.group(1))
            # 根据岗位描述中的经验要求进行匹配
            if '3年以上' in job_description and years >= 3:
                return 100.0
            elif '2年以上' in job_description and years >= 2:
                return 100.0
            elif '1年以上' in job_description and years >= 1:
                return 100.0
    return 50.0  # 默认分数