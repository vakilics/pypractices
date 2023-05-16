'''
import glob
myfile = glob.glob("files/*.txt")
for filepath in myfile:
    with open(filepath, 'r') as file:
        #print(file.read().find("Ha"))
        print(file.read().upper())
print(myfile)
'''

# Search L.Name of a person by providing his/her name!
import csv

with open("files/ok.csv") as f:
    data = list(csv.reader(f))
print(data)
name = input("Enter the name to search: ")
for row in data[1:]:  #means: start from index 1 and therefore escapes first row (Nun, Name, L,Name)
    #print(row)
    if row[1] == name: #row[1], here is the Name
        print(row[2])

#print(data[0][1])