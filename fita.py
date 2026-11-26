"""
fita.py - Fita da Máquina de Turing (Pessoa 2)

A fita é uma lista de símbolos que cresce sob demanda nos dois sentidos,
simulando a fita infinita. Toda posição nunca visitada contém o branco "_".
"""

BRANCO = "_"


class Fita:
    def __init__(self, cadeia: str):
        # A cadeia é escrita a partir da posição 0, seguida de um branco.
        # Cadeia vazia -> fita com um único branco.
        self.celulas = list(cadeia) + [BRANCO]
        self.cabeca = 0

    def ler(self) -> str:
        """Retorna o símbolo sob a cabeça."""
        return self.celulas[self.cabeca]

    def escrever(self, simbolo: str) -> None:
        """Escreve um símbolo na posição da cabeça."""
        self.celulas[self.cabeca] = simbolo

    def mover(self, direcao: str) -> None:
        """
        Move a cabeça uma posição.
        D -> direita: se passar do fim, acrescenta um branco no final.
        E -> esquerda: se passar do início, insere um branco no começo
             (a cabeça continua no índice 0, que agora é a nova célula).
        """
        if direcao == "D":
            self.cabeca += 1
            if self.cabeca == len(self.celulas):
                self.celulas.append(BRANCO)
        elif direcao == "E":
            if self.cabeca == 0:
                self.celulas.insert(0, BRANCO)
            else:
                self.cabeca -= 1
        else:
            raise ValueError(f"Direção inválida: {direcao!r} (use 'E' ou 'D')")

    def copia(self) -> list:
        """Cópia do conteúdo atual (usada para registrar o histórico)."""
        return list(self.celulas)

    def __str__(self) -> str:
        return "".join(self.celulas)
