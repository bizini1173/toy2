import random  
class Toy:
    def __init__(self, toy_id, name, quantity, weight):  
        self.toy_id = toy_id  
        self.name = name  
        self.quantity = quantity  
        self.weight = weight 

class ToyStore:
    def __init__(self):  
        self.toys = []  # Создаем пустой список для хранения игрушек

    def add_toy(self, toy_id, name, quantity, weight):  # Метод добавления новой игрушки
        toy = Toy(toy_id, name, quantity, weight) 
        self.toys.append(toy)  # Добавляем игрушку в список игрушек магазина

    def update_weight(self, toy_id, new_weight):  # Метод обновления веса игрушки
        for toy in self.toys:  
            if toy.toy_id == toy_id:  
                toy.weight = new_weight  
                break

    def choose_prize_toy(self):  # Метод выбора призовой игрушки
        total_weight = sum(toy.weight for toy in self.toys)  
        random_number = random.uniform(0, total_weight) 
        cumulative_weight = 0
        for toy in self.toys:  
            cumulative_weight += toy.weight  
            if random_number <= cumulative_weight:  
                return toy  

    def award_prize_toy(self):  # Метод проведения розыгрыша призовой игрушки
        prize_toy = self.choose_prize_toy()  # Выбираем призовую игрушку
        if prize_toy:  # Если призовая игрушка выбрана
            prize_toy.quantity -= 1  # Уменьшаем количество игрушек на 1
            self.toys.remove(prize_toy)  # Удаляем призовую игрушку из списка игрушек
            print(f"Поздравляем! Вы выиграли {prize_toy.name}\n")  # Выводим сообщение о победе

# Пример использования
toy_store = ToyStore()  # Создаем объект класса ToyStore
toy_store.add_toy(1, "Машина", 10, 20)  # Добавляем игрушку в магазин
toy_store.add_toy(2, "Кукла", 5, 30)  # Добавляем игрушку в магазин
toy_store.add_toy(3, "мяч", 8, 50)  # Добавляем игрушку в магазин

# Розыгрыш
for i in range(1):  # Проводим 1 розыгрыш
    toy_store.award_prize_toy()  # Вызываем метод проведения розыгрыша призовой игрушки
