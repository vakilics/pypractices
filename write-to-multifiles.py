content = ['Hamid', 'Nazanin', 'Sadiya']
filenames = ['Hamidfile.txt','Nazaninfile.txt', 'Sadiyafile.txt']

for content, filename in zip(content,filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)


