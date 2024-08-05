import pygame as pg
import Solucionador
import Janela
from Configs import *

def mudar_valor(linha: int, coluna: int, valor: int):
    Janela.preencher_tabela_fixos(True)
    SUDOKU[linha][coluna] = valor

def apagar_sudoku():
    for i in range(9):
        for j in range(9):
            SUDOKU[i][j] = 0

def verificar_evento(janela: Janela.Janela):
    for event in pg.event.get():
        if event.type  == pg.QUIT:
            janela.executando = False
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pressionado(janela)
        if event.type == pg.KEYDOWN:
            tecla_pressionada(janela, event.key)

def mouse_pressionado(janela: Janela.Janela):
    x, y = pg.mouse.get_pos()
    valido = False
    for i in range(9):
        if (x >= INDICES[i] and x <= INDICES[i] + TAM_CELULA):
            valido = True
            x = i
            break
    if valido:
        valido = False
        for j in range(9):
            if (y >= INDICES[j] and y <= INDICES[j] + TAM_CELULA):
                valido = True
                y = j
                break
    if valido:
        janela.lin_selec = y
        janela.col_selec = x


def tecla_pressionada(janela: Janela.Janela, key: pg.key):
    if key == pg.K_KP9 or key == pg.K_9:
        mudar_valor(janela.lin_selec, janela.col_selec, 9)
    elif key == pg.K_KP8 or key == pg.K_8:
        mudar_valor(janela.lin_selec, janela.col_selec, 8)
    elif key == pg.K_KP7 or key == pg.K_7:
        mudar_valor(janela.lin_selec, janela.col_selec, 7)
    elif key == pg.K_KP6 or key == pg.K_6:
        mudar_valor(janela.lin_selec, janela.col_selec, 6)
    elif key == pg.K_KP5 or key == pg.K_5:
        mudar_valor(janela.lin_selec, janela.col_selec, 5)
    elif key == pg.K_KP4 or key == pg.K_4:
        mudar_valor(janela.lin_selec, janela.col_selec, 4)
    elif key == pg.K_KP3 or key == pg.K_3:
        mudar_valor(janela.lin_selec, janela.col_selec, 3)
    elif key == pg.K_KP2 or key == pg.K_2:
        mudar_valor(janela.lin_selec, janela.col_selec, 2)
    elif key == pg.K_KP1 or key == pg.K_1:
        mudar_valor(janela.lin_selec, janela.col_selec, 1)
    elif key == pg.K_KP0 or key == pg.K_0 or key == pg.K_BACKSPACE:
        mudar_valor(janela.lin_selec, janela.col_selec, 0)
    elif key == pg.K_r:
        apagar_sudoku()
    elif key == pg.K_UP or key == pg.K_w:
        janela.lin_selec = 8 if janela.lin_selec == 0 else janela.lin_selec - 1
    elif key == pg.K_DOWN or key == pg.K_s:
        janela.lin_selec = 0 if janela.lin_selec == 8 else janela.lin_selec + 1
    elif key == pg.K_LEFT or key == pg.K_a:
        janela.col_selec = 8 if janela.col_selec == 0 else janela.col_selec - 1
    elif key == pg.K_RIGHT or key == pg.K_d:
        janela.col_selec = 0 if janela.col_selec == 8 else janela.col_selec + 1
    elif key == pg.K_ESCAPE:
        janela.executando = False
    elif key == pg.K_SPACE or key == pg.K_RETURN or key == pg.K_KP_ENTER:
        Janela.preencher_tabela_fixos()
        Solucionador.resolver(janela)
        janela.lin_selec = 0
        janela.col_selec = 0

    
lin_selec = 0
col_selec = 0

