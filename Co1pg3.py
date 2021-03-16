#list comprehension generate posive list of numbers from a given list of integers.#

list=[1,-3,5,9,0,-8,2,-6,-4]
newlist=[x for x in list if x>0]
print(newlist)

#square

n = int(input("enter no. of no.s:"))
list=[]
for x in range(n):
    x=int(input("Enter no.:"))
    list.append(x)
print(list)
squarelist=[x**2 for x in list]
print(squarelist)

#list of vowels

word = "umberella"
vowels = "aeiou"
list = [x for x in word if x in vowels]
print(list)

#ordinal value

word="flower"
list=[ord(x) for x in word]
print(list)