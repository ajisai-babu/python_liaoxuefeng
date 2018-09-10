
def findMinAndMax(l):
    if len(l) == 0:
        return (None,None)
    else:
        Max = l[0]
        Min = l[0]
        for i in l:
            Max = max(Max,i)
            Min = min(Min,i)

        return (Min,Max)

if findMinAndMax([]) != (None,None):
    print('error')
elif findMinAndMax([7]) !=(7,7):
    print('error')
elif findMinAndMax([7,1]) !=(1,7):
    print('error')            
elif findMinAndMax([7,1,3,9,5]) !=(1,9):
    print('error')
else:
    print('succeeful')
