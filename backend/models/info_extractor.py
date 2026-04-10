import re

def extract_info(text):
    """
    从简历文本中提取关键信息
    :param text: 简历文本
    :return: 提取的关键信息
    """
    info = {
        'basic_info': {
            'name': extract_name(text),
            'phone': extract_phone(text),
            'email': extract_email(text),
            'address': extract_address(text)
        },
        'job_info': {
            'job_intention': extract_job_intention(text),
            'expected_salary': extract_expected_salary(text)
        },
        'background_info': {
            'work_years': extract_work_years(text),
            'education': extract_education(text),
            'projects': extract_projects(text)
        }
    }
    return info

def extract_name(text):
    """提取姓名"""
    # 简单的姓名提取，假设姓名在文本开头
    name_pattern = r'^[\u4e00-\u9fa5]{2,4}'
    match = re.search(name_pattern, text)
    if match:
        return match.group(0)
    return ''

def extract_phone(text):
    """提取电话"""
    phone_pattern = r'1[3-9]\d{9}'
    match = re.search(phone_pattern, text)
    if match:
        return match.group(0)
    return ''

def extract_email(text):
    """提取邮箱"""
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    match = re.search(email_pattern, text)
    if match:
        return match.group(0)
    return ''

def extract_address(text):
    """提取地址"""
    address_pattern = r'地址[:：]?\s*([\u4e00-\u9fa5]+(?:市|区|县|镇|街道|路|巷|弄|号).*?)\s+'
    match = re.search(address_pattern, text)
    if match:
        return match.group(1)
    return ''

def extract_job_intention(text):
    """提取求职意向"""
    job_pattern = r'求职意向[:：]?\s*([^\n]+)'
    match = re.search(job_pattern, text)
    if match:
        return match.group(1)
    return ''

def extract_expected_salary(text):
    """提取期望薪资"""
    salary_pattern = r'期望薪资[:：]?\s*([^\n]+)'
    match = re.search(salary_pattern, text)
    if match:
        return match.group(1)
    return ''

def extract_work_years(text):
    """提取工作年限"""
    work_pattern = r'工作年限[:：]?\s*([^\n]+)'
    match = re.search(work_pattern, text)
    if match:
        return match.group(1)
    return ''

def extract_education(text):
    """提取学历背景"""
    edu_pattern = r'教育背景[:：]?\s*([^\n]+)'
    match = re.search(edu_pattern, text)
    if match:
        return match.group(1)
    return ''

def extract_projects(text):
    """提取项目经历"""
    project_pattern = r'项目经历[:：]?\s*((?:[^\n]+\n)+)'
    match = re.search(project_pattern, text)
    if match:
        return match.group(1)
    return ''