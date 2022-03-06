print('''
輸入國文 英文 數學成績
三科都90以上 輸出 有獎金
只要一科90以上 輸出 有糖果
只要有一科不及格 輸出 再加油
三科都不及格 輸出 欠揍
其餘 輸出 普通學生
''')
x=input('please enter chinese score')
y=input('please enter english score')
z=input('please enter math score')
x=int(x)
y=int(y)
z=int(z)
if x>=90 and y>=90 and z>=90:
    print('有獎金')
elif x>=90 or y>=90 or z>=90:
    print('有糖果')
elif x< 60 or y<60 or z<60:
    print('再加油')
elif x<60 and y<60 and z<60:
    print('欠揍')
else:
    print('普通學生')
