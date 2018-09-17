'''
回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
'''

def is_palindrome(n):
    s = str(n)
    # 每隔 -1 取出一位 ，如 l=[1,2,3] l[::-1] == [3,2,1]
    return s[::-1] == s
'''
     如果没有把列表n转化为str，会出错
     但是为什么把n转化为字符串后s[::-1] == s会返回True呢？
        例如：     
        >>> l = [33,44,55]
        >>> l[::-1]
        [55, 44, 33]
        >>> l[::-1] == l
        False
        >>> ls=str(l)
        >>> ls
        '[33, 44, 55]'
        >>> ls[::-1]
        ']55 ,44 ,33['
        >>> ls[::-1] == ls
        False
        
        因为 filter()把传入的函数依次作用于每个元素，filter会把range(1,1000)列表中的函数依次传入is_palindrome函数
'''

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

