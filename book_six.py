#字典是一系列键值对，每个键都与一个值相关联，可以使用键来访问相关联的值
#一个简单的字典
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])


alien_0 = {'color':'green','points':5}
new_points = alien_0['points']
print(f"you just earned {new_points} points!")

#添加键值对
alien_0 = {'color':'green','points':5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


#修改字典中的值
alien_0 = {'color':'green','points':5}
alien_0['color'] = 'red'
print (alien_0)

#删除键值对
alien_0 = {'color':'green','points':5}
del alien_0['color']
print (alien_0)

#由类似对象组成的字典
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'java'
    }
print(favorite_languages)
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

#遍历字典中的所有键值对
for name,language in favorite_languages.items():
    print (f"{name.title()}'s favorite language is {language.title()}")


user_0={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
    }

for key,value in user_0.items():
    print(f"Key:{key}")
    print(f"Value:{value}")


#遍历字典中的所有键
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'java'
    }
for name in favorite_languages.keys():
    print(name.title())
for name in favorite_languages:
    print(name.title())

friends = ['phil','sarah']
for name in favorite_languages:
    print(f"Hi!{name}")
    if name in friends:
        print(f"{name}'s favorite language is {favorite_languages[name]}")

#按特定顺序遍历字典中的所有键
#sorted() 按字母顺序遍历
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'java'
    }
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()},thank you for taking the poll")

#遍历字典中的所有值
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'java'
    }
print("the following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

#剔除值中的重复项 set()
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'java',
    'agela':'python'
    }
print("the following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

#嵌套
    
#字典列表（创建多个外星人）
    
#1笨方法：一个一个创建

alien_0={'color':'green','points':'5'}
alien_1={'color':'red','points':'2'}
alien_2={'color':'blue','points':'7'}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
#2 使用range()创建多个外星人
aliens = []
for alien_number in range(30):
    new_alien = {'color':'green','points':'3'}
    aliens.append(new_alien)
    print(new_alien)

#显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

#显示创建了多少个外星人
print(f"total number of aliens:{len(aliens)}")

#将前三个外星人修改为黄色
for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color'] = 'yellow'
    print(alien)

#在字典中存储列表
#存储披萨的外皮类型和配料列表
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
    }
print(f"you orded a {pizza['crust']}-crust pizza "
      "\nwith the following toppings:")
for topping in pizza['toppings']:
    print("\t"+topping)


#每人喜欢的语言
favorite_languages={
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],}
for name,languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
          print("\t"+language)

#在字典中存储字典
#三位用户的姓，名和居住地
users = { 
    'zhangsan': { 
        'first':'zhang',
        'last':'san',
        'location':'beijing',
        },
    'lisi':{
        'first':'li',
        'last':'si',
        'location':'shenzhen',
        },
    'wangwu':{
        'first':'wang',
        'last':'wu',
        'location':'xian',
        },
    }
for username,user_info in users.items():
    print(f"\nusername:{username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = f"{user_info['location']}"
    print(f"\tFull_name:{full_name.title()}")
    print(f"\tLocation:{location.title()}")

