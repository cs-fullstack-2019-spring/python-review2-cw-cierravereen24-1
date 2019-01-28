# Point of entry.
# The main function calls the problem fucntion within its scope.
def main():
    problem1()

# Create a task list. A user is presented with the text below.
# Let them select an option to list all of their tasks,
# add a task to their list, delete a task, or quit the program.
# Make each option a different function in your program.
def problem1():

    toDoList = [{"1. Do my laundry."},
                {"2. Watch YouTube tutorials about Python."},
                {"3. Vacuum Civi's floor."},
                {"4. Feed YangYang amd Thalia."}
                ]

    prompt = ""
    prompt2 = ""

    # A while loop that keeps iterating the user inputted value, until q is typed to quit.
    while True:
        prompt = input("Congratulations! You're running Cierra's Task List program.\nEnter what would you like to do next:\n1. List all tasks.\n2. Add a task to the list.\n3. Delete a task.\n0. To quit the program press 'q'. ")

        for goals in toDoList:
            print(goals)

        if prompt.lower() == "q":
            break
        elif prompt == 1:
            print(toDoList)
        elif prompt == 2:
            prompt2 = input("Enter a task to add to the the list.")
            toDoList.append(prompt2)
        elif prompt == 3:
            toDoList.remove([])



if __name__ == '__main__':
    main()