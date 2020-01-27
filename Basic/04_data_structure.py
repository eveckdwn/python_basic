#   list, tuple, dict

#   list: element가 여러개일때 사용
x = list()
x = [1, 4, 2, 3]
#    0  1  2  3
y = ["hello", "world"]
z = ["hello", 1, 2, 3]

print(x)
print(y)
print(z)

print("x[2]: " + str(x[2]))
#   print(x[4]) #   IndentationError: unexpected indent

#   list 관련 function
num_elements = len(x) # length
print(num_elements)

s = sorted(x)   #   정렬
print(s)

sum = sum(x)    #   숫자로 기록된 변수들의 총합
print(sum)

for n in x:     # list x의 element를 순서대로 반복처리
    print(n)

for c in y:
    print(c)

print(x.index(3)) # element의 위치를 확인
print(y.index("hello"))
#   print(z.index(10))  #   ValueError: 10 is not in list

if "hello" in y:
    print("hello가 있어요")


#   tuple
x = tuple()
y = ()

x = (1,2,3)
y = ('a', 'b', 'c')
z = (1, "hello", "there")

print(x)
print(y)
print(z)
print(x + y)
print('a' in y)
print(z.index(1))

#   tuple과 list의 차이: Assignment(튜플 안의 값을 업데이트 하는 것)
#   list = mutable (가변: 바꿀 수 있는 것) vs tuple = immutable (불변: 바꿀 수 없는 것)
#   x[0] = 10   #TypeError: 'tuple' object does not support item assignment

#   dictionary: key와 value로 존재 (≒ Map)
x = {
    "name" : "워니",
    "age" : 20
}
y = {
    0: "Wonie",
    1: "Hello",
    "age": 20
}

print(x["name"])
print(x["age"])

print(y[0])
print(y[1])
print(y["age"])

print("age" in x)
print("name" in y)

print(y.keys())
print(x.values())

for key in x:
    print("key: " + str(key))
    print("value: " + str(x[key]))

y[0] = "손창주"
print(y)

y["school"] = "서울과학기술대학교"
print(y)

#   Homework
fruit = ["사과", "사과", "바나나", "바나나", "딸기", "키위", "복숭아" , "복숭아", "복숭아"]
#   과일 숫자 세는 프로그램 만들기
print("전체 과일 수: " + str(len(fruit)))

count = dict()

for key in fruit:
    if key in count:    # count 라는 딕셔너리에 "사과"라는 key가 들어있는가?
        count[key] += 1 # 사과의 갯수를 1개 올려줘
    else:
        count[key] = 1  # 그렇지 않으면 값을 1개로 만들어줘

print(count)

