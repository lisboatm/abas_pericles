# Leitura dos valores iniciais
N, M = map(int, input().split())

# Inicializa o número de abas
abas = N

# Processa as ações
for _ in range(M):
    acao = input().strip()  # Lê a ação e remove espaços em branco
    if acao == "fechou":
        abas += 1  # Aumenta uma aba
    elif acao == "clicou":
        abas -= 1  # Diminui uma aba

# Garante que o número de abas não fique negativo
abas = max(abas, 0)

# Impressão do número final de abas
print(abas)
