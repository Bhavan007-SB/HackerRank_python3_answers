n = int(input())
if n%2 == 1:
    print("Weird")
elif 2<n<5 and n%2 == 0:
    print("Not Weird")    
elif 6<n<21 and n%2 == 0:
    print("Weird")
elif  n>20 and n%2  == 0: 
    print("Not Weird")
