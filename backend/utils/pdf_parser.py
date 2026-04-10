import PyPDF2
import re

def parse_pdf(filepath):
    """
    解析PDF文件，提取文本内容
    :param filepath: PDF文件路径
    :return: 提取的文本内容
    """
    text = ""
    try:
        with open(filepath, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            # 遍历所有页面
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                page_text = page.extract_text()
                if page_text:
                    text += page_text
        # 清洗文本
        text = clean_text(text)
        return text
    except Exception as e:
        raise Exception(f"PDF解析失败: {str(e)}")

def clean_text(text):
    """
    清洗文本，去除冗余字符和空白
    :param text: 原始文本
    :return: 清洗后的文本
    """
    # 去除多余的空白字符
    text = re.sub(r'\s+', ' ', text)
    # 去除特殊字符
    text = re.sub(r'[\x00-\x1f\x7f]', '', text)
    return text.strip()