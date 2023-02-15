from typing import List


def get_user_words() -> List[str]:
    """Recebe as palavras do usuário e retorna uma lista com elas.
    Esta não é uma função pura, pois ela recebe dados do usuário."""
    x: List[str] = input('Digite as palavras separadas por espaço: ').split()
    return x


def count_quantity_letter_x_occurences(word: str) -> int:
    """Conta a quantidade de ocorrências da letra x em uma palavra.
    Esta é uma função pura, pois ela não recebe dados do usuário."""
    return word.count('x')


def inform_average_quantity_letter_x_occurences(words: List[str]) -> None:
    """Informa a média de ocorrências da letra x em uma lista de palavras.
    Esta não é uma função pura, pois ela usa uma função que não é pura."""
    total_occurences: int = 0
    total_lenght: int = 0
    for word in words:
        total_occurences += count_quantity_letter_x_occurences(word)
        total_lenght += len(word)
    average: float = (total_occurences / total_lenght) * 100
    print(f'A média de ocorrências da letra x é de {average:.0f}%\n')


def main() -> None:
    """Função principal.
    Esta não é uma função pura, pois ela usa uma função que não é pura."""
    words: List[str] = get_user_words()
    inform_average_quantity_letter_x_occurences(words)


if __name__ == '__main__':
    main()
