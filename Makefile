CC = gcc

PYTHON = python3

SRC = logic.c

LIB_NAME = logic.so
CFLAGS = -shared -fPIC
RM = rm -f

ifeq ($(OS),Windows_NT)
    LIB_NAME = logic.dll
    CFLAGS = -shared
    RM = del
endif

all: $(LIB_NAME)

$(LIB_NAME): $(SRC)
	$(CC) $(CFLAGS) -o $(LIB_NAME) $(SRC)

run: all
	$(PYTHON) game.py

clean:
	$(RM) $(LIB_NAME)

.PHONY: all run clean
