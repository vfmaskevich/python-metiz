user_name = " Vladimir\t \n\t  "
print(user_name)
print(user_name.lstrip())  # метод strip() удаляет пропуски с левого края
print(user_name.rstrip())  # метод strip() удаляет пропуски с правого края
print(user_name.strip())  # метод strip() удаляет пропуски с обоих концов

# 2.7. Удаление пропусков: сохраните имя пользователя в переменной. Добавьте
# в начале и в конце имени несколько пропусков. Проследите за тем, чтобы каждая
# служебная последовательность , "\t" и "\n", встречалась по крайней мере один
# раз.
# Выведите имя, чтобы были видны пропуски в начале и конце строки. Затем выве-
# дите его снова с использованием каждой из функций удаления пропусков:
# lstrip(), rstrip() и strip().