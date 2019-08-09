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
    hashtable = HashTable(length)
    route = ["NONE"] * length

    for i in range(len(tickets)):
        hash_table_insert(hashtable,tickets[i].source,tickets[i].destination)

    current_route = hash_table_retrieve(hashtable,"NONE")#not sure how this gets hashed
    route_index = 0
    while current_route != "NONE":
        route[route_index] = current_route
        print(route)
        current_route = hash_table_retrieve(hashtable,current_route)
        route_index += 1

    """
    YOUR CODE HERE
    """

    return route
