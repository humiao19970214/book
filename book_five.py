#if语句

#1
car='subaru'
print("is car =='subaru'?i predict True")
print(car=='subaru')

print("\nIs car =='audi'?i predict True")
print(car=='audi')


#2
age =19
if age>=18:
    print("\nyou are old enough to vote")


#if...else语句
age =17
if age>=18:
    print("\nyou are old enough to vote")
else:
    print("\nsorry,you are too young to vote")


#if...elif...else语句
'''
4岁以下免费
4~18岁收费5美元
18岁（含）以上收费10美元
'''
#表达1
age=80
if age<4:
    print('your admission coat is $0')
elif age<18:
    print('your admission coat is $5')
else :
    print('your admission coat is $10')


#表达2
age=12
if age<4:
    price=0
if age<18:
    price=5
else:
    price=10
print("your admission coat is $"+str(price)+".")

    
#制作披萨（需遍历条件）
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese'] 
for requested_topping in requested_toppings: 
 print("\nAdding " + requested_topping + ".") 
print("\nFinished making your pizza!")

#如果青椒用完了
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese'] 
for requested_topping in requested_toppings:
    if requested_topping=="green peppers":
        print("\nsorry,we are out of green peppers roght now")
    else:
        print("\nAdding " + requested_topping + ".") 
print("\nFinished making your pizza!")



#确定列表不是空的
requested_toppings = [] 
if requested_toppings: 
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!") 
else:
    print("Are you sure you want a plain pizza?")
 

#使用多个列表（披萨配料加炸薯条）
available_toopings=['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple']
requested_toopings=['mushrooms', 'french fries', 'extra cheese']
for requested_tooping in requested_toopings:
    if requested_tooping in available_toopings:
        print("Adding "+requested_tooping+".")
    else:
        print("sorry,we dont have"+requested_tooping+" right now.")
print("\nFinished making your pizza")





















