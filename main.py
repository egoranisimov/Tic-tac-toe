# Словарь с ключами-координатами и значениями, в которые будут записываться сделанные ходы
cells = {'1_1': '-', '1_2': '-', '1_3': '-',
         '2_1': '-', '2_2': '-', '2_3': '-',
         '3_1': '-', '3_2': '-', '3_3': '-'}
used_cells = []  # Список использованных клеток
result = False  # Переменная для остановки основного цикла в случае победы или ничьи


# Функция для вывода игрового поля
def print_field():
    global cells
    print(' ', '1', '2', '3', sep='  ')
    print('1', cells['1_1'], cells['1_2'], cells['1_3'], sep='  ')
    print('2', cells['2_1'], cells['2_2'], cells['2_3'], sep='  ')
    print('3', cells['3_1'], cells['3_2'], cells['3_3'], sep='  ')


# Функция для определения победы/ничьи
def check_result(user, marker):
    global result

    cells_values = list(cells.values())
    # Создаем список возможных выигрышных комбинаций клеток
    win_streak = [cells_values[::3], cells_values[1::3], cells_values[2::3],  # Столбцы
                  cells_values[:3], cells_values[3:6], cells_values[6:],  # Строки
                  cells_values[::4], cells_values[2:7:2]]  # Диагонали

    if any([i.count(marker) == 3 for i in win_streak]):
        print_field()
        print(f'Пользователь {user} выиграл! Поздравляю!')
        result = True
    elif len(used_cells) == 9:
        print_field()
        print('Ничья! Победила дружба!')
        result = True


# Функция, вызывающая следующий ход
def next_step(user):
    print_field()
    step = input(f'{user}, введи координату клетки: ')

    # Цикл для проверки правильности ввода координаты.
    # Если координата введена корректно, то ее значение записывается в список использованных клеток
    while True:
        if step not in cells.keys():
            step = input(f"{user}, координата клетки введена неправильно.\n"
                         f"Координату клетки необходимо вводить в формате 'i_j', где 'i' и 'j' - номер строки и "
                         f"столбца соовтетственно.\n"
                         f"Попробуй ввести координату клетки еще раз: ")
        elif step in used_cells:
            step = input(f"{user}, данная клетка уже использована, попробуй еще раз: ")
        else:
            used_cells.append(step)
            break

    # Цикл с присвоением маркера, соответствующего текущему пользователю, клетке, соответствующей введенным координатам
    for i in cells.keys():
        if user == user_1:
            if i == step:
                cells[i] = 'O'
                check_result(user, 'O')
                break
        else:
            if i == step:
                cells[i] = 'X'
                check_result(user, 'X')
                break


# Приветственное сообщение, считывание имен пользователей, общая информация, правила ввода координат
print('Добро пожаловать в игру крестики-нолики')
user_1, user_2 = input('Введите имя первого пользвоателя: '), input('Введите имя второго пользователя: ')
current_user = user_1
print(f"Пользователь {user_1} будет использовать маркер 'O'.")
print(f"Пользователь {user_2} будет использовать маркер 'X'.")
print("Введите координату клетки, чтобы сделать ход.\n"
      "Координату клетки необходимо вводить в формате 'i_j', где 'i' и 'j' - номер строки и столбца соовтетственно.")

# Основной цикл с вызовом функции следующего шага. Цикл прерывается в случае победы или ничьи
while not result:
    next_step(current_user)
    if current_user == user_1:
        current_user = user_2
    else:
        current_user = user_1
