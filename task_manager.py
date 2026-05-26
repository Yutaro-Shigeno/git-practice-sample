from datetime import datetime


class Task:
    def __init__(self, task_id, title, owner, priority):
        self.task_id = task_id
        self.title = title
        self.owner = owner
        self.priority = priority
        self.status = "todo"
        self.created_at = datetime.now()

    def start(self):
        self.status = "in_progress"

    def complete(self):
        self.status = "done"

    def change_priority(self, priority):
        self.priority = priority

    def __str__(self):
        return (
            f"[{self.task_id}] {self.title} "
            f"owner={self.owner} "
            f"priority={self.priority} "
            f"status={self.status}"
        )


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def find_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def show_all_tasks(self):
        for task in self.tasks:
            print(task)

    def show_open_tasks(self):
        for task in self.tasks:
            if task.status != "done":
                print(task)


def main():
    manager = TaskManager()
    print("Task Manager Practice")

    task1 = Task(1, "Create GitHub repository", "Alice", "High")
    task2 = Task(2, "Clone repository to local PC", "Bob", "Medium")
    task3 = Task(3, "Practice merge conflict on main branch", "Charlie", "High")
    
    manager.add_task(task1)
    manager.add_task(task2)
    manager.add_task(task3)

    task1.start()
    task2.complete()

    print("Main branch exclusive message")
    print("All tasks:")
    manager.show_all_tasks()

    print("Open tasks:")
    manager.show_open_tasks()


if __name__ == "__main__":
    main()