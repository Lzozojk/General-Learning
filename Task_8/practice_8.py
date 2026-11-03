from pathlib import Path
with open('notes.txt','w',encoding='utf-8') as file:
    file.write('''今天学习 Python 文件操作
我会使用 with open
中文也能正确保存''')
with open('notes.txt','r',encoding='utf-8') as file:
    content = file.read()
    print(content)
with open('notes.txt','a',encoding='utf-8') as file:
    file.write('\n明天学习JSON')
with open('notes.txt','r',encoding='utf-8') as file:
    content = file.read()
    print(content)
    lines = content.splitlines()
    print(len(lines))



folder = Path('Practice') 
print('路径是否存在:', folder.exists())
print('路径是否是文件：' , folder.is_file())
all_folder = folder / 'b.txt'
for file1 in folder.glob('*.md'):
    print(file1)
for file2 in folder.rglob('*.md'):
    print(file2.name , file2)



students = [
    {"name": "小明", "score": 85},
    {"name": "小红", "score": 92},
    {"name": "小刚", "score": 78},
]
import json
with open('scores.json','w',encoding='utf-8') as file:    
    json.dump(students,file,indent=2,ensure_ascii=False)
with open('scores.json','r',encoding='utf-8') as file: 
    data = json.load(file)
    print(data)
scores = [student['score'] for student in students]
print(scores)
total = 0
for score in scores:
    total += score
    average = total / len(scores)
print('平均分：', average)
best_student = students[0]
for student in students:
    if student['score'] > best_student['score']:
        best_student = student
print('最高分学生：',best_student['name'])



file_path = input("请输入文本文件路径：")
try:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("文件不存在")
except PermissionError:
    print("没有读取权限")
except UnicodeDecodeError:
    print("文件编码不符合 UTF-8")
except OSError as error:
    print(f"文件读取失败：{error}")
finally:
    print("本次读取结束")