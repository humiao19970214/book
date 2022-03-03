#第四章  操作列表

Magics=['alice','david','carolina']
for magic in Magics:
    print(magic+",that is a good trick")
    print("i can not wait to see your next trick,"+magic+".")
print("Thank you")

#创建数值列表
for value in range(1,6):
 print(value)

numbers=list(range(1,6))
print(numbers)

numbers=list(range(0,50,5))
print(numbers)

#打印 列表数字的平方
#方法1
squares=[]
for value in range(1,6):
    square= value**2
    squares.append(square)
print(squares)

#方法2
squares=[]
for value in range(1,6):
    squares.append(value**2)
print(squares)

#方法3
squares=[value**2 for value in range(1,6)]
print(squares)

#对数字列表进行简单的统计计算

a=[1,2,3,4,5,6,7,8,9]
print(min(a))
print(max(a))
print(sum(a))

#使用列表的一部分
players=['chares','martina','machael','florence','eli']

  #前三个
print(players[0:3])

  #第2~4个
print(players[1:4])

  #从头开始到第四个
print(players[:4])

  #最后三个
print(players[-3:])

#遍历切片
players=['chares','martina','machael','florence','eli']
print('Here are the first three players om my team:')
for player in players[:3]:
    print(player.title())


#复制列表
my_foods=['pizza','dumplings','noodles']

  #1
friend_foods=my_foods[:]
print(my_foods)
print(friend_foods)

  #2
my_foods.append('cannoli')
friend_foods.append('cake')
print(my_foods)
print(friend_foods)

#元组
'''
里面的智不可以呗修改单可以重新赋值；
使用圆括号标识，可使用索引访问；
哪怕只有一个值，也要用都好隔开；
'''
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])


  #遍历元素中的所有值
for dimension in dimensions:
    print(dimension)

  #修改元素变量（重新赋值）
shows=('1','2','3')
for show in shows:
    print(show)
shows=('3','3','3')
for show in shows:
    print(show)


