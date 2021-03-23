#6 store a list of first names.Count the occurence of 'a' within the list

l = input("enter names")
word=l.split()
print(word)
count=0
for i in l:
  if i=="a":
    count+=1
print("The occurence of a is",count)