# LottieLab Watermark Remover

一个用于移除 Lottie lab JSON 文件中水印图层的 Python 工具。

## 功能特点

- 自动移除 ind=12345679 的水印图层
- 支持文件选择对话框
- 支持文件压缩选项
- 中文界面

## 使用要求

- Python 3.x
- tkinter（Python 标准库）

## 使用方法

1. 运行程序：
```bash
python process.py# Lottie Watermark Remover

一个用于移除 Lottie JSON 文件中水印图层的 Python 工具。

## 功能特点

- 自动移除 ind=12345679 的水印图层
- 支持文件选择对话框
- 支持文件压缩选项
- 中文界面
- 自动检测水印图层并显示处理结果
- 支持UTF-8编码

## 使用要求

- Python 3.x
- tkinter（Python 标准库）
- 操作系统：Windows/MacOS/Linux

## 安装步骤

1. 克隆或下载此项目：
```bash
git clone [repository-url]
cd lottie-watermark-process
```

2. 确保系统已安装Python 3.x

## 使用方法

1. 运行程序：
```bash
python process.py
```

2. 按照提示操作：
   - 点击选择要处理的 Lottie JSON 文件
   - 选择处理后文件的保存位置
   - 在弹出的对话框中选择是否压缩文件
     - 选择"是"：生成压缩版本（文件体积更小）
     - 选择"否"：生成格式化版本（更易读）

## 处理流程

1. 程序会自动扫描JSON文件中的所有图层
2. 识别并删除 ind 值为 12345679 的水印图层
3. 显示处理结果：
   - 是否找到水印图层
   - 删除的图层数量
   - 文件保存状态
   - 是否使用压缩模式

## 注意事项

- 建议在处理前备份原始文件
- 压缩模式特点：
  - 优点：文件体积更小，适合生产环境
  - 缺点：文件可读性差
- 格式化模式特点：
  - 优点：文件结构清晰，易于阅读和编辑
  - 缺点：文件体积较大

## 开发说明

项目文件结构：
```
lottie-watermark-process/
├── README.md
└── process.py
```

## 技术支持

如有问题或建议，请提交 Issue。
