#Create-To-Do-List-----------
while True:
    userinput = input("Type add, show, edit or exit:")
    userinput = userinput.strip()
    match userinput:
        case 'add' | 'include':
            todo = input("Enter a todo: ") + "\n"

            file = open('save-todo.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('save-todo.txt', 'w')  #SAVE DATA: 'w': write and overwrite!
            file.writelines(todos)
            file.close()

        case 'show' | 'print' | 'display':
            file = open('save-todo.txt', 'r')
            todos = file.readlines()
            file.close()

            #print(todos) # we see that is includes \n . for user frendly view, can use list comprehension (list and loop in one line of code!)
            new_todos = [item.strip('\n') for item in todos]

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
            file.close()
            break
print("Bye!")

