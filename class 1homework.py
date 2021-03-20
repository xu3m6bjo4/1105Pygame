import random
number = 0
er = int(input("遊玩人數"))

#for i in range(100):
number = random.randint(1,20 * er)
   # print("終極密碼為:" + str(number))

#print(number)
ty = 20 * er
print("範圍是1~" + str(ty))

rt = 1
count = 0
while True:
    guess = input("請輸入終極密碼:")
    if int(guess) == number:
        print("猜對了!!!")
        break
    else:
        print("第" + str(count + 1) + "次猜錯了")
    count = count + 1
    if rt == er:
                rt = 0
    if count == 5 * er:
        print("次數猜完了")
        break
    if rt < er:
        if er > 2:
            print("換第" + str(rt + 1) + "個人玩")
            rt = rt + 1
            
            
  