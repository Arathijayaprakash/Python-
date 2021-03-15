N = int(input("Enter no. of terms: "))
a = 0
b = 1
if (N <= 0):
    print("Enter a positive integer: ")
elif(N==1):
    print(a)
else:
    for nth in range(N+1):
        print(a)
        nth = a+b
        a = b
        b = nth