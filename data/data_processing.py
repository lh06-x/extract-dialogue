# %%
import json

def merge_jsonl_files(file1, file2, output_file):
    merged_data = []

    # 读取第一个文件
    with open(file1, 'r', encoding='utf-8') as f1:
        for line in f1:
            try:
                merged_data.append(json.loads(line.strip()))
            except json.JSONDecodeError as e:
                print(f"解析 {file1} 时出错: {e}")

    # 读取第二个文件
    with open(file2, 'r', encoding='utf-8') as f2:
        for line in f2:
            try:
                merged_data.append(json.loads(line.strip()))
            except json.JSONDecodeError as e:
                print(f"解析 {file2} 时出错: {e}")

    # 保存到输出文件
    with open(output_file, 'w', encoding='utf-8') as out:
        for item in merged_data:
            out.write(json.dumps(item, ensure_ascii=False) + '\n')

# 示例调用
file1 = "D:\extract-dialogue\data\converted_zhubajie_lines_up.jsonl"
file2 = "D:\extract-dialogue\data\converted_zhubajie_lines_down.jsonl"
output_file = "d:\\extract-dialogue\\output\\merged_zhubajie_lines.jsonl"
merge_jsonl_files(file1, file2, output_file)


