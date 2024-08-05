import pygame as pg
from Configs import *

class Janela:
    canvas: pg.display
    fonte: pg.font
    executando: bool
    resolvendo: bool
    lin_selec: int
    col_selec: int

def preencher_tabela_fixos(zerar: bool = False):
    for i in range(9):
        for j in range(9):
            if zerar:
                fixos[i][j] = 0
            else:
                fixos[i][j] = 1 if SUDOKU[i][j] != 0 else 0

def desenhar_janela(janela: Janela, fundo: tuple):
    janela.canvas.fill(fundo)
    pg.draw.rect(janela.canvas, COR_LINHA, pg.Rect(MARGEM // 2, MARGEM //2, TAM_JANELA - MARGEM, TAM_JANELA - MARGEM))
    for lin in range(9):
        for col in range(9):
            celula = pg.Rect(INDICES[col], INDICES[lin], TAM_CELULA, TAM_CELULA)
            cor_cel = COR_CELULA
            if lin == janela.lin_selec and col == janela.col_selec:
                cor_cel = COR_SELECAO
            pg.draw.rect(janela.canvas, cor_cel, celula)
            texto = str(SUDOKU[lin][col]) if SUDOKU[lin][col] != 0 else " "
            img_txt = janela.fonte.render(texto, True, COR_FONTE if fixos[lin][col] == 0 else COR_LINHA)
            txt_ret = img_txt.get_rect()
            txt_ret.center = celula.center
            janela.canvas.blit(img_txt, txt_ret)
    pg.display.update()

fixos = [[0 for _ in range(9)] for _ in range(9)]