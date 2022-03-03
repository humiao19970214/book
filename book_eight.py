
#第八章 函数
#8.1 定义函数（定义一个名为greet_user()的函数）
def greet_user():
    print("hello")
greet_user()

#8.1.1 向函数传递信息
def greet_user(username):
    print(f"hello,{username.title()}!")
greet_user('jesse')

#8.1.2 形参和实参
#8.2 传递实参

#8.2.1 位置实参
def describe_pet(animal_type,pet_name):
    print(f"I have a {animal_type},")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('dog','harry')
describe_pet('cat','willie')

#8.2.2 关键字实参
def describe_pet(animal_type,pet_name):
    print(f"I have a {animal_type},")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type='dog',pet_name='harry')
describe_pet(pet_name='willie',animal_type='cat')

#8.2.3 给实参设置默认值（默认宠物品种为狗）
def describe_pet(pet_name,animal_type='dog'):
    print(f"I have a {animal_type},")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='harry')
describe_pet(pet_name='willie',animal_type='cat')

#8.2.4 等效的函数调用

#describe_pet('willie')
#    =describe_pet(pet_name='willie')
#describe_pet('harry','hamster')
#    =describe_pet(pet_name='harry',animal_type='hamster')
#    =describe_pet(animal_type='hamster',pet_name='harry')

#8.3 返回值
#8.3.1 返回简单值
def get_formatted_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
misician = get_formatted_name('hu','miao')
print(misician)

#8.3.2 让实参变成可选的(给实参设置默认值为空）
def get_formatted_name(first_name,last_name,middle_name=''):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()
misician = get_formatted_name('hu','miao')
print(misician)

#8.3返回字典
def build_person(first_name,last_name):
    person = {'first':first_name,'last':last_name}
    return person
musician = build_person('jimi','hendrix')
print(musician)

#添加存储年龄
def build_person(first_name,last_name,age=None):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person
musician = build_person('hu','miao',age=25)
print(musician)

#8.3.4结合使用函数和while循环

    #无限循环
def build_formatted_name(first_name,last_name):
    full_name = {'first':first_name,'last':last_name}
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    f_name = input("First_name:")
    l_name = input("last_name:")
    formatted_name = get_formatted_name(f_name,l_name)
    print(f"\nHello,{formatted_name}!")
    #定义退出条件
def build_formatted_name(first_name,last_name):
    full_name = {'first':first_name,'last':last_name}
    return full_name
while True:
    print("\nPlease tell me your name:")
    print("Enter'q' at any time to quit")
    f_name = input("First_name:")
    if f_name == 'q':
        break
    l_name = input("last_name:")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print(f"\nHello,{formatted_name}!")

#8.4 传递列表
def greet_users(names):
    for name in names:
        msg = f"hello,{name.title()}!"
        print(msg)
usernames = ['liming','wangli','zhangyu']
greet_users(usernames)

#8.4.1在函数中修改列表
unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"\nPrinting model:{current_design}")
    completed_models.append(current_design)
  #显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


#8.4.2禁止函数修改列表
 #将列表的副本传递给函数
def function_name():
    function_name(list_name[:])
 #切片表示法[:]创建列表的副本，如果不想清空未打印的设计列表，可以调用print_models():
def print_models():
    print_models(unprinted_designs[:],completed_models)

#8.5 传递任意数量的实参（调用形参[*形参名])
def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

#将函数调用print()替换为一个循环
def make_pizza(*toppings):
    print("\nMaking a pizza with the folling toppings:")
    for topping in toppings:
        print(f"{topping}")
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

#8.5.1结合使用位置实参和任意数量实参
def make_pizza(size,*toppings):
    print(f"\nMaking a {size}-inch pizza with the folling toppings:")
    for topping in toppings:
        print(f"{topping}")
make_pizza(1,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

#8.5.2使用任意数量的关键字实参
def build_profile(first,last,**user_info):
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info
user_profile = build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)
                  
#8.6将函数存储在模块中
#8.6.1.导入整合模块 在此目录所在文件夹下面新建应该名为pizza的py文件后import pizza导入即可

import pizza
pizza.make_pizza(2,'ppepperoni')
pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')

#8.6.2.导入特定的函数
#导入模块中的特定函数 from module_name import function_name
#通过逗号分隔函数名，从模块中导入任意数量的函数 from module_name import function_0，funcion_1，function_2
from pizza import make_pizza
pizza.make_pizza(3,'ppepperoni')
pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')

#8.6.3 使用as给函数指定别名 from ...import ... as...
#给make_pizza()指定别名mp()
from pizza import make_pizza as mp
mp(4,'ppepperoni')
mp(12,'mushrooms','green peppers','extra cheese')

#8.6.4使用as给模块指定别名 import...as...
#给pizza指定别名p
import pizza as p
p.make_pizza(5,'ppepperoni')
p.make_pizza(12,'mushrooms','green peppers','extra cheese')

#8.6.5 导入模块中的所有函数
from pizza import *
make_pizza(6,'ppepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')






