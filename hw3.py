print('''
有獎或受罰，輸入數學和英文成績，2科都90分以上輸出有獎品，
如果2科都不及格下輸出要處罰，其中一科不及格輸出再加油。
''')
scoreone=input('please enter score1--')
scoretwo=input('please enter score2--')
scoreone=int(scoreone)
scoretwo=int(scoretwo)
if scoreone >=90 and scoretwo >=90:
    print('有獎品')
elif scoreone <60 and scoretwo <60:
    print('要處罰')
else:
    print('再加油')
x=input ('123')
print('x')

