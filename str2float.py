'''
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
'''
from functools import reduce

def str2float(s):
    # 检测s中是否含有.  （是否为浮点） 包含返回字符串开始索引值i，否则抛出异常
    i = s.index('.')
    # 取出s中除小数点外的其他字符
    s1 = s[:i] + s[i+1:]
    '''
        map(char2num,s1): 将s1中的字符替换成整形
        reduce(fn,map(char2num,s1))： 将s1替换为整形数字，比如 s1 = [1,2,3,4,5,6]  reduce后为 123456  
        (10**(len(s)-i-1)： len(s)-i-1计算出小数点后位数，用reduce返回值除以10的(len(s)-i-1次方)   **为python中的幂运算
    '''
    return reduce(fn,map(char2num,s1))/(10**(len(s)-i-1))


def char2num(s):
    digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':'.'}
    return digits[s]

def fn(x,y):
    return x * 10 + y

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) == 0.0:
    print('测试成功!')
else:
    print('测试失败!')