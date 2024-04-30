class Task:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        """Добавляет новую задачу в список с задачами."""
        self.tasks.append({
            'description': description,
            'due_date': due_date,
            'status': 'не выполнено'
        })

    def mark_as_done(self, description):
        """Отмечает задачу как выполненную по описанию."""
        for task in self.tasks:
            if task['description'] == description:
                task['status'] = 'выполнено'
                break

    def get_pending_tasks(self):
        """Возвращает список невыполненных задач."""
        return [task for task in self.tasks if task['status'] == 'не выполнено']

# Создание объекта класса Task
task_manager = Task()

# Добавление задач
task_manager.add_task("Купить продукты", "2023-09-10")
task_manager.add_task("Посетить врача", "2023-09-12")
task_manager.add_task("Сдать проект", "2023-09-15")

# Отметка задачи как выполненной
task_manager.mark_as_done("Посетить врача")

# Вывод списка невыполненных задач
pending_tasks = task_manager.get_pending_tasks()
for task in pending_tasks:
    print(f"Задача: {task['description']}, Срок: {task['due_date']}, Статус: {task['status']}")