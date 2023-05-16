filenames = ['1.doc','1.report','1.xml']

#list comprehension: for any filename in filenemames, replace filename with new naming
filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]

print(filenames)

# capitalizes all the names and surnames
names = ["john smith", "jay santi", "eva kuki"]
names = [name.title() for name in names]
print(names)