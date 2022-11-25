'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")
def mini(a):
    k=a[0]
    for i in range(1,len(a)):
        if a[i]<k:
            k=a[i]
    print (k , "is minimun")
def maxi(a):
    k=a[0]
    for i in range(1,len(a)):
        if a[i]>k:
            k=a[i]
    print (k, "is maxsimum")
       
        
a=(8,2, -3, 7,9,6)
b=(9,3,2,4,7)
mini(a)
maxi(a)
mini(b)
maxi(b)


                
    