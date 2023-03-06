from typing import Tuple
from timer import timer



@timer
def locate_clause(text:str, clause:str) -> Tuple[int, int]:
    """Assumptions:
        Either or both the start or end of the clause is contained in the text
    """
    # full match 
    index = text.find(clause)
    if index != -1:
        print(" ", text[index: index+len(clause)])
        return index, index+len(clause)-1
    # forward pass ie. end of clause cut off
    len_text = len(text)
    len_clause = len(clause)
    for i in reversed(range(1, len(clause))): 
        if text[-i:] == clause[:i]:
            print(" ", text[-i: len_text])
            return len_text-i, len_text-1
    # backward pass ie. start of clause cut off
    for i in reversed(range(len(clause))): 
        if text[:i] == clause[-i:]:
            print(" ", text[0: i+1])
            return 0, i-1
