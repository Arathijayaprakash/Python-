import csv

header = ["place", "name", "age"]
with open("city.csv", "w") as file:
    write = csv.DictWriter(file, fieldnames=header)
    write.writeheader()
    write.writerow({"place": "Thiruvangoor", "name": "Arathi", "age": 21})
    write.writerow({"place": "Kainatty", "name": "Aswana", "age": 21})
    write.writerow({"place": "Anela", "name": "Anusree", "age": 21})
    write.writerow({"place": "Kiyoor", "name": "Arundhathi", "age": 21})
with open("city.csv", "r") as file:
    read = csv.DictReader(file);
    n = input("Enter the column name you want(place,name,age):")
    for i in read:
        print(i[n])