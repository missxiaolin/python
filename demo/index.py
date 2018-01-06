# mood = True
#
# if mood :
#     print('开心')
# else:
#     print('不开心')

# 循环
# while for
# CONDITION = True
#
# while CONDITION:
#     print('hello word')
#     CONDITION = False

# for 循环

# for x in range(0,10):
#     print('hello')

# class Student():
#     name = 'xiaolin'
# 
#     def __init__(self, name=''):
#         self.name = name
#
#     def getName(self):
#         return self.name
#
#
# student = Student('xiaobei')
# print(student.getName())

from enum import Enum

class Vip(Enum):
    TOKEN = 1

print(Vip.TOKEN.value)


