import os

class ToDoList:
    def __init__(self, filename='todo.txt'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                tasks = file.read().splitlines()
        else:
            tasks = []
        return tasks

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task}\n")

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks.pop(task_number)
            self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            todo_list.view_tasks()
        elif choice == '2':
            task = input("Enter the task: ").strip()
            if task:
                todo_list.add_task(task)
                print("Task added.")
            else:
                print("Task cannot be empty.")
        elif choice == '3':
            todo_list.view_tasks()
            try:
                task_number = int(input("Enter the task number to remove: ").strip()) - 1
                todo_list.remove_task(task_number)
                print("Task removed.")
            except (ValueError, IndexError):
                print("Invalid task number.")
        elif choice == '4':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please select from the menu options.")

if __name__ == "__main__":
    main()
