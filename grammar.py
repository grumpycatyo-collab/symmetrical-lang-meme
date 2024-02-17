import random
from finite_automaton import FiniteAutomaton
class Grammar:
    def __init__(self):
        self.nonterminals = {'S', 'A', 'B', 'C'}
        self.terminals = {'a', 'b', 'c', 'd'}
        self.productions = {
            'S': ['dA'],
            'A': ['d', 'aB'],
            'B': ['bC'],
            'C': ['cA', 'aS']
        }
        self.start_symbol = 'S'

    def generate_strings(self, count=5):
        strings = []
        while len(strings) < count:
            string = self._generate_from_symbol(self.start_symbol)
            if string not in strings:
                strings.append(string)
        return strings

    def _generate_from_symbol(self, symbol):
        if symbol in self.terminals:
            return symbol
        else:
            production = self.productions[symbol]
            chosen_production = random.choice(production)
            return ''.join(self._generate_from_symbol(sym) for sym in chosen_production)
        
    def to_finite_automaton(grammar):
        states = grammar.nonterminals.union({'FINAL'})
        alphabet = grammar.terminals
        transitions = {}
        final_states = {'FINAL'}

        for nonterminal, production_list in grammar.productions.items():
            for production in production_list:
                if len(production) == 1:  # A -> a
                    terminal = production
                    transitions[(nonterminal, terminal)] = {'FINAL'}
                elif len(production) == 2:  # A -> aB
                    terminal, next_nonterminal = production
                    if (nonterminal, terminal) not in transitions:
                        transitions[(nonterminal, terminal)] = set()
                    transitions[(nonterminal, terminal)].add(next_nonterminal)

        start_state = grammar.start_symbol
        return FiniteAutomaton(states, alphabet, transitions, start_state, final_states)
        