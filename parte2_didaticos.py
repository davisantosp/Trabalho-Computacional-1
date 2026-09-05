import numpy as np
import metodos as mt
import pandas as pd

# Ex 2.1 Isolamento
def tabelar_sinais(f, a, b, n):
    lista_pontos = np.linspace(a, b, n)

    intervalos = []
    for i in range(n - 1):
        xn = lista_pontos[i]
        xm = lista_pontos[i+1]
        if f(xn) * f(xm) < 0:
            intervalos.append((xn, xm))

    return intervalos

def ex_2_1():
    # Ex 2.1.a
    f = lambda x: x**3 - 9*x + 3 # Função Teste
    a = -5
    b = 5
    n = [21, 11, 6, 4] # Numero de Divisões do Intervalo

    count_intervalos = []
    for i in n:
        intervalos = tabelar_sinais(f, a, b, i)

        # Adiciona a quantia de intervalos que satisfazem f(a)*f(b) < 0 ou seja que possuem raiz
        count_intervalos.append(len(intervalos))

    if (max(count_intervalos) != min(count_intervalos)):
        print(f"[ Ex_2.1.a ] Número diferente de raízes encontradas")
    else:
        print(f"[ Ex_2.1.a ] Mesmo número de raízes encontradas")


    #Ex 2.1.b
    g = lambda x: (x - 1.05)*(x - 1.15)*(x - 3)
    a = 0
    b = 4
    n = [9, 17, 41, 401]
    numero_raizes_real = 3

    count_intervalos = []
    for i in n:
        intervalos = tabelar_sinais(g, a, b, i)

        # Adiciona a quantia de intervalos que satisfazem f(a)*f(b) < 0 ou seja que possuem raiz
        count_intervalos.append(len(intervalos))

    for i, quantidade in enumerate(count_intervalos):
        print(f'[ Ex_2.1.b ] Raízes encontradas para n={n[i]}: {quantidade}')

    print(f"[ Ex_2.1.b ] Quantia real de raízes {numero_raizes_real}")
    if min(count_intervalos) == max(count_intervalos) and min(count_intervalos) == numero_raizes_real:
        print(f"[ Ex_2.1.b ] Quantia de raízes igual ao esperado.")
    else:
        print(f"[ Ex_2.1.b ] Divergência de quantia de raízes analisadas com real.")


# Ex 2.2 Previsão x realidade na bissecção
def ex_2_2():
    f = lambda x: x**3 - 9*x + 3 # Função Teste
    eps = [1e-2, 1e-4, 1e-6, 1e-8, 1e-10]

    # Limites do Intervalo
    a = 0
    b = 1

    # Fórmula da previsão de iterações com np.ceil necessário para encontrar o menor inteiro maior que o valor tal que k > valor
    formula_previsao = lambda a0, b0, e: np.ceil((np.log(b0 - a0) - np.log(e)) / np.log(2))

    # Cálculo da quantia de iterações a partir de cada eps
    resultados = []
    for e in eps:
        k_previsao = int(formula_previsao(a, b, e))

        # Recebe os resultados em histórico da bissecção e formata tal que (<valor de eps>, <k_efetivo>)
        raiz, historico = mt.bisseccao(f, a, b, e)
        k_efetivo = historico[-1]['k']

        resultados.append({'eps': e, 'k_previsao': k_previsao, 'k_efetivo': k_efetivo})

    # Formatação em tabela do resultado
    df = pd.DataFrame(resultados)
    print("[ Ex_2.2   ]")
    print(df)

# Ex 2.3 Custo real: avaliações de função
def ex_2_3():
    pass


ex_2_1()
ex_2_2()