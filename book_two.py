#第二章 变量和简单数据类型
print("hello,world")

message= "hello,world"
print(message)

#修改字符串大小写
name="hu mIAo"
print(name.title())
print(name.upper())
print(name.lower())

#使用两个变量
first_name="hu"
last_name="miao"

full_name=f"{first_name+last_name}"
print(full_name)

full_name=f"{first_name} {last_name}"
print(full_name)

print(f"Hello,{full_name.title()},nice to see you!")


#使用制表符(\t)来添加空白
print("languages:\nPython\nJAVA\nc++")
print("languages:\n\tPython\n\tJAVA\n\tc++")

"""
使用换行符添加空白
rstrip(删除末尾空白）
lstrip(删除开头空白）
strip(删除所有空白）
"""
favorite_language=" Python "
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

#数的加减乘除

print(2+2)
print(0.2*0.2)
print(int(2/0.2))
print(3.14_1592_5357)

#同时给多个变量赋值
a,b,c=1,2,3
print(a,b,c)


