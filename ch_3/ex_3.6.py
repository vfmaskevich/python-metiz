# 3.6. Больше гостей: вы решили купить обеденный стол большего размера.
# Дополнительные места позволяют пригласить на обед еще трех гостей.
# • Начните с программы из упражнения 3.4 или 3.5. Добавьте в конец программы
# коман ду print, которая выводит сообщение о расширении списка гостей.
# • Добавьте вызов insert() для добавления одного гостя в начало списка.
# • Добавьте вызов insert() для добавления одного гостя в середину списка.
# • Добавьте вызов append() для добавления одного гостя в конец списка.
# • Выведите новый набор сообщений с приглашениями — по одному для каждого
# участника, входящего в список.
guests = ['Андрей', 'Александр', 'Станислав']
message = f"Привет, {guests[0]}! Приглашаю тебя пообедать с нами, если желаешь!"
print(message)
message = f"Привет, {guests[1]}! Приглашаю тебя пообедать с нами, если желаешь!"
print(message)
message = f"Привет, {guests[2]}! Приглашаю тебя пообедать с нами, если желаешь!"
print(message)
message = "Список гостей увеличен."
print(message)

# Добавляем гостей в разные позиции, согласно заданию и выводим список.
guests.insert(0, 'Владимир')
guests.insert(2, 'Константин')
guests.append('Виктор')
print(guests)

# Выводим соообщения с приглашениями для каждого гостя.
message = f"Привет, {guests[0]}! Приглашаю тебя пообедать с нами, если желаешь!"
print(message)
message = f"Привет, {guests[1]}! Приглашаю тебя пообедать с нами, если желаешь!"
print(message)
message = f"Привет, {guests[2]}! Приглашаю тебя пообедать с нами, если желаешь!"
print(message)
message = f"Привет, {guests[3]}! Приглашаю тебя пообедать с нами, если желаешь!"
print(message)
message = f"Привет, {guests[4]}! Приглашаю тебя пообедать с нами, если желаешь!"
print(message)