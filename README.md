# Simulador de Máquina de Turing

Trabalho 02 de Teoria da Computação (UFPI, Prof. Carlos André Batista de Carvalho).
Simulador de Máquina de Turing Determinística em Python, sem bibliotecas de autômatos.

> README inicial do repositório. A versão final (seções exigidas no enunciado) será escrita pela Pessoa 3.

## Divisão do trabalho

| Pessoa | Responsabilidade | Arquivos |
|---|---|---|
| Luidge de Sousa Carvalho | Leitura e validação do arquivo da MT, exemplos | `leitor.py`, `exemplos/` |
| Monnik Luianne Oliveira Nascimento Veloso Barbosa | Fita dinâmica e motor de execução | `fita.py`, `maquina.py`, `testes/` |
| Samuel Lucas Alves Matos | Exibição das CIs, Modo de Rastreio, CLI e README | `exibicao.py`, `main.py`, `README.md` |

## Contrato entre os módulos

**`leitor.ler(caminho)` → `mt`**

```python
mt = {
    "estados": {"q0", "q1", "q2"},
    "alfabeto_entrada": {"a", "b"},
    "alfabeto_fita": {"a", "b", "_"},
    "inicial": "q0",
    "finais": {"q2"},
    "delta": {("q0", "a"): ("q0", "a", "D"), ...},
    "cadeias": ["aabb", "abbb", "aba"],
}
```

**`maquina.executar(mt, cadeia, limite)` → `historico, resultado`**

```python
historico = [
    {"passo": 0, "estado": "q0", "fita": ["a", "a", "b", "b", "_"],
     "cabeca": 0, "transicao": None},
    {"passo": 1, "estado": "q0", "fita": [...], "cabeca": 1,
     "transicao": (("q0", "a"), ("q0", "a", "D"))},
]
resultado = {"status": "ACEITA" | "REJEITADA", "motivo": "..."}
```

**`exibicao.exibir(cadeia, historico, resultado, rastreio)`** imprime as CIs.

⚠️ Não mude o formato do contrato sem avisar o grupo.

## Como executar

```bash
python main.py exemplos/enunciado.json            # modo normal
python main.py exemplos/enunciado.json --rastreio # mostra as transições
python main.py exemplos/enunciado.json --limite 500
```

## Testes

```bash
python testes/teste_fita.py
python testes/teste_maquina.py
```

## Convenções

- Branco: `_`
- Direções: `E` (esquerda) e `D` (direita)
- Sem marcador de início; a fita cresce para os dois lados.
- Aceita ao entrar em estado final; rejeita quando não há transição ou ao atingir o limite de passos.

## Prazo

Entrega via SIGAA até **05/12**.
