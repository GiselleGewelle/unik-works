"""
Лабораторная работа №4
"""
# from random import sample
# ls=sample(range(-30,30),10)
# print(ls)
# ls1=[]
# for i in ls:
#     if ls.index(i)%2==0:
#         ls1.append(i)
# print(ls1)

# lerm=[1,20,2,20,3,20]
# for i in lerm:
#     if i==20:
#         lerm.remove(i)
# print(lerm)

# ls2=[]
# for i in ls:
#     if i>0:
#         ls2.append(i)
# print(ls2)
"""
Самостоятельная работа №4
"""
# from random import sample
# ls=sample(range(-5,5),10)
# ls1=[]
# d=0
# for i in range(len(ls)):
#     if ls[i-1]<ls[i]>ls[i+1]:
#         ls1.append(i)
#         d+=1
# print(ls)
# print(d)


# ls4=[1,2,2,2,2,2,3,3,4,5]
# max=ls4[0]
# max1=ls4.count(max)
# for i in ls4:
#     if ls4.count(i)>max1:
#         max=i
#         max1=ls4.count(i)
# print(max)

# list1='4 0 5 0 3 0 0 5'
# list1=list1.split(" ")
# result=[i for i in list1 if i!="0"]
# count_zero=len(list1)-len(result)
# result +=['0' for _ in range(count_zero)]
# print(" ".join(str(result)))