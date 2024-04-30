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
                print(f"Задача {description} выполнена")
                break

    def get_pending_tasks(self):
        return [task for task in self.tasks if task["status"] == "не выполнено"]
    def list_tasks(self):
        print("Текущие задачи")
        for task in self.tasks:
            if task["status"] == "не выполнено":
                print(f"{task["description"]} - {task["deadline"]}")

Zada4a = Task()
Zada4a.add_task("Приготовить ужин", "30.04.2024")
Zada4a.add_task("Визит к врачу", "01.05.2024")
Zada4a.add_task("Пройти урок", "02.05.2024")

Zada4a.list_tasks()
Zada4a.mark_as_done("Приготовить ужин")

pending_tasks = Zada4a.get_pending_tasks()
for task in pending_tasks:
    print(f"Задача: {task["description"]}, Срок: {task["deadline"]}, Статус: {task["status"]}")