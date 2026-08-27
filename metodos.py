import numpy as np

# Formatação dos valores para historico de retorno
def add_historico(historico:list, k, x, fx, erro):
    registro = {
        "k": k,
        "x": x,
        "fx": fx,
        "erro": erro
    }
    historico.append(registro)

# ========= Davi =========
def bisseccao(f , a , b , eps=1e-8 , max_iter=200):
    historico = []

    # Validação da propriedade
    if f(a) * f(b) >= 0:
        raise ValueError("O produto f(a) * f(b) não é menor que 0.")

    #Definicao de intervalos
    inicio = a
    fim = b

    k = 0
    while(True):
        k += 1
        # Se max_iter for alcançada
        if (k > max_iter):
            print("Convergência não alcançada.")
            return (x, historico)

        #Definição dos Xk e Xk-1 junto do Erro
        if (k == 1):
            antigo_x = 0
            x = (inicio + fim)/2
            erro = '----'
        else:
            antigo_x = x
            x = (inicio + fim)/2
            erro = np.absolute(x - antigo_x)

        #Comparacões para retornar valor da raiz ou passar para a próxima análise
        if (f(x) == 0 or (fim - inicio) < eps):
            add_historico(historico, k, x, f(x), erro)
            return (x, historico)

        if (f(a)*f(x) < 0):
            add_historico(historico, k, x, f(x), erro)
            fim = x
        else:
            add_historico(historico, k, x, f(x), erro)
            inicio = x

#Teste Bissecção
def funcao_teste(x):
    return (x**2 - 1)
print(bisseccao(funcao_teste, 0, 2))


# ========= Gabriel =========
def newton(f, df, x0, eps=1e-8, max_iter =200):
    def funcao_f(x):
        return eval(f)

    def funcao_df(x):
        return eval(df)

    x_atual = x0

    for k in range(max_iter):
        fx = funcao_f(x_atual)
        dfx = funcao_df(x_atual)

        if dfx == 0:
            raise ValueError("O valor da derivada não pode ser 0.")

        x_next = x_atual - (fx / dfx)

        if abs(x_next - x_atual) < eps:
            print("Convergiu")
            return x_next

        x_atual = x_next
    print("Não convergiu: número máximo de iterações atingido.")
    return x_atual

# teste
raiz = newton(
    f="x**3 - 2",
    df="3**2",
    x0=1
)

print(raiz)


# ========= () =========
def secante (f , x0 , x1 , eps =1e-8 , max_iter =200):
    pass
