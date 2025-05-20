def box(lines):
    """Exibe uma "caixinha" (ASCII) contendo as linhas passadas."""
    largura = max(len(l) for l in lines)
    borda = "+" + "-" * (largura + 2) + "+"
    print(borda)
    for linha in lines:
        print(f"| {linha.ljust(largura)} |")
    print(borda)


def saudacao():
    msg = [
        "Olá! Seja bem‑vindo à Calculadora",
        "Operações: +  -  *  /",
        "Digite 'sair' para encerrar."
    ]
    box(msg)


def calcular(a: float, b: float, op: str):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b if b != 0 else "Erro: divisão por zero"
    else:
        return "Operação inválida"


def loop_calculadora():
    saudacao()
    while True:
        op = input("Operação (+, -, *, /) ou 'sair': ").strip()
        if op.lower() == "sair":
            box(["Até logo! Obrigado por utilizar a calculadora."])
            break
        if op not in ["+", "-", "*", "/"]:
            box(["Operação inválida. Tente novamente."])
            continue
        try:
            a = float(input("Primeiro número: "))
            b = float(input("Segundo número: "))
        except ValueError:
            box(["Entrada inválida: digite números válidos."])
            continue
        resultado = calcular(a, b, op)
        box([f"Resultado: {a} {op} {b} = {resultado}"])


# Execução direta
loop_calculadora()