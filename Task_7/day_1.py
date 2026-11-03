print('hello python')
print('100+200=', 100 + 200)
print('Please input your name:')
name = input()
print('I love you', name)
print(name)
name1 = input('Please input your name:')
print('hello,', name1)
print('1024*768=', 1024 * 768)
print('\\n\\')
print('\\\n\\')
print('\\\\\\n\\\\')
print('line1\nline2\nline3')
print('line1\\n\nline2')
age = 18
print('18' + '2')
print(age + 2)
print(f'{age:05d}')
print(f'{29 / 30:.3%}')
print(f'{26:#x}')
print(int(-3.9))
print(-7 // 2)
print(f'{2.675:.2f}')
print('向下取整a=', 17 // 5)
print('除b=', 17 / 5)
print('求余数c=', 17 % 5)
print('d=', '3' + '5')
print('e=', int('3') + float('5.0'))
name = input('请输入你的名字：')
age = int(input('请输入你的年龄：'))
print(f'你好，{name}！你今年{age}岁，五年后{int(age) + 5}岁。')
price = float(input('请输入商品单价：'))
quantity = int(input('请输入商品数量：'))
total = price * quantity
print(f'商品总价为：{total:.2f}')
number = int(input('请输入一个表示总秒数的非负整数：'))
hours = number // 3600
minutes = number % 3600 // 60
seconds = number % 60
print(f'现在的时间是：{hours}时{minutes}分{seconds}秒')
print(bool(0))
print(bool(0.0))
print(bool(''))
print(bool('False'))
print(bool('0'))
print(5 == 5.0)
print('5' == 5)
score = 85
if score < 0 or score > 100:
    print('成绩无效')
elif score >= 90:
    print('优秀')
elif score >= 80:
    print('良好')
elif score >= 60:
    print('及格')
else:
    print('不及格')
total = 0
for number in range(1, 21):
    if number % 2 == 0:
        print(number)
    if number % 2 != 0:
        continue
    total += number
print(f'1~20中所有偶数的和为:{total}')
scores = [85, -5, 92, 101, 60, 0, 48]
count = 0
for score in scores:
    if score < 0 or score > 100:
        continue
    if 0 <= score <= 100:
        print(f'有效成绩为：{score}')
        count += 1
print(f'{count}')
numbers = [5, 12, 18, 21, 28, 35]
for number in numbers:
    if number % 7 == 0:
        print(f'第一个能被7整除的数字是:{number}')
        break
else:
    print('没有符合条件的数字')
while True:
    content = input('请输入内容：')
    if content == 'quit':
        break
    if content == '':
        print('内容不能为空')
        continue
    else:
        print(f'{content}')
fruits = ['apple', 'banana', 'orange']
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[-1])
fruits.append(['watermelon', 'peach'])
fruits.append('fig')
print(fruits)
fruits.insert(1, 'grape')
print(fruits)
fruits.extend(['pear', 'lemon', 'lime'])
print(fruits)
fruits.remove('banana')
print(fruits)
removed = fruits.pop(1)
print(removed)
print(fruits)
removed = fruits.pop(2)
print(fruits)
print(removed)
fruits[1] = 'grape'
print(fruits)
print('pear' in fruits)
print(fruits.index('lemon'))
print(fruits.count('apple'))
print(len(fruits))
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[0:5])
print(numbers[1:5])
print(numbers[:3])
print(numbers[2:])
print(numbers[-2:])
print(numbers[::2])
print(numbers[::-1])
print(numbers[:])
part = numbers[0:5:2]
print(part)
result = [number * 2 for number in range(1, 4)]
print(result)
fruits = ['apple', 'banana', 'orange', 'grape']
fruits.append('watermelon')
fruits[1] = 'strawberry'
fruits.remove('orange')
removed = fruits.pop(0)
print(removed)
print(fruits)
print(fruits[:2])
numbers = [1, 2, 3, 4, 5, 6]
tripled_evens = [number * 3 for number in numbers if number % 2 == 0]
print(tripled_evens)
student = {'name': '小王', 'age': 20, 'score': 85}
student['name'] = '小刘'
student['city'] = '北京'
student['score'] = '90'
print(student)
print(student.get('price', '未填写'))
print(student.get('name', '未填写'))
for key, value in student.items():
    print(key, value)
