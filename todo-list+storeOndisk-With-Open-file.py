#Create-To-Do-List-----------
while True:
    userinput = input("Type add, show, edit or exit:")
    userinput = userinput.strip()
    match userinput:
        case 'add' | 'include':
            todo = input("Enter a todo: ") + "\n"

            with open('save-todo.txt', 'r') as file:   #With context manager: no need to use file.close() then!
                todos = file.readlines()

            todos.append(todo)
            #Instead of bellow 3 lines, used with open....
            #file = open('save-todo.txt', 'w')  #SAVE DATA: 'w': write and overwrite!
            #file.writelines(todos)
            #file.close()
            with open('save-todo.txt', 'w') as file:
                file.writelines(todos)



        case 'show' | 'print' | 'display':
            with open('save-todo.txt', 'r') as file:  # With context manager: no need to use file.close() then!
                todos = file.readlines()

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

            with open('save-todo.txt', 'r') as file:
                todos = file.readlines()
            print('here is existing todo',todos)

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('save-todo.txt', 'w') as file:
                file.writelines(todos)


        case 'complete' | 'done' | 'remove':   #manipulation process!
            number = int(input('# of todo to complete: '))
            with open('save-todo.txt', 'r') as file:
                todos = file.readlines()
            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(number -1)

            with open('save-todo.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)

        case 'exit' | 'quite' | 'q':
            break
print("Bye!")

