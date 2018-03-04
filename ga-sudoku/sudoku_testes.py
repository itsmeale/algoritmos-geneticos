"""
algoritmos primitivos para a elaboracao de um score
para avaliar um dado tabuleiro
"""

sudoku = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0 ,9 ,8, 0, 0, 0, 0, 6, 0],
          
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],

          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

def view_sudoku(sudoku):

    for row in sudoku:
        print(" ".join([str(value) for value in row]))

def check_rows(sudoku):

    ok_rows = 0
    for index, row in enumerate(sudoku):
        if len(set(row)) == len(sudoku[index]):
            ok_rows += 1
    return ok_rows

def check_cols(sudoku):

    ok_cols = 0
    for row in list(zip(*sudoku)):
        if len(set(row)) == len(sudoku):
            ok_cols += 1
    return ok_cols

def check_diagonals(sudoku):
    
    diag_1 = ""; diag_2 = ""
    for index, row in enumerate(sudoku):
        for index_aux, value in enumerate(row):
           if index == index_aux: diag_1 += str(value)   
        diag_2 += str(row[len(row)-index-1])
    ok_diags = 0

    if len(set(diag_1)) == len(sudoku[0]): ok_diags += 1
    if len(set(diag_2)) == len(sudoku[0]): ok_diags += 1
    return ok_diags

def avaliar_sudoku(sudoku):
    
    return (check_rows(sudoku) + check_cols(sudoku) + check_diagonals(sudoku))/(len(sudoku) + len(sudoku[0]) + 2) * 10
