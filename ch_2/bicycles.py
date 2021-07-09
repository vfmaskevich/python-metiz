bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# Вывод элементов списка
print(bicycles[1].title())
print(bicycles[3].title())
# Вывод последнего элемента списка
print(bicycles[-1])
# Попробуем извлечь название первого велосипеда из списка и составить
# сообщение, включающее это значение.
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)
