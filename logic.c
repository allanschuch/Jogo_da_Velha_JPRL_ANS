#include <stdbool.h>

// ' ' eh um espaço vazio
char gameBoard[9] = {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '};

// inicia tabuleiro com tudo vazio logicamente
void initBoard() {
    for (int i = 0; i < 9; i++) {
        gameBoard[i] = ' ';
    }
}

// realiza jogada (1 se bem sucedida, 0 caso contrario)
int makeMove(int position, char player) {
    // verifica se esta dentro do limite e se a posicao ta vazia
    if (position >= 0 && position < 9 && gameBoard[position] == ' ') {
        gameBoard[position] = player;
        return 1; // deu bom
    }
    return 0; // n deu bom (posicao invalida)
}


// verifica condicoes de vitoria e retorna o simbolo do vencedor (X ou O) ou ' ' se n houver vencedor
char checkWinner() {
    int winConditions[8][3] = {
        {0, 1, 2}, {3, 4, 5}, {6, 7, 8}, // linhas
        {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, // colunas
        {0, 4, 8}, {2, 4, 6}             // diagonais
    };

/* isso ajuda:

     |     |
  0  |  1  |  2
-----------------
  3  |  4  |  5
-----------------
  6  |  7  |  8
     |     |
     
*/

    for (int i = 0; i < 8; i++) {
        int pos1 = winConditions[i][0];
        int pos2 = winConditions[i][1];
        int pos3 = winConditions[i][2];

        // se tres posicoes sao iguais e n estao vazias, alguem ganhou
        if (gameBoard[pos1] == gameBoard[pos2] && gameBoard[pos2] == gameBoard[pos3] && gameBoard[pos1] != ' ') {
            return gameBoard[pos1];
        }
    }

    return ' '; // ngm ganhou :( (ainda)
}

// checa empate (true = empate)
bool checkDraw() {
    // checa por espacos vazios
    for (int i = 0; i < 9; i++) {
        if (gameBoard[i] == ' ') {
            return false;
        }
    }

    return true;
}
