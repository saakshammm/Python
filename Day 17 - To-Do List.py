# To-Do List – Create a basic to-do list where users can add and remove tasks

tasks = []

def show_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"\n{task} has been added to your to-do list.")


def remove_task():
    show_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"{removed_task} has been removed from your to-do list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()



