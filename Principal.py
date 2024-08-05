import pygame as pg
from Configs import *
import Janela
import Eventos

pg.init()
janela = Janela.Janela()
janela.canvas = pg.display.set_mode((TAM_JANELA, TAM_JANELA))
pg.display.set_caption("Solucionador de Sudoku")
janela.fonte = pg.font.Font("chintzy.ttf", 72)
janela.executando = True
janela.resolvendo = False
janela.lin_selec = 0
janela.col_selec = 0
while janela.executando:
    Janela.desenhar_janela(janela, COR_FUNDO)
    Eventos.verificar_evento(janela)
pg.quit()
quit()