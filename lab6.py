"""
Лабораторная работа №6
"""

# def delitel(n):
#     ls=[]
#     for i in range(1,n):
#         if n%i==0:
#             ls.append(i)
#     print(ls)
#     return ls
# delitel(100)
#-----------------------------------
# def armstrong(n):
#     des=[]
#     ls=[]
#     c=str(n)
#     c=list(c)
#     for i in c:
#         des.append(int(i))
#     x=len(des)
#     for i in des:
#         ls.append(i**x)
#     print(sum(ls))
#     if sum(ls)==n:
#         print(True)
#     else:
#         print(False)
#     return ls
# armstrong(1634)
#-----------------------------------------
# def chet(a=[]):
#     ls=[]
#     newls=[]
#     for i in a:
#         ls.append(int(i))
#     print(ls)
#     for i in ls:
#         if i %2==0:
#             newls.append(i)
#     print(newls)
#     return newls
# chet(a=[1,2,3,4,5])
"""
Самостоятельная работа №6
"""
# def stroka(a=[]):
#     ls=[]
#     for i in a:
#         if "python".lower() in i:
#             ls.append(i)
#     print(ls)
#     return ls
# stroka(a=["lol","Hello wrold","I like python","python is cool"])
#-----------------------------------------------------------------
# def country(a=[]):
#     ls=[]
#     for i in a:
#         if i[0]=="K":
#             ls.append(i)
#     print(ls)
#     return ls
# country(a=["Kyrgyzstan","Kanada","USA","Moroko","China","Kolumbia"])
#----------------------------------------------------------------------
# def calculate_virus_cells(hours):
#     bact_per_hour = 4 * 60  # количество новых бактерий в час
#     time_to_combine = 25  # минут на объединение 100 бактерий
#     virus_cells = 1  # начальное количество вирусных клеток
#     for i in range(hours):
#         new_bacteria = bact_per_hour * virus_cells
#         virus_cells += new_bacteria // 100
#         virus_cells *= 4 * time_to_combine // 60
#     return virus_cells
# print(calculate_virus_cells(1))


def virus_count(hours: int):
    amount = 1
    bac = 0
    for min in range(hours * 60 + 1):
        if bac >= 100:
            amount += 1
            bac = bac % 100
        bac += 4 * amount
    return amount

print(virus_count(1))