
"""Testes da fita dinâmica. Rodar a partir da raiz: python testes/teste_fita.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from fita import Fita


def teste_inicial():
    f = Fita("ab")
    assert f.celulas == ["a", "b", "_"] and f.cabeca == 0 and f.ler() == "a"


def teste_cadeia_vazia():
    f = Fita("")
    assert f.celulas == ["_"] and f.ler() == "_"


def teste_expande_direita():
    f = Fita("a")
    for _ in range(4):
        f.mover("D")
    assert f.celulas == ["a", "_", "_", "_", "_"] and f.cabeca == 4


def teste_expande_esquerda():
    f = Fita("ab")
    f.mover("E")
    f.mover("E")
    assert f.celulas == ["_", "_", "a", "b", "_"] and f.cabeca == 0
    f.mover("D"); f.mover("D")
    assert f.ler() == "a"


def teste_escrever():
    f = Fita("ab")
    f.escrever("X")
    assert str(f) == "Xb_"


def teste_direcao_invalida():
    try:
        Fita("a").mover("C")
        assert False, "deveria ter lançado ValueError"
    except ValueError:
        pass


if __name__ == "__main__":
    for nome, func in list(globals().items()):
        if nome.startswith("teste_"):
            func()
            print(f"OK  {nome}")
    print("Todos os testes da fita passaram.")
