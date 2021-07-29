# 3.10. Все функции: придумайте информацию, которую можно было бы хранить в
# списке.
# Например, создайте список гор, рек, стран, городов, языков… словом, чего
# угодно. Напишите программу, которая создает список элементов, а затем вызыва-
# ет каждую функцию, упоминавшуюся в этой главе, хотя бы один раз.
languages = ['русский', 'английский', 'немецкий', 'польский', 'испанский']
print(languages)

# Определение длины списка
message = f"В списке {len(languages)} языков."
print(message)

# Временная сортировка списка функцией sorted()
print("Вот исходный список:")
print(languages)

print("\nВот отсортированный список:")
print(sorted(languages))

print("\nВот снова исходный список:")
print(languages)

# Вывод списка в обратном порядке
languages.reverse()
print("\nВывод списка в обратном порядке:")
print(languages)

# Упорядочение списка. Постоянная сортировка списка методом sort()
languages.sort()
print(languages)
# В следующем примере список сортируется в порядке, обратном алфавитному
languages.sort(reverse=True)
print(languages)
