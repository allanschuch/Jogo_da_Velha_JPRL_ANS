# Jogo da Velha com Python e C

Este é um projeto simples que implementa o clássico Jogo da Velha. A sua particularidade está na arquitetura: a interface gráfica (GUI) foi desenvolvida em **Python** com a biblioteca **Tkinter**, enquanto toda a lógica do jogo (regras, tabuleiro, verificação de vencedor) foi escrita em **C**.

As duas partes se comunicam através da biblioteca `ctypes` do Python, que carrega o código C compilado como uma biblioteca compartilhada (`.so` no Linux ou `.dll` no Windows).

## Estrutura do Projeto
```
/
|-- logic.c          # A lógica do jogo em C
|-- game.py       # A interface gráfica em Python
|-- Makefile          # Arquivo para automatizar a compilação
`-- README.md         # Este arquivo
```

## Pré-requisitos

Para compilar e executar este projeto, você precisará de:

1.  **Python 3**: [python.org](https://www.python.org/)
2.  **Tkinter**: Geralmente vem com o Python, mas em algumas distribuições Linux (como Debian/Ubuntu) precisa ser instalado separadamente:
    ```bash
    sudo apt-get install python3-tk
    ```
3.  **Compilador C**: O `gcc` é recomendado.
    * **Linux**: Geralmente já vem instalado ou pode ser obtido com `sudo apt-get install build-essential`.
    * **Windows**: Recomenda-se o [MinGW-w64](https://www.mingw-w64.org/).
4.  **Make**: Ferramenta para automatizar a compilação (opcional, mas recomendado).
    * **Linux**: Geralmente já vem com o `build-essential`.
    * **Windows**: Vem com as ferramentas do MinGW ou pode ser instalado separadamente.

## Como Construir e Executar

### Método 1: Usando o Makefile (Recomendado)

Abra um terminal na pasta do projeto e use os seguintes comandos:

1.  **Para compilar o código C:**
    ```bash
    make
    ```
2.  **Para rodar o jogo (compila se necessário e executa):**
    ```bash
    make run
    ```
3.  **Para limpar os arquivos compilados:**
    ```bash
    make clean
    ```

### Método 2: Manualmente

Se você não tem ou não quer usar o `make`, siga estes passos:

1.  **Compile o código C:**
    * No **Linux** ou **macOS**:
        ```bash
        gcc -shared -o logic.so -fPIC logic.c
        ```
    * No **Windows**:
        ```bash
        gcc -shared -o logic.dll logic.c
        ```

2.  **Execute o script Python:**
    ```bash
    python3 game.py
    ```
