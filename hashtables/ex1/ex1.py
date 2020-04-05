#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for w in range(0, len(weights)):
        hash_table_insert(ht, weights[w], w)

    response = None
    for w in range(0, len(weights)):
        findMatchIndex = hash_table_retrieve(ht, limit - weights[w])
        if findMatchIndex is not None and findMatchIndex != w:
            if findMatchIndex > w:
                response = (findMatchIndex, w)
                break
            else:
                response = (w, findMatchIndex)
                break

    return response


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
