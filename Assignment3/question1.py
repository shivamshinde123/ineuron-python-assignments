

lst = [10,20,30,40,50]

# finding the maximum value from the list
def func(a,b):
    if a > b:
        return a
    else:
        return b
        
a = lst[0]

for i in range(1,len(lst)):
    b = lst[i]
    a = func(a,b)

def myreduce(func,sequence):
    return a

print(myreduce(func,lst))