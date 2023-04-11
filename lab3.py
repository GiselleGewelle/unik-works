"""
Лабораторная работа №3
"""
# ls=[1,4,7,23,-13,0,0]

# print(sum(ls))

# def mul(obj):
#     n = 1
#     for x in obj:
#         n *= x
#     return n
# print(mul(ls))

# print(sum(ls)/len(ls))

# d=0
# for i in ls:
#     if i==0:
#         d+=1
# print(d)

# c=0
# for j in ls:
#     if j<0:
#         c+=1
# print(c)
"""
Самостоятельная работа №3
"""
ls=[[1,20,33,44],[42,21,-12,40,0]]
newls=[]
for i in ls:
    for j in i:
        if j%10==0:
            j=0
        newls.append(j)
print(newls)

ls1=[]
for i in ls:
    for j in i:
        if j>=10 and j <100 or j <=-10 and j>-100:
            ls1.append(j)
print(ls1)


# ls2=[]
# for i in ls:
#     for j in i:
#         des=j%10
#         if j%2==0 and (j-des)%2==0 and j>19 and j>-10:
#             ls2.append(j)
# print(ls2)

# ls3=[]
# d=0
# for i in ls:
#     if len(i)%2!=0:
#         for j in i:
#             if j==0:
#                 ls3.append(j)
#                 d+=1
# print(f" kol-vo 0 v stolbce {d}")

ls4=[]
for i in ls:
    for j in i:
        
        j=abs(j)
        ls4.append(j)
print(ls4)