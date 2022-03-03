#列表
bicycles=['trek','cannondale','redline','specialized']
print(bicycles)

#访问列表元素(索引从零开始）
print(bicycles[0])
print(bicycles[1].title())
print(bicycles[2])
print(bicycles[3])
print(bicycles[-1])


message=f"my favorite bicycle is {bicycles[2].title()}."
print(message)

#列表增删改查

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

"""
增
append()增到列表末尾
insert()增到任意位置
"""
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0,'ducati')
print(motorcycles)

"""
删
del 列表[]   删除列表第n位的元素
pop()删除列表末尾元素但可以继续使用它
   last_owned=列表.pop()会显示删除的元素
pop(元素位置）可以删除指定位置的元素
remove('')根据值删除元素
"""
motorcycles=['honda','yamaha','suzuki','ducati','1','2','3','4']
print(motorcycles)

del motorcycles[3]
print(motorcycles)

popped_motorcycles=motorcycles.pop()
print(motorcycles)

last_owned=motorcycles.pop()
print(last_owned)

first_owned=motorcycles.pop(2)
print(motorcycles)

motorcycles.remove('1')
print(motorcycles)

"""
改
列表[元素位置]='修改元素'
"""
motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles[3]='change'
print(motorcycles)

#排序

'''
永久性排序
sort()顺序
sort(reverse=True)倒序
'''

cars=['bmw','audi','toyota','subaru']
print(cars)

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

'''
临时排序（按字母顺序） sorted()
reverse()按顺序排列
再次调用reverse()倒序排列
'''

print(sorted(cars))

cars.reverse()
print(cars)

cars.reverse()
print(cars)

#确定列表长度

print(len(cars))

#python 计算列表元素是从零开始，但第一个列表元素的索引是0


a=['你好','我是','胡苗']
print(sorted(a))
print(len(a))

