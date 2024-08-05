# DEFINIÇÃO CORES
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (152, 255, 51)
ROSA = (255, 51, 153)
CINZA_CLARO = (150, 150, 150)
CINZA_ESCURO = (50, 50, 50)
AZUL = (0, 51, 102)
BORDO = (95, 2, 31)

# APLICAÇÃO CORES
COR_FUNDO = AZUL
COR_FUNDO2 = BORDO
COR_CELULA = CINZA_ESCURO
COR_LINHA = BRANCO
COR_FONTE = VERDE
COR_SELECAO = ROSA

# TAMANHOS 
MARGEM = 40
TAM_CELULA = 70
LINHA_P = 1
LINHA_G = 5
TAM_JANELA = (TAM_CELULA * 9) + (LINHA_G * 4) + (LINHA_P * 6) + MARGEM
INDICES = [(MARGEM // 2) + LINHA_G, 0, 0, 0, 0, 0, 0, 0, 0]
INDICES[1] = INDICES[0] + TAM_CELULA + LINHA_P
INDICES[2] = INDICES[1] + TAM_CELULA + LINHA_P
INDICES[3] = INDICES[2] + TAM_CELULA + LINHA_G
INDICES[4] = INDICES[3] + TAM_CELULA + LINHA_P
INDICES[5] = INDICES[4] + TAM_CELULA + LINHA_P
INDICES[6] = INDICES[5] + TAM_CELULA + LINHA_G
INDICES[7] = INDICES[6] + TAM_CELULA + LINHA_P
INDICES[8] = INDICES[7] + TAM_CELULA + LINHA_P

# OUTROS
ESPERA = 0

# TABULEIRO
SUDOKU = [[ 8 , 7 , 0 ,     0 , 3 , 5 ,     9 , 0 , 2 ],
          [ 0 , 4 , 0 ,     0 , 0 , 0 ,     0 , 1 , 0 ],
          [ 0 , 0 , 0 ,     9 , 0 , 1 ,     0 , 0 , 7 ],

          [ 0 , 0 , 0 ,     0 , 0 , 0 ,     5 , 0 , 0 ],
          [ 0 , 1 , 0 ,     0 , 6 , 0 ,     0 , 0 , 0 ],
          [ 0 , 0 , 3 ,     0 , 2 , 4 ,     0 , 7 , 9 ],

          [ 0 , 0 , 0 ,     0 , 0 , 9 ,     6 , 5 , 0 ],
          [ 0 , 0 , 0 ,     6 , 1 , 0 ,     0 , 4 , 0 ],
          [ 7 , 6 , 0 ,     3 , 0 , 0 ,     0 , 9 , 1 ]]
