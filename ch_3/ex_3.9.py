# 3.9. Количество гостей: в одной из программ из упражнений с 3.4 по 3.7
# используйте len() для вывода сообщения с количеством людей, приглашенных на обед.
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

# Выводим сообщение и удаляем последовательно гостя, выдавая каждый раз сооб-
# щение
message = "На обед приглашаются всего 2 гостя"
print(message)
cancel_invite = guests.pop()
message = f"Дорогой {cancel_invite}! Сожалею, об отмене приглашения"
print(message)
cancel_invite = guests.pop()
message = f"Дорогой {cancel_invite}! Сожалею, об отмене приглашения"
print(message)
cancel_invite = guests.pop()
message = f"Дорогой {cancel_invite}! Сожалею, об отмене приглашения"
print(message)
cancel_invite = guests.pop()
message = f"Дорогой {cancel_invite}! Сожалею, об отмене приглашения"
print(message)

# Выведим сообщение для каждого из двух человек, остающихся в списке.
message = f"Дорогой, {guests[0]}! Раннее высланное приглашение остается в силе"
print(message)
message = f"Дорогой, {guests[1]}! Раннее высланное приглашение остается в силе"
print(message)

message = f"Приглашено на обед {len(guests)} гостей."
print(message)
