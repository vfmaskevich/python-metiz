# # # Изменение, добавление и удаление элементов

# Удаление элементов из списка
# Удаление элемента с использованием метода pop()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# Пример
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"Последний купленный мотоцикл: {last_owned.title()}.")
