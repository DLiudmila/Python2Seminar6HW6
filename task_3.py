# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной
# расстановки ферзей в задаче выше. Проверяйте различный случайные
# варианты и выведите 4 успешных расстановки.
import random


def is_safe(board):
    for i in range(8):
        for j in range(i+1, 8):
            # Проверяем, бьют ли ферзи друг друга по столбцам, строкам или диагоналям
            if board[i][0] == board[j][0] or board[i][1] == board[j][1] or abs(board[i][0] - board[j][0]) == abs(board[i][1] - board[j][1]):
                return False
    return True

# Считывание координат ферзей
def get_quins():
    queens = set()

    while len(queens)<8:
        x = random.randint(1, 8)
        y = random.randint(1, 8)
        queens.add((x, y))
    return queens

# Проверка, бьют ли ферзи друг друга
counter = 0
while counter < 4:
    boardList = list(get_quins())
    if is_safe(boardList):
        print(boardList)
        counter=counter+1