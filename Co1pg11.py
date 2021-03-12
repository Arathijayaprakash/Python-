a = int(input("Enter a no."))
b = int(input("enter a no."))
c = int(input("enter a no."))
if a > b:
    if a > c:
        print(a,"is biggest")
    else:
        print(c,"is biggest")
else:
    if b < c:
        print(c,"is biggest")
    else:
        print(b,"is biggest")