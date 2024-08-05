import pygame as pg
import Janela
from Configs import *

def verificar_na_linha(linha: int, coluna: int, valor: int) -> bool:
    for i in range(9):
        if SUDOKU[linha][i] == valor:
            return False
    return True

def verificar_na_coluna(linha: int, coluna: int, valor: int) -> bool:
    for i in range(9):
        if SUDOKU[i][coluna] == valor:
            return False
    return True

def verificar_no_box(linha: int, coluna: int, valor: int) -> bool:
    linha_inicio = (linha // 3) * 3
    coluna_inicio = (coluna // 3) * 3
    for i in range(3):
        for j in range(3):
            if SUDOKU[i + linha_inicio][j + coluna_inicio] == valor:
                return False
    return True

def verificar_disponibilidade(linha: int, coluna: int, valor: int) -> bool:
    return verificar_na_linha(linha, coluna, valor) and \
           verificar_na_coluna(linha, coluna, valor) and \
           verificar_no_box(linha, coluna, valor)

def resolver(janela: Janela.Janela, linha: int = 0, coluna: int = 0) -> bool:
    janela.lin_selec = linha
    janela.col_selec = coluna
    Janela.desenhar_janela(janela, COR_FUNDO2)
    pg.time.wait(ESPERA)
    if linha == 9:
        return True
    if coluna == 9:
        return resolver(janela, linha + 1, 0)
    if SUDOKU[linha][coluna] != 0:
        return resolver(janela, linha, coluna + 1)
    for i in range(1, 10):
        if verificar_disponibilidade(linha, coluna, i):
            SUDOKU[linha][coluna] = i
            if resolver(janela, linha, coluna + 1):
                return True
    SUDOKU[linha][coluna] = 0
    return False
    