import json
import tkinter as tk
from tkinter import filedialog

# 读取json文件
def process_json(file_path):
    # 打开并加载JSON文件
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    found_watermark = False
    if 'layers' in data:
        original_length = len(data['layers'])
        data['layers'] = [layer for layer in data['layers'] if layer.get('ind') != 12345679]
        new_length = len(data['layers'])
        
        if original_length != new_length:
            found_watermark = True
            print(f"找到并删除了 {original_length - new_length} 个水印图层 (ind=12345679)")
        else:
            print("未找到水印图层 (ind=12345679)")

    # 返回处理后的数据
    return data

# 写入新的json文件
def write_json(output_file_path, data, compress=True):
    with open(output_file_path, 'w', encoding='utf-8') as f:
        if compress:
            # 压缩模式：无缩进，无空格
            json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
            print("文件已压缩保存")
        else:
            # 格式化模式：带缩进
            json.dump(data, f, indent=4, ensure_ascii=False)
            print("文件已格式化保存")

# 弹出文件选择对话框
def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    file_path = filedialog.askopenfilename(title="选择输入的 JSON 文件", filetypes=[("JSON files", "*.json")])
    return file_path

# 弹出保存文件对话框
def save_file_dialog():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    save_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")], title="选择保存位置")
    return save_path

# 主程序
def main():
    # 选择输入文件
    input_file_path = open_file_dialog()
    if not input_file_path:
        print("未选择输入文件，程序结束")
        return

    print(f"正在处理文件: {input_file_path}")
    # 处理json文件
    processed_data = process_json(input_file_path)

    # 选择保存文件
    output_file_path = save_file_dialog()
    if not output_file_path:
        print("未选择保存位置，程序结束")
        return

    # 让用户选择是否压缩
    root = tk.Tk()
    root.withdraw()
    compress = tk.messagebox.askyesno("压缩选项", "是否要压缩JSON文件？")
    
    # 输出处理后的数据到文件
    write_json(output_file_path, processed_data, compress)
    print(f"处理后的json文件已保存到 {output_file_path}")

# 启动程序
if __name__ == "__main__":
    main()
