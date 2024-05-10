from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Generator, Any

@dataclass
class Node:
    name: type
    leafs: list[Any]



def parse(scanner, sintax, axiom, end, token_class):
    first = Node(object, [])
    tree_stack = [first]
    stack = [axiom]
    for token in scanner.tokens():
        while True:
            try:
                parent = tree_stack.pop()
            except IndexError:
                if issubclass(type(token), end):
                    break
                else:
                    raise IndexError
            rule = stack.pop()
            if issubclass(rule, token_class):
                if issubclass(type(token), rule):
                    parent.leafs.append(token)
                    break
                else:
                    print(f'Ожидался {rule} получен {type(token)} как  {token}')
                    raise Exception
            elif (rule, token.__class__.__bases__[0]) in sintax.keys():
                leaf = Node(rule, [])
                parent.leafs.append(leaf)
                to_add = sintax[(rule, token.__class__.__bases__[0])]
                for i in to_add[::-1]:
                    tree_stack.append(leaf)
                    stack.append(i)
                
            else:
                print(f'Ожидался {rule} получен {token.__class__.__bases__[0]}  как  {token}')
                raise Exception
    return first.leafs[0]