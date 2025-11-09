import json
"""两处需要修改的，一个是角色名字，一个是输入输出路径和文件名"""
"""角色名字在这里修改"""
special_role = ["孙悟空", "大圣", "齐天大圣", "美猴王", "悟空", "假悟空", "真悟空", "悟空、八戒", "悟空、沙僧", "悟空、八戒、沙僧", "两个悟空", ]

def extract_sunwukong_lines(input_file, output_file):
    results = []
    previous_line = None  # 用于存储上一行台词

    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                dialogue = json.loads(line.strip()) # 解析 JSONL 行
                if dialogue.get('role') in special_role:  # 检查角色是否正确
                    if previous_line:
                        results.append({
                            'previous': previous_line,
                            'current': dialogue
                        })
                previous_line = dialogue  # 更新上一行台词
            except json.JSONDecodeError:
                print(f"无法解析行: {line}")

    # 将结果写入输出文件
    with open(output_file, 'w', encoding='utf-8') as file:
        for result in results:
            file.write(json.dumps(result, ensure_ascii=False) + '\n')

import json

def convert_to_instruction_format(input_file, output_file):
    results = []

    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                data = json.loads(line.strip())  # 解析 JSONL 行
                previous_dialogue = data['previous']['dialogue']
                current_dialogue = data['current']['dialogue']
                # 转换为指定格式
                results.append({
                    "instruction": previous_dialogue,
                    "input": "",
                    "output": current_dialogue
                })
            except KeyError as e:
                print(f"缺少关键字段: {e}")
            except json.JSONDecodeError:
                print(f"无法解析行: {line}")

    # 将结果写入输出文件
    with open(output_file, 'w', encoding='utf-8') as file:
        for result in results:
            file.write(json.dumps(result, ensure_ascii=False) + '\n')


# 示例调用
def main():
    """输入路径、输出路径和相应的文件名在这里修改"""
    input_path = "d:\\extract-dialogue\\【西游记剧本】俚雅剧作集三 电视剧卷 上_dialogues_concurrent.jsonl"
    output_path_1 = "d:\\extract-dialogue\\output\\sunwukong_lines_up.jsonl"
    output_path_2 = "d:\\extract-dialogue\\output\\converted_sunwukong_lines_up.jsonl"
    extract_sunwukong_lines(input_path, output_path_1)
    convert_to_instruction_format(output_path_1, output_path_2)

if __name__ == "__main__":
    main()