#   같은 기능을 여러 번 반복할 때, 어떻게 해야할까?
#   for
for i in range(3):
    print(i)    # i = 0
    print("철수: 안녕 영희야, 뭐해?")
    print("영희: 안녕 철수야, 그냥 있어.")

#   while
i = 0
while i < 3:
    print(i)
    print("철수: 안녕 영희야, 뭐해?")
    print("영희: 안녕 철수야, 그냥 있어.")
    i = i + 1

#break, continue
i = 0
while True:
    print(i)
    print("철수: 안녕 영희야, 뭐해?")
    print("영희: 안녕 철수야, 그냥 있어.")
    i = i + 1

    if i > 2:
        break

i = 0
for i in range(3):
    print(i)
    print("철수: 안녕 영희야, 뭐해?")
    print("영희: 안녕 철수야, 그냥 있어.")

    if i >= 2:
        continue
    print("워니: 안녕 철수와 영희야!")