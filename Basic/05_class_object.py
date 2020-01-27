#   Class: 함수 + 변수의 합
#   Object: Class를 이용해서 만들어 낸 물체 (=instance)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    """
    def say_hello(self):
        print("안녕! 나는 " + self.name)
    """

    def say_hello(self, to_name):
        print("안녕! " + to_name + " 나는 " + self.name)

    def introduce(self):
        print("내 이름은 " + self.name + " 그리고 나는 " + str(self.age) + "살이야.")

"""
wonie = Person("워니")
"""
changjoo = Person("창주", 31)

"""
wonie.say_hello()
changjoo.say_hello()
"""

changjoo.say_hello("워니")
changjoo.introduce()