list = []
n = int(input("Enter size : "))
for i in range(0,n):
    x = int(input("enter No."))
    if x>100:
        list.append("over")
    else:
        list.append(x)
print(list)