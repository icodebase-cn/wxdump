# wxdump Python 后端

基于 [PyWxDump](https://github.com/xaoyaoo/PyWxDump) 的优化升级版本，提供微信数据获取、解密、分析等功能。

## 🚀 快速开始

### 环境要求

- Python 3.8+
- Windows 10 64位及以上
- 微信电脑版

### 安装方式

#### 方式一：使用 uv（推荐）

```bash
# 安装 uv
pip install uv

# 克隆项目
git clone https://github.com/icodebase-cn/wxdump.git
cd wxdump/py

# 安装依赖
uv sync --index-url https://mirrors.aliyun.com/pypi/simple

# 运行程序
uv run main.py
```

#### 方式二：使用 pip

```bash
# 克隆项目
git clone https://github.com/icodebase-cn/wxdump.git
cd wxdump/py

# 创建虚拟环境
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# 安装依赖
pip install -r requirements.txt

# 运行程序
python main.py
```

#### 方式三：开发模式安装

```bash
# 克隆项目
git clone https://github.com/icodebase-cn/wxdump.git
cd wxdump/py

# 安装为可编辑包
pip install -e .

# 运行程序
wxdump
```

## 📖 使用方法

### 命令行使用

```bash
# 启动API服务（默认行为）
uv run main.py

# 查看帮助信息
uv run main.py -h

# 获取微信信息
uv run main.py info

# 解密微信数据库
uv run main.py decrypt -k <密钥> -i <数据库路径> -o <输出路径>

# 启动Web界面
uv run main.py ui

# 启动API服务（显式指定）
uv run main.py api
```

### 快速启动脚本

#### Windows
```cmd
# 双击运行（启动API服务）
start.bat

# 启动Web界面
start.bat ui

# 获取微信信息
start.bat info
```

#### Linux/Mac
```bash
# 添加执行权限
chmod +x start.sh

# 运行（启动API服务）
./start.sh

# 启动Web界面
./start.sh ui

# 获取微信信息
./start.sh info
```

### 测试安装

```bash
# 运行安装测试
uv run python test_install.py
```

### Python API 使用

```python
from pywxdump import *

# 获取微信信息
wx_info = get_wx_info()

# 解密数据库
result = batch_decrypt(key, db_path, out_path)

# 启动Web服务
start_server()
```

## 🔧 功能特性

### 核心功能
- ✅ 微信信息获取（昵称、账号、手机、邮箱、密钥）
- ✅ 数据库自动解密
- ✅ 聊天记录查看和搜索
- ✅ 多媒体文件管理
- ✅ 数据导出（HTML、CSV、JSON）

### 新增功能
- 🆕 性能优化
- 🆕 更好的错误处理
- 🆕 改进的API接口
- 🆕 增强的数据分析功能

## 📁 项目结构

```
py/
├── main.py                 # 主程序入口
├── pyproject.toml         # 项目配置
├── requirements.txt       # 依赖列表
├── setup.py              # 安装脚本
├── pywxdump/             # 核心模块
│   ├── wx_core/          # 微信核心功能
│   ├── db/               # 数据库处理
│   ├── api/              # API接口
│   ├── analyzer/         # 数据分析
│   └── ui/               # UI相关
├── doc/                  # 文档
├── tests/                # 测试文件
└── wxdump_work/          # 工作目录
```

## 🛠️ 开发

### 开发环境设置

```bash
# 安装开发依赖
uv sync --dev

# 运行测试
uv run pytest

# 代码格式化
uv run black .
uv run isort .

# 类型检查
uv run mypy .
```

### 构建

```bash
# 构建包
uv build

# 安装到系统
uv pip install dist/*.whl
```

## 📋 依赖说明

主要依赖包括：
- `psutil` - 系统进程管理
- `pycryptodomex` - 加密解密
- `pymem` - 内存操作
- `fastapi` - Web框架
- `uvicorn` - ASGI服务器
- `pydantic` - 数据验证

完整依赖列表请查看 `requirements.txt` 或 `pyproject.toml`。

## ⚠️ 注意事项

1. **仅限Windows系统**：目前只支持Windows 10 64位及以上
2. **微信版本**：支持主流微信版本，具体支持情况请查看 `WX_OFFS.json`
3. **权限要求**：需要管理员权限来访问微信进程内存
4. **数据安全**：请妥善保管解密后的数据，避免泄露

## 🐛 问题反馈

如果遇到问题，请：
1. 查看 [FAQ](doc/FAQ.md)
2. 提交 [Issue](https://github.com/icodebase-cn/wxdump/issues)
3. 微信号：qianji_ai

## 📄 许可证

本项目基于 [MIT License](../LICENSE) 开源协议。

## 🙏 致谢

感谢 [@xaoyaoo](https://github.com/xaoyaoo) 的 [PyWxDump](https://github.com/xaoyaoo/PyWxDump) 和 [@baiyajin](https://github.com/baiyajin) 的 [wx-dump-plus](https://github.com/baiyajin/wx-dump-plus) 项目提供的核心功能。