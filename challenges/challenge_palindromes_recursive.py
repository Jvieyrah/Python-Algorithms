def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    # Verifica se a string está vazia
    if len(word) == 0:
        return False
    # Verifica se um lado da string é igual a seu indice do lado equivalente oposto
    elif low_index >= high_index:
        return True
    elif word[low_index] != word[high_index]:
        return False
    else:
    #repete o processo para o proximo ṕar de indices até concluir.
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    