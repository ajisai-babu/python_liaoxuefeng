L1 = ['Hello','World',18,'Apple',None]
L2 = []
for i in L1:
    if(isinstance(i,str)):
        L2.append(i)
    else:
        continue


L2 = [s.lower() for s in L2]

print(L2)
if L2 == ['hello','world','apple']:
    print('测试通过')
else:
    print('测试失败')
