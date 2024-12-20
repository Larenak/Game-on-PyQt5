"""Файл создания модели игрового поля"""

from random import randint

#максимальное значение одного квадрата
max_value_green_sqr = 9
#длина и ширина игровога поля
board_x = 5
board_y = 5
#максимальное значение суммы ряда ( не работает на столбцы ) ( board_x * max_value_green_sqr / 2 + board_x * max_value_green_sqr / 4)
# формула оптимального максимального значения при данном алгоритме

max_sum = int(board_x * max_value_green_sqr / 2 + board_x * max_value_green_sqr / 4)
def Board_generate():

    sum_x = [] # суммы чисел рядов 
    sum_y = [] # суммы чисел строк

    game_board = [[None for i in range(board_x)] for j in range(board_y)]
    for i in range(board_y):
        sum_y.append(randint(1, max_sum))
    tmp = sum_y.copy()

    # заполнение массив поля рандомными значениями в соответствии с суммой ряда по оси y
    # при этом, оставляя случайные ячейки ряда пустыми для создания головоломки

    for j in range(board_y):
        while tmp[j] != 0:
            tmp[j] = sum_y[j]
            game_board[j] = [None for i in range(board_x)]
            for i in range(board_x):
                green_sqr_value = randint(1,max_value_green_sqr)
                green_sqr_place = randint(0,board_x - 1)
                while game_board[j][green_sqr_place] != None:
                    green_sqr_place = randint(0,board_x - 1)
                game_board[j][green_sqr_place] = green_sqr_value
                tmp[j] -= green_sqr_value
                if tmp[j] == 0:
                    break

            # Если в строке все числа подходят, то начинаем подбирать числа заново, то есть продолжаем выполнение цикла
            # (нужна хотя бы 1 ячейка, которая нарушает сумму строки) 

            if None not in game_board[j]:
                tmp[j] = 1            
                
    # заполнение сумм столбцов доски по оси x в соответствии с полученными значениями

    for i in range(board_x):
        summ = 0
        for j in range(board_y):
            if game_board[j][i] != None:
                summ += game_board[j][i]

            # заполнение пустых ячеек доски случайными числами

            else:
                game_board[j][i] = randint(1,max_value_green_sqr)
        sum_x.append(summ)
    return game_board, sum_x, sum_y
res = Board_generate()
game_board = res[0]
sum_x = res[1]
sum_y = res[2]