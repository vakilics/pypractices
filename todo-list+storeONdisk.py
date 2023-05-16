#Create-To-Do-List-----------
todos = []
while True:
    userinput = input("Type add, show, edit or exit:")
    userinput = userinput.strip()
    match userinput:
        case 'add' | 'include':
            todo = input("Enter a todo: ") + "\n"
            todos.append(todo)
            file = open('save-todo.txt', 'w')  #SAVE DATA: 'w': write and overwrite!
            file.writelines(todos)

        case 'show' | 'print' | 'display':
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

