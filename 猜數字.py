print('程式從1~10隨機選一個數字，在螢幕上要求使用者輸入數字，只能猜一次若猜錯，告知「你猜錯了」。')
import random
x=random.randint(1,10)
k=int(input(' please enter number'))
if k==x:
    print('猜對了')
else:
    print('猜錯了')