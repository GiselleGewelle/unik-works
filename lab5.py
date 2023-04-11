# box1=5
# box2=10
# box3=15
# apple=100
# a=0
# b=0
# c=0
# while apple>25:
#     apple=apple-box3
#     a+=1
#     print(a)
# while apple>10:
#     apple=apple-box2
#     b+=1
#     print(b)
# while apple!=0:
#     apple=apple-box1
#     c+=1
#     print(c)
# print(a,b,c)
#-----------------------------------------------------
# usp={"Samat":100,"Aida":83,"Aruke":87,"Abdusattar":55}
# x=input("Vvedite bal: ")
# x=x.strip()
# x=int(x)
# def ocenka(usp,value):
#     for i,j in usp.items():
#         if j==value:
#             return i
# print(ocenka(usp,x))
#-------------------------------------------------------------
# fish={"Рыбы":{"Речные":"Карась","Озерные":"Сом","Морские":"Селедь"}}
# print(type(fish))
# for i,j in fish.items():
#     print(i)
#     for x,d in j.items():
#         print(x)
#     for x,d in j.items():
#         print(d)
#-----------------------------------------------------------------
"""
Самостоятельнай работа №5
"""
# cort=(3,"s",1,5,"s")
# print(type(cort))
# print(len(cort))
# print(cort.count("s"))
# print(cort.index("s"))
#------------------------------------------
# d={"1":1.29,"2":0.43}
# c=d["1"]*d["2"]
# d.setdefault("3",c)
# print(d)
# print(d["3"])
#--------------------------------------------
# shool={"3a":32, "3b":34, "3g":27, "3d":38}
# shool["3b"]=32
# shool.setdefault("3v",32)
# shool.pop("3b")
# print(shool)
