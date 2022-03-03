#第七章 用户输入input()和while循环
#普通输入

message = input("tell me something,and i will repeat it back to you: ")
print(message)

name = input("please enter your name: ")
print(f"hello,{name}")


prompt = "if you tell us who you are,we can personalise the message you see."
prompt +="\nWhat's your first name"
print(f"\nHello,{input(prompt)}")


#使用int()获取数值输入
#是否满足过山车的身高要求
height = input("how tall are you? inches?")
height = int(height)

if height >=120:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou will be able to ride when you are a little older.")

#求模运算符
#判断某数是奇数还是偶数
number = input("\nenter a number,and and i'll tell you if it'seven or odd: ")
number = int(number)

if number % 2 ==0:
    print(f"the number {number} is even")
else:
    print(f"the number {number} is odd")

#while循环
current_number = 1
while current_number<=5:
    print(current_number)
    current_number += 1

#让用户选择何时推出（输入quit退出）
prompt = "\nTell me something,and i will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

#不打印quit
prompt = "\nTell me something,and i will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)


#使用标志（判断整个程序是否处于活动状态）（简化while语句）
prompt = "\nTell me something,and i will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

#使用break退出循环
prompt = "\nplease enter the name of a city you have visited: "
prompt += "\nEnter 'quit' to end the program."
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")


#在循环中使用continue（返回循环开头，并根据条件测试结果决定是否执行循环）
current_number = 0
while current_number< 10:
    current_number +=1
    if current_number %2 == 0:
        continue
    print(current_number)


#避免无限循环（若不运行x+=1，则无限循环）
x = 1
while x <= 5:
    print(x)
    x+=1
    

#使用while循环处理列表和字典
#假设一个列表包含新注册但还未验证的网站用户，需要对用户进行验证，同时将其从未验证用户提取出来，加入已验证用户列表中

unconfirmed_users = ['alice','brian','candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"verifying_user:{current_user.title()}")
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#删除为特定值的所有列表元素
pets = ['dog','cat','goldfish','rabbit','cat','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#使用用户输入来填充字典
#创建一个调查程序，每次提示用户输入应该名和回答，将手机的数据存储在一个字典中
responses = {}
    #设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
    #提示输入被调查者的名字和回答
    name = input("\nWhat's your name?")
    response = input("which mountain would you like to climb someday?")
    #将回答存储在字典中
    responses[name] = response
    #看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        polling_active = False
    #调查结束，显示结果
print("\n---Roll Results---")
for name,response in responses.items():
    print(f"{name} wolde like to climb {response}.")



