
class Grammar:
    """
    Represents a grammar with nonterminals, terminals, productions, and a start symbol.
    """

    def __init__(self, nonterminals=None, terminals=None, productions=None, start_symbol=None):
        """
        Initializes the Grammar object.

        Args:
            nonterminals (set): Set of nonterminal symbols.
            terminals (set): Set of terminal symbols.
            productions (dict): Dictionary representing the productions.
            start_symbol (str): Start symbol of the grammar.
        """
        self.nonterminals = nonterminals if nonterminals is not None else {'S', 'A', 'B', 'C'}
        self.terminals = terminals if terminals is not None else {'a', 'b', 'c', 'd'}
        self.productions = productions if productions is not None else {
            'S': ['dA'],
            'A': ['d', 'aB'],
            'B': ['bC'],
            'C': ['cA', 'aS']
        }
        self.start_symbol = start_symbol if start_symbol is not None else 'S'

    def classify_grammar(self):
        for lhs, rhs_list in self.productions.items():
            for rhs in rhs_list:
                if len(lhs) > len(rhs) or (len(lhs) > 1 and any(char in self.nonterminals for char in lhs)):
                    return "UNRESTRICTED"

                if len(lhs) != 1 or lhs not in self.nonterminals:
                    return "CONTEXT_SENSITIVE"
                
        is_right_linear = any(all(symbol in self.terminals for symbol in rhs[:-1]) and rhs[-1] in self.nonterminals for rhs_list in self.productions.values() for rhs in rhs_list)
        is_left_linear = any(rhs[0] in self.nonterminals and all(symbol in self.terminals for symbol in rhs[1:]) for rhs_list in self.productions.values() for rhs in rhs_list)

        if is_right_linear and not is_left_linear:
            return "REGULAR_RIGHT_LINEAR"
        elif is_left_linear and not is_right_linear:
            return "REGULAR_LEFT_LINEAR"

        return "CONTEXT_FREE"



# Type 1
non_terminals = {'S', 'A'}
terminals = {'a', 'b', 'c'}
rules = {
    'S': ['AB'],
    'A': ['aB'],
    'B': ['b']
}
grammar = Grammar(non_terminals, terminals, rules)
print(grammar.classify_grammar())


#Type 0
non_terminals = {'S', 'A'}
terminals = {'a', 'b'}
rules = {
    'Sab': ['ba'],
    'A': ['S']
}
grammar = Grammar(non_terminals, terminals, rules)
print(grammar.classify_grammar())


# Type 3 (left linear)
non_terminals = ['S', 'B', 'C', 'D']
terminals = ['a', 'b', 'c']
rules = {
    'S': ['Ba', 'Baa'],
    'B': ['Sb', 'Ca', 'c'],
    'C': ['Db'],
    'D': ['c', 'Ca']
}
grammar = Grammar(non_terminals, terminals, rules)
print(grammar.classify_grammar())

# Type 2
non_terminals = {'S', 'A', 'B'}
terminals = {'a', 'b', 'c'}
rules = {
    'S': ['ABa'],
    'A': ['a'],
    'B': ['b']
}
grammar = Grammar(non_terminals, terminals, rules)
print(grammar.classify_grammar())  


# Type 3 (right linear)
non_terminals = ['S', 'B', 'C', 'D']
terminals = ['a', 'b', 'c']
rules = {
    'S': ['aB', 'aB'],
    'B': ['bS', 'aC', 'c'],
    'C': ['bD'],
    'D': ['c', 'aC']
}
grammar = Grammar(non_terminals, terminals, rules)
print(grammar.classify_grammar())


print(Grammar().classify_grammar())