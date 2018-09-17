'''
假设我们用一组tuple表示学生名字和成绩：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
请用sorted()对上述列表分别按名字排序：
'''

L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]

def by_name(t):
    return t[0]

L2 = sorted(L,key=by_name)
print(L2)

'''
再按成绩从高到低排序：
'''
L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]


def by_socre(t):
    return t[1]

#L列表传入sorted，是把列表中的元素拆开，依次执行key所指的函数，所以t[0]指的是L中每个tuple的第一个元素，而并非第一个tuple
L2 = sorted(L,key=by_socre)
print(L2)

