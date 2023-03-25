# https://stackoverflow.com/questions/13101468/python-how-to-sort-the-alphabet-in-a-list-without-sorted-functions
def alptbabetical(lst):
    if not lst:
        return []
    return (quicksort([x for x in lst[1:] if x < lst[0]])
            + [lst[0]] +
            quicksort([x for x in lst[1:] if x >= lst[0]]))


def is_anagram(first_string, second_string):
    """Faça o código aqui."""

    first_string = alptbabetical(list(str.lower(first_string)))
    second_string = alptbabetical(list(str.lower(second_string)))

    if (first_string == '' and second_string == ''):
        return ("", "", False)
    return (
            ''.join(first_ordered),
            ''.join(second_ordered),
            first_ordered == second_ordered
        )
