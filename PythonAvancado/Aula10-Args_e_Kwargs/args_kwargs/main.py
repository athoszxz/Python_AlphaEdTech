def teste_args(a: str, b: str, *args):
    print(a)
    print(b)
    for arg in args:
        print(arg)


def multipy_args(*args):
    result = 1
    for arg in args:
        result *= arg
    return result


def teste_kwargs(a: str, b: int, **kwargs):
    print(a)
    print(b)
    for key, value in kwargs.items():
        print(f'{key} = {value}')


def main():
    print("Questão 1 - Args:")
    teste_args("brasil", "País", "Mundo", "Carro", 100, 50, "Pedra")
    print("\nQuestão 2 - Multiply Args:")
    print(multipy_args(10, 2, 4, 3))
    print("\nQuestão 3 - Kwargs:")
    teste_kwargs('Carro', 100, c='José', d='Teste', e='Brasil', f='Python')


if __name__ == '__main__':
    main()
