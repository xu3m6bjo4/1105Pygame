import random
number = 0
for i in range(100):
    number = random.randint(1,20)
    print("終極密碼為:" + str(number))

#print(number)
count = 0
while True:
    guess = input("請輸入終極密碼:")
    if int(guess) == number:
        print("猜對了!!!")
        break
    else:
        print("第" + str(count + 1) + "次猜錯了")
    count = count + 1
    if count == 5:
        break