#   Number
x = 1
y = 2
z = 1.2

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x ** y) # 제곱
print(x % y)  # mod

#   String
a = 'Hello'
b = "안녕"
c = """
안녕하세요.
손창주입니다.
"""
print(a)
print(b)
print(c)

print("안녕" + " 잘 지내니?")

# print("너 혹시 몇 살이니? " + 4) #TypeError: must be str, not int → 같은 타입으로 바꿔줘야함.
print("너 혹시 몇 살이니? " + str(4))

d = 4   #   숫자 타입
e = "4" #   문자열 타입
print(str(d) + e)
print(d + int(e))

#   Boolean
f = True
g = False

if 2 > 1:
    print("Hello")

if 1 > 2:
    print("Bye")

if not 1 > 2:
    print("Oh Yeah")

if 1 > 0 and 2 > 1:
    print("Good")

if 0 > 0 and 2 > 1:
    print("Bad")

if 0 > 0 or 2 > 1:
    print("Or")

h = 3
if h > 5:
    print("False 1")
elif h == 3:
    print("Right")
else:
    print("False 2")

