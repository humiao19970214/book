#第九章 类(首字母大写）
#9.1创建和使用类
#9.1.1 创建Dog类（狗有年龄，姓名，会蹲下sit和打滚roll_over）
class Dog:
    def _init_(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        print(f"{self.name} rolled over.")
