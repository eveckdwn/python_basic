def chat1():
    print("철수: 안녕? 넌 몇 살이니?")
    print("영희: 나? 나는 20")

chat1()

def chat2(name1, name2):
    print("%s: 안녕? 넌 몇 살이니?" % name1)
    print("%s: 나? 나는 20" % name2)

chat2("알렉스", "윤하")
chat2("철수", "영희")

def chat3(name1, name2, age):
    print("%s: 안녕? 넌 몇 살이니?" % name1)
    print("%s: 나? 나는 %d" % (name2, age))

chat3("알렉스", "윤하", 20)
chat3("철수", "영희", 30)

"""
a = 1
b = 2
return = a + b
"""
def dsum(a, b):
    result = a + b
    return result

d = dsum(2, 4)
print(d)


#   Homework
#   먼저 이름과 나이를 받아라
#   나이가 10살 미만이면 "안녕" 이라고 말해라
#   나이가 10살에서 20말 사이면 "안녕하세요"라고 말해라
#   그 외에는 "안녕하십니까" 라고 말해라

def sayHello(name, age):
    if age < 10:
        print("안녕, " + name)
    elif age <= 20 and age >= 10:
        print("안녕하세요, " + name)
    else:
        print("안녕하십니까, " + name)

sayHello("창주", 5)
sayHello("수연", 10)
sayHello("최고", 20)