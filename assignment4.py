
#Question 1
lst_1=[1,3,5,7,9]
print(list(reversed(lst_1)))

#Question 2
a=input("Enter A string:")
for i in range(len(a)):
    if a[i].isupper():
        print(a[i])

#Question 3
a=input("Enter Values:").split(",")
b=[]
for i in a:
    b.append(int(i))
print(b)

#Question 4
a=int(input("Enter a number:"))
b=a
f=0
rem=0
while a!=0:
    f=a%10
    rem=rem*10+f
    a//=10
if b==rem:
    print("Palandromic Number")
else:
    print("Not a Palandromic Number")



#Question 5
"""A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original."""
from copy import *
print("DeepCopy: ")
lst_1 = ['a','b',['ab','ba']]

lst_2 = deepcopy(lst_1)

lst_2[2][1] = "d"
lst_2[0] = "c";

print(lst_2)
print(lst_1)
print("Shallow Copy: ")
lst_3=lst_1
lst_3[0]="Hello"
print(lst_3)
print(lst_1)
