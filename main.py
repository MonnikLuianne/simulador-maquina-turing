"""
main.py - Ponto de entrada (Pessoa 3)
Uso: python main.py exemplos/enunciado.json [--rastreio] [--limite N]
"""
import argparse

from leitor import ler
from maquina import executar, LIMITE_PADRAO
from exibicao import exibir


def main():
    p = argparse.ArgumentParser(description="Simulador de Máquina de Turing Determinística")
    p.add_argument("arquivo", help="arquivo JSON com a definição da MT")
    p.add_argument("--rastreio", action="store_true", help="mostra a transição usada em cada passo")
    p.add_argument("--limite", type=int, default=LIMITE_PADRAO, help="limite de passos (detecção de loop)")
    args = p.parse_args()

    mt = ler(args.arquivo)
    for cadeia in mt["cadeias"]:
        historico, resultado = executar(mt, cadeia, args.limite)
        exibir(cadeia, historico, resultado, args.rastreio)


if __name__ == "__main__":
    main()

