# AI 赋能的智能简历分析系统

## 项目背景
在招聘流程中，快速筛选和分析大量简历是一项耗时的工作。本项目旨在构建一个后端服务，能够自动解析上传的简历（PDF 格式），提取关键信息，并利用 AI 模型对简历进行评分和关键词匹配，帮助招聘者快速筛选候选人。

## 技术栈
- **后端**：Python, Flask
- **前端**：HTML, CSS, JavaScript
- **PDF解析**：PyPDF2
- **缓存**：Redis
- **部署**：阿里云 Serverless（函数计算 FC）

## 项目结构
```
resume/
├── backend/           # 后端服务
│   ├── app.py         # Flask应用主文件
│   ├── requirements.txt  # 依赖包
│   ├── routes/        # API路由
│   │   ├── __init__.py
│   │   ├── upload.py  # 简历上传
│   │   ├── extract.py # 信息提取
│   │   └── match.py   # 匹配度计算
│   ├── utils/         # 工具函数
│   │   ├── pdf_parser.py  # PDF解析
│   │   └── cache.py       # 缓存机制
│   └── models/        # 模型
│       ├── info_extractor.py  # 信息提取模型
│       └── matcher.py         # 匹配度计算模型
├── frontend/          # 前端页面
│   └── index.html     # 主页面
└── README.md          # 项目说明
```

## 功能模块

### 1. 简历上传与解析
- 支持上传单个 PDF 格式的简历文件
- 解析 PDF 内容，提取文本信息（兼容多页简历）
- 对提取文本进行清洗和结构化处理

### 2. 关键信息提取
- 基本信息：姓名、电话、邮箱、地址
- 求职信息：求职意向、期望薪资
- 背景信息：工作年限、学历背景、项目经历

### 3. 简历评分与匹配
- 接收招聘岗位的需求描述
- 对岗位需求进行关键词提取和分析
- 将解析后的简历信息与岗位需求进行匹配，计算匹配度评分

### 4. 结果返回与缓存
- 以 JSON 格式结构化返回解析结果、关键信息和匹配度评分
- 实现缓存机制（Redis），对已解析和评分的简历进行缓存，避免重复计算

### 5. 前端页面
- 简洁可用的交互页面
- 支持简历上传、解析结果展示和匹配度计算

## 快速开始

### 后端服务
1. 进入backend目录
2. 安装依赖：`pip install -r requirements.txt`
3. 启动服务：`python app.py`
4. 服务将在 http://localhost:5000 运行

### 前端页面
1. 直接打开 frontend/index.html 文件
2. 或部署到 GitHub Pages：
   - 创建一个 GitHub 仓库
   - 将 frontend 目录下的文件推送到仓库
   - 在仓库设置中启用 GitHub Pages

## API 接口

### 1. 上传简历
- **URL**：/api/upload
- **方法**：POST
- **参数**：form-data，key为file，值为PDF文件
- **返回**：JSON格式，包含上传结果和文件名

### 2. 提取信息
- **URL**：/api/extract
- **方法**：POST
- **参数**：JSON格式，包含filename字段
- **返回**：JSON格式，包含提取的简历信息

### 3. 计算匹配度
- **URL**：/api/match
- **方法**：POST
- **参数**：JSON格式，包含resume_info和job_description字段
- **返回**：JSON格式，包含匹配度评分

## 部署到阿里云 Serverless
1. 创建函数计算服务
2. 配置函数入口为 `app.app`
3. 上传依赖包和代码
4. 配置API网关

## 注意事项
- 确保安装了所有依赖包
- 如需使用缓存功能，请确保Redis服务可用
- 前端页面默认调用本地后端服务，部署后需要修改API地址

## 未来优化方向
- 接入更强大的AI模型，提高信息提取和匹配度计算的准确性
- 增加多语言支持
- 优化PDF解析性能，支持更多格式的简历
- 增加用户认证和权限管理