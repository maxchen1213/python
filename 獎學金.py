print('輸入數學和英文成績，2科都90分以上或任一科100分，就可獲得校長提供的獎學金')
x=input('please enter english score--')
v=input('please enter math score--')
x=int(x)
v=int(v)
if x >= 90 and  v >= 90:
    print('有獎學金')
elif x == 100 or v == 100:
    print('有獎學金')
else:
    print('再加油')
    
