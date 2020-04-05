#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * (length - 1)

    """
    YOUR CODE HERE
    """
    for t in range(0, length):
        hash_table_insert(ht, tickets[t].source, tickets[t].destination)

    lastKey = "NONE"
    for t in range(0, length):
        foundDestination = hash_table_retrieve(ht, lastKey)
        if foundDestination is not None and foundDestination is not "NONE":
            route[t] = foundDestination
            lastKey = foundDestination

    return route