scores = {'小王': 90, '小李': 55, '小张': 76, '小赵': 40}
passed_scores = {name: score for name, score in scores.items() if score >= 60}
print(passed_scores)
point = (10, 20, 30)
print(point[1])
print(point[:2])
x, y, z = point
print(x)
print(y)
print(z)
single = (10,)
print(type(single))
numbers = [1, 2, 2, 3, 4, 4, 5]
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b)
print(a | b)
print(a - b)
print(b - a)
result = set(numbers)
print(type(numbers))
print(type(result))


def greet():
    print('你好！小悦')
    print('欢迎学习python')


print('程序开始')
greet()


def greet(name):
    print(f'你好，{name}!')


greet('小悦')
greet('小哲')


def introduce(name, age):
    print(f'我叫{name}，今年{age}岁。')


introduce('小悦', '18')
introduce(name='小哲', age='20')
introduce('小悦', age=18)


def greet(name, message='你好'):
    print(f'{message},{name}!')


greet('小悦')
greet('小悦', '中午好')


def add(a, b):
    print(a + b)
    return a + b


result = add(6, 7)
print(result)


def check(score):
    if score < 0 or score > 100:
        return '成绩无效'
    return '成绩有效'


print(check(-5))
print(check(85))


def calculate(a, b):
    return (a + b, a - b)


print(calculate(10, 5))
total, difference = calculate(10, 5)
print(total)
print(difference)


def numbers(*args):
    print(args)


numbers(1, 2, 3, 4, 5, 6, 7)


def add(*args):
    total = 0
    for number in args:
        total += number
    return total


print(add(1, 2, 3, 4))


def add_numbers(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(add_numbers(1, 2, 3, 4, 5, 6))


def show_scores(name, *scores):
    print(f'姓名：{name}')
    print(f'成绩：{scores}')


show_scores('小悦', 99, 98, 97)


def show_info(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f'{key},{value}')


show_info(name='小王', age=20, city='北京')
show_info(name='小哲')


def introduce(**kwargs):
    name = kwargs.get('name', '未填写')
    city = kwargs.get('city', '未填写')
    print(f'姓名：{name}')
    print(f'城市：{city}')


introduce(name='小悦')


def demo(*args, **kwargs):
    print(args)
    print(kwargs)


demo(10, 20, name='小王', age=20)


def add_numbers(*numbers):
    return sum(numbers)


numbers = [1, 2, 3, 4, 5, 6]
print(add_numbers(*numbers))


def introduce(name, age):
    print(f'我叫{name}，今年{age}岁')


info = {'name': '小王', 'age': 20}
introduce(**info)


def greet(name, message='你好'):
    print(f'{message},{name}!')


greet('小王')
greet('小李', '早上好')
greet(name='小张', message='晚上好')


def calculate_total(price, quantity):
    total = price * quantity
    return total


print(calculate_total(15, 3))


def add_numbers(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(add_numbers(1, 2, 3, 4, 5))
print(add_numbers(1, 2))
print(add_numbers(1, 2, 3, 4))
print(add_numbers())


def show_info(**info):
    name = info.get('name', '未填写')
    age = info.get('age', '未填写')
    city = info.get('city', '未填写')
    print(f'姓名：{name}')
    print(f'年龄：{age}')
    print(f'城市：{city}')


show_info(name='小王', age=20, city='北京')
show_info(name='小李')
name = '小王'


def change_name():
    name = '小李'
    print(name)


change_name()
print(name)


def add_fruit(items):
    list_copy = items.copy()
    list_copy.append('香蕉')
    return list_copy


fruits = ['苹果']
new_fruits = add_fruit(fruits)
print(fruits)
print(new_fruits)
