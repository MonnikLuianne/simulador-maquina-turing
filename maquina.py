"""
maquina.py - Motor de execução da Máquina de Turing Determinística (Pessoa 2)

Recebe a MT no formato do contrato (gerado por leitor.py) e uma cadeia,
executa a computação passo a passo e devolve o histórico de configurações
instantâneas e o resultado. Esta parte NÃO imprime nada: quem exibe é
exibicao.py.

Contrato de entrada (mt):
    {
        "estados": set, "alfabeto_entrada": set, "alfabeto_fita": set,
        "inicial": str, "finais": set,
        "delta": {(estado, simbolo_lido): (prox_estado, simbolo_escrito, direcao)},
        "cadeias": list
    }

Contrato de saída:
    historico = [ {"passo": int, "estado": str, "fita": list,
                   "cabeca": int, "transicao": ((q, s), (q', s', d)) | None}, ... ]
    resultado = {"status": "ACEITA" | "REJEITADA", "motivo": str}
"""

from fita import Fita

LIMITE_PADRAO = 1000


def _registrar(historico, passo, estado, fita, transicao):
    historico.append({
        "passo": passo,
        "estado": estado,
        "fita": fita.copia(),       # cópia! senão todos os passos apontam para a mesma lista
        "cabeca": fita.cabeca,
        "transicao": transicao,
    })


def executar(mt: dict, cadeia: str, limite: int = LIMITE_PADRAO):
    """
    Executa a MT sobre a cadeia.

    Critério de parada:
      - entrou em estado final          -> ACEITA
      - não há transição para (q, s)    -> REJEITADA (travamento)
      - atingiu o limite de passos      -> REJEITADA (possível loop)
    """
    fita = Fita(cadeia)
    estado = mt["inicial"]
    delta = mt["delta"]
    finais = mt["finais"]

    historico = []
    passo = 0
    _registrar(historico, passo, estado, fita, None)

    while True:
        # 1) Parada por aceitação
        if estado in finais:
            return historico, {
                "status": "ACEITA",
                "motivo": f"Parada em estado final {estado}",
            }

        # 2) Parada por limite de passos
        if passo >= limite:
            return historico, {
                "status": "REJEITADA",
                "motivo": f"Limite de {limite} passos atingido (possível loop)",
            }

        # 3) Busca a transição
        simbolo = fita.ler()
        chave = (estado, simbolo)
        if chave not in delta:
            return historico, {
                "status": "REJEITADA",
                "motivo": f"Travamento: não há transição para ({estado}, {simbolo})",
            }

        # 4) Aplica a transição: escreve, move, troca de estado
        prox_estado, escrito, direcao = delta[chave]
        fita.escrever(escrito)
        fita.mover(direcao)
        estado = prox_estado
        passo += 1

        _registrar(historico, passo, estado, fita, (chave, (prox_estado, escrito, direcao)))
