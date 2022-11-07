from itertools import chain

lst_xyz = ['x','y','z']
lst_num = list(range(2,7))
lst_num2 = list(range(2,9))

answer1 = [j*i for j in lst_xyz for i in range(1,5)]

answer2 = [j*i for i in range(1,4) for j in lst_xyz ]

answer3 = list(chain.from_iterable(([lst_num[i]],[lst_num[i+1]],[lst_num[i+2]]) for i in range(3)))

answer4 = list(chain.from_iterable(([[lst_num2[i],lst_num2[i+1],lst_num2[i+2],lst_num2[i+3]]]) for i in range(4)))

answer5 = [(j,i) for i in range(1,4) for j in range(1,4)]

print(answer1)
print(answer2)
print(answer3)
print(answer4)
print(answer5)

