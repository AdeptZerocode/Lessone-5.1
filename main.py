#Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и
# статус (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки
# выполненных задач и вывода списка текущих (не выполненных) задач.


class Task():
    def __init__(self):
        self.tasks = []
    def add_task(self, description, deadline):
        self.tasks.append({"description": description, "deadline": deadline,"status": "не выполнено"})

    def mark_as_done(self, description):
        for task in self.tasks:
            if task["description"] == description:
                task["status"] = "выполнено"
                print(f"Задача выполнена")
            else:
                print(f"Задача не выполнена")
