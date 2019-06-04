#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Descubram a quantidade de buracos que existe nas letras que formam uma palavra
'''

import sys

def num_buracos(param=None):
    '''
    Initializations. our codebook is:
    a b c d e f g e h j l m n o p q r s t u v w x y z
    A B C D E F G E H J L M N O P Q R S T U V W X Y Z
    * *   *     *             * * * *
    please notice that B has 2 holes while b is just 1
    '''
    codebook = {
        'A': 1,
        'B': 2,
        'D': 1,
        'O': 1,
        'P': 1,
        'Q': 1,
        'R': 1,
        'a': 1,
        'b': 1,
        'd': 1,
        'g': 1,
        'e': 1,
        'o': 1,
        'p': 1,
        'q': 1
    }
    num_holes, total_holes = (0, 0)

    ## checking if the parameter is a list of strings
    if param and isinstance(param, list):
        if all(isinstance(elem, str) for elem in param):
            for word in param:
                for char in word:
                    if char in codebook:
                        num_holes += codebook[char]
                print(f"palavra '{word}' contém '{num_holes}' buraco(s)")
                total_holes += num_holes
                num_holes = 0
            print(f"total de '{total_holes}' buraco(s)")
            return total_holes
    ## checking if parameter is just 1 string
    elif param and isinstance(param, str):
        for char in param:
            if char in codebook:
                num_holes += codebook[char]
        print(f"palavra '{param}' contém '{num_holes}' buraco(s)")
        return num_holes
    return False


####### MAIN ########
if __name__ == "__main__":
    USERARGS = sys.argv[1:] or list()
    if USERARGS:
        print("No args! expecting a list of words")
        sys.exit(-1)
    else:
        RET = num_buracos(USERARGS)
        sys.exit(RET)
