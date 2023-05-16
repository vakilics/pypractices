#Create-To-Do-List-----------
todos = []
while True:
    userinput = input("Type add, show, edit or exit:")
    userinput = userinput.strip()
    match userinput:
        case 'add' | 'include':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'print' | 'display':
            #print(todos)
            #for item in todos:  #we can add enumerate fuc to access items and index! more otions!
            for index, item in enumerate(todos):
                item = item.title() #capitalizes each words first character
                #print(item) with "f" string!
                print(f"{index + 1}-{item}") # add 1 just to statrt index nums from  1
        case 'edit' | 'change':
            number = int(input('# of todo to edit: '))
            number = number -1  # haha, indexing issue!
            #print(existing_todo = todos[number])
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

        case 'complete' | 'done' | 'remove':   #manipulation process!
            number = int(input('# of todo to complete: '))
            todos.pop(number)
        case 'exit' | 'quite' | 'q':
            break
print("Bye!")

#NOTES-------------------------
'''
#------------------List .vs Tuple:
List is more flexible( modifications such as replace (mylist.replace...), remove...) but Tuple is immutable!

#------------------Object representation:
<enumerate object at 0x7fd45e46f740>
>>> list(a)     
[(0, 'a'), (1, 'b')]
>>> 
>>> b = enumerate("Hellow")
>>> b
<enumerate object at 0x7f5c400d9080>
>>> list(b)
[(0, 'H'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o'), (5, 'w')]






'''