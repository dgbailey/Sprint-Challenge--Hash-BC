#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)#started as 16
    for i in range(len(weights)):
        hash_table_insert(ht,weights[i],i)

    answer = None
   
    for i in range(len(weights)):
        search_value = limit - weights[i]

        result =  hash_table_retrieve(ht,search_value)
        print("Result",result)
        if result is not None:
            
            answer = [i,result]
            print("answernot NONE", answer)
            
        
    return answer
    """
    YOUR CODE HERE
    """




def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
