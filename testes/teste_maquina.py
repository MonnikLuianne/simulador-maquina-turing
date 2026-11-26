
"""Testes do motor com MTs escritas à mão (sem depender do leitor).
Rodar a partir da raiz: python testes/teste_maquina.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from maquina import executar

# MT do enunciado
MT_ENUNCIADO = {
    "estados": {"q0", "q1", "q2"},
    "alfabeto_entrada": {"a", "b"},
    "alfabeto_fita": {"a", "b", "_"},
    "inicial": "q0",
    "finais": {"q2"},
    "delta": {
        ("q0", "a"): ("q0", "a", "D"),
        ("q0", "b"): ("q1", "b", "D"),
        ("q1", "b"): ("q1", "b", "D"),
        ("q1", "_"): ("q2", "_", "D"),
    },
    "cadeias": ["aabb", "abbb", "aba"],
}

# MT que anda para a esquerda para sempre (testa loop e expansão à esquerda)
MT_LOOP = {
    "estados": {"q0"}, "alfabeto_entrada": {"a"}, "alfabeto_fita": {"a", "_"},
    "inicial": "q0", "finais": set(),
    "delta": {("q0", "a"): ("q0", "a", "E"), ("q0", "_"): ("q0", "_", "E")},
    "cadeias": ["a"],
}


def teste_aabb_aceita():
    hist, res = executar(MT_ENUNCIADO, "aabb")
    assert res["status"] == "ACEITA"
    assert len(hist) == 6                      # passos 0 a 5
    assert hist[-1]["estado"] == "q2"
    assert "".join(hist[-1]["fita"]) == "aabb__"


def teste_abbb_aceita():
    _, res = executar(MT_ENUNCIADO, "abbb")
    assert res["status"] == "ACEITA"


def teste_aba_rejeita():
    hist, res = executar(MT_ENUNCIADO, "aba")
    assert res["status"] == "REJEITADA"
    assert "Travamento" in res["motivo"]
    assert hist[-1]["estado"] == "q1"


def teste_vazia_rejeita():
    _, res = executar(MT_ENUNCIADO, "")
    assert res["status"] == "REJEITADA"


def teste_historico_e_copia():
    hist, _ = executar(MT_ENUNCIADO, "aabb")
    assert hist[0]["fita"] is not hist[1]["fita"]
    assert hist[0]["transicao"] is None
    assert hist[1]["transicao"] == (("q0", "a"), ("q0", "a", "D"))


def teste_loop_limite():
    hist, res = executar(MT_LOOP, "a", limite=50)
    assert res["status"] == "REJEITADA" and "loop" in res["motivo"]
    assert len(hist) == 51


def teste_inicial_final():
    mt = dict(MT_ENUNCIADO, finais={"q0"})
    hist, res = executar(mt, "ab")
    assert res["status"] == "ACEITA" and len(hist) == 1


if __name__ == "__main__":
    for nome, func in list(globals().items()):
        if nome.startswith("teste_"):
            func()
            print(f"OK  {nome}")
    print("\nHistórico de 'aabb':")
    hist, res = executar(MT_ENUNCIADO, "aabb")
    for ci in hist:
        print(ci["passo"], ci["estado"], "".join(ci["fita"]), "cabeça =", ci["cabeca"])
    print(res)
    print("\nTodos os testes do motor passaram.")
