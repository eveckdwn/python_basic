#   inheritance: 상속

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("안녕! " + to_name + " 나는 " + self.name)

    def introduce(self):
        print("내 이름은 " + self.name + " 그리고 나는 " + str(self.age) + "살이야.")


class Police(Person):
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("안녕! " + to_name + " 나는 " + self.name)

    def introduce(self):
        print("내 이름은 " + self.name + " 그리고 나는 " + str(self.age) + "살이야.")
    """
    def arrest(self, to_arrest):
        print("넌 체포됐다, " + to_arrest)

class Programmer(Person):
    def program(self, to_program):
        print("다음엔 뭘 만들지? 아 이걸 만들어야겠다: " + to_program)

changjoo = Person("창주", 31)
jenny = Police("제니", 21)
micheal = Programmer("마이클", 22)

jenny.introduce()
jenny.arrest("창주")

micheal.introduce()
micheal.program("이메일 클라이언트")


"""
function을 가지고 있지 않기 때문에 하기 명령어는 불가능

changjoo.arrest("제니")
changjoo.program("채팅 프로그램")
jenny.program("CTI Module")
micheal.arrest("창주")
"""