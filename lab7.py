# """
# Лабораторная работа №7
# """
# class krug:
#     def find_length(self, radius):
#         from math import pi
#         return 2*pi*radius
#     def find_obem(self,radius):
#         from math import pi
#         return (4.3)*pi*(radius**2)
# figure=krug()
# print(figure.find_length(5))
# print(figure.find_obem(5))
# #---------------------------------------------
# class paralelepiped:
#     def find_obem(self,x,y,z):
#         v=x*y*z
#         return v
#     def find_area(self,x,y,z):
#         s=((x*y)+(x*z)+(z*y))
#         return s

# x=paralelepiped()
# print(x.find_obem(4,2,3))
# print(x.find_area(4,2,3))
# #--------------------------------------------------
# class obemi:
#     def obem_orb(self,radius):
#         from math import pi
#         return (4.3)*pi*(radius**2)
#     def obem_cilindra(self,radius,h):
#         from math import pi
#         return pi*(radius**2)*h
#     def obem_konusa(self,radius,h):
#         from math import pi
#         return (1/3)*pi*(radius**2)*h

# x=obemi()
# print(x.obem_orb(4))
# print(x.obem_cilindra(4,6))
# print(x.obem_konusa(4,7))

"""
Самостоятельная работа №7
"""
# class auto:
#     mark="Mitsubishi"
#     color="Black"
#     year=2007
#     obem=3.0

# car=auto()
# print(car.mark,car.color,car.year,car.obem)
# x=input("select changes: mark\ncolor\nyear\nobem\n")
# y=input("choice cange:")
# if x.strip().lower()=="mark":
#     car.mark=y
# elif x.strip().lower()=="color":
#     car.color=y
# elif x.strip().lower()=="year":
#     car.year=y
# elif x.strip().lower()=="obem":
#     car.obem=y

# print(car.mark,car.color,car.year,car.obem)
#----------------------------------------------------
# class robot:
#     power=100
#     room="kitchen"

# atributs=robot()
# print(atributs.power,atributs.room)
# x=input("Enter atribut: \npower\nroom\n")
# y=input("Enter changes: ")
# if x.strip().lower()=="power":
#     atributs.power=y
# elif x.strip().lower()=="room":
#     atributs.room=y
# print(atributs.power,atributs.room)
#--------------------------------------------------
# class figure:
#     height=5
#     wigth=4
#     def perimetr(self,x,y):
#         return (x+y)*2
#     def plosh(self,x,y):
#         return x*y

# figr=figure()

# print(figr.perimetr(figr.height,figr.wigth))
# print(figr.plosh(figr.height,figr.wigth))