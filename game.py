import tkinter as tk # interface
from tkinter import messagebox
import ctypes # chama funcoes do codigo em C
import os # ve qual SO eh

# define nome do arquivo da biblioteca C (.dll para Windows, .so para Linux/Mac)
if os.name == 'nt':
    libFilename = './logic.dll'
else:
    libFilename = './logic.so'

# carrega a biblioteca
try:
    logicLib = ctypes.CDLL(libFilename)
except OSError as e:
    messagebox.showerror("deu uma merda ai")
    exit()

logicLib.initBoard.restype = None # seria tipo equivalente a: void initBoard()

logicLib.makeMove.argtypes = [ctypes.c_int, ctypes.c_char]
logicLib.makeMove.restype = ctypes.c_int

logicLib.checkWinner.restype = ctypes.c_char

logicLib.checkDraw.restype = ctypes.c_bool

# passa o array gameboard pro python
cGameBoard = (ctypes.c_char * 9).in_dll(logicLib, 'gameBoard')

# GUI
class TicTacToeGui:

    def __init__(self, mainWindow):

        # janela principal
        self.mainWindow = mainWindow
        self.mainWindow.title("Jogo da Velha (Python + C)")
        self.mainWindow.resizable(False, False) # n pode ser redimensionada nem em x nem em y (mudar?)

        self.currentPlayer = 'X' # comeca pelo jogador X
        self.isGameOver = False

        # widgets!
        boardFrame = tk.Frame(self.mainWindow)
        boardFrame.pack(pady=10) # espaco vertical

        # guardar os botoes do tabuleiro
        self.boardButtons = []
        for buttonIndex in range(9):
            row = buttonIndex // 3
            column = buttonIndex % 3
            
            # gera botao
            button = tk.Button(
                boardFrame,
                text=' ',
                font=('Arial', 24, 'bold'),
                height=2,
                width=5,
                command=lambda idx=buttonIndex: self.onButtonClick(idx) # n sei oq o lambda faz exatamente, so pesquisei e funciona
            )
            # coloca o botao no grid
            button.grid(row=row, column=column)
            self.boardButtons.append(button)

        # informacoes do jogador
        self.statusLabel = tk.Label(self.mainWindow, text=f"Jogador {self.currentPlayer}, sua vez", font=('Arial', 12))
        self.statusLabel.pack(pady=10)

        # botao de reiniciar
        restartButton = tk.Button(self.mainWindow, text="Reiniciar Jogo", command=self.restartGame)
        restartButton.pack(pady=10)
        
        # inicia o jogo
        self.restartGame()

    # tratamento ao clica no tabuleiro
    def onButtonClick(self, buttonIndex):
    
        # checa se o jogo terminou ou se o botao ja foi clicado
        if self.isGameOver or self.boardButtons[buttonIndex]['text'] != ' ':
            return

        # converte o caractere do jogador para o formato que a funcao C espera (bytes)
        playerAsByte = self.currentPlayer.encode('utf-8')

        # makeMove em C
        wasMoveSuccessful = logicLib.makeMove(buttonIndex, playerAsByte)

        # jogada valida (retorno 1)
        if wasMoveSuccessful:
            # atualiza interface
            self.boardButtons[buttonIndex].config(text=self.currentPlayer)
            self.checkGameStatus()
            
            if not self.isGameOver:
                self.switchPlayer()

    # troca o player
    def switchPlayer(self):
        if self.currentPlayer == 'X':
            self.currentPlayer = 'O'
        else:
            self.currentPlayer = 'X'
        
        self.statusLabel.config(text=f"Jogador {self.currentPlayer}, sua vez")

    def checkGameStatus(self):
        winner = logicLib.checkWinner().decode('utf-8') # # pega dado da funcao em C converte o byte pra string blablabla
        isDraw = logicLib.checkDraw()

        if winner != ' ':
            self.isGameOver = True
            self.statusLabel.config(text=f"O jogador '{winner}' venceu")
            messagebox.showinfo("Game Over", f"Parabens! O jogador '{winner}' venceu")

        elif isDraw:
            self.isGameOver = True
            self.statusLabel.config(text="Deu velha")
            messagebox.showinfo("Game Over", "O jogo empatou")

    def restartGame(self):
        self.isGameOver = False
        self.currentPlayer = 'X'
        
        self.statusLabel.config(text=f"Jogador {self.currentPlayer}, sua vez.")
        for button in self.boardButtons:
            button.config(text=' ', state=tk.NORMAL) # limpa os botoes da GUI

        # limpa os botoes logicamente
        logicLib.initBoard()

# ponto de entrada do programa
if __name__ == "__main__":
    # janela principal
    rootWindow = tk.Tk()
    gameApp = TicTacToeGui(rootWindow)
    rootWindow.mainloop()
