"""
leitor.py - Leitura e validação do arquivo da MT (Pessoa 1)

Deve devolver o dicionário mt no formato do contrato:
    {"estados": set, "alfabeto_entrada": set, "alfabeto_fita": set,
     "inicial": str, "finais": set,
     "delta": {(estado, simbolo): (prox_estado, escrito, direcao)},
     "cadeias": list}
"""


def ler(caminho: str) -> dict:
    raise NotImplementedError("Pessoa 1: implementar leitura e validação")

