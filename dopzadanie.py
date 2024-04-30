#Ты разрабатываешь программное обеспечение для сети магазинов.
# Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики,
# такие как адрес, название и ассортимент товаров. Ваша задача — создать класс Store,
# который можно будет использовать для создания различных магазинов.
#Шаги:
#1. Создай класс Store:
#-Атрибуты класса:
#name: название магазина.
#address: адрес магазина.
#items: словарь, где ключ - название товара, а значение - его цена. Например, {'apples': 0.5, 'bananas': 0.75}.
#Методы класса:
#__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь дляitems`.
#-  метод для добавления товара в ассортимент.
#метод для удаления товара из ассортимента.
#метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
#метод для обновления цены товара.
#2. Создай несколько объектов класса Store:
#Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
#3. Протестировать методы:
#Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери
# товар и запрашивай цену.

class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар {item_name} был добавлен в {self.name}")
    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
    def get_price(self, item_name):
        return self.items.get(item_name)
    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

shop1 = Store("Лента", "Казань, Закиева,5")
shop2 = Store("Ашан", "Казань, Победы,88")
shop3 = Store("Спар", "Казань, Фучика,90")

shop1.add_item("apples", 50)
shop1.add_item("bananas", 75)
shop2.add_item("carrots", 35)
shop2.add_item("tomatoes", 65)
shop3.add_item("milk", 60)
shop3.add_item("bread", 45)

print("Цены перед обновлением:")
print("Яблоки:", shop1.get_price("apples"))
print("Бананы:", shop1.get_price("bananas"))

shop1.update_price("apples", 55)
print("Цена яблок после обновления:", shop1.get_price("apples"))

shop1.remove_item("bananas")
print("Цена бананов после удаления:", shop1.get_price("bananas"))

shop1.add_item("oranges", 80)
print("Цена новых апельсинов:", shop1.get_price("oranges"))