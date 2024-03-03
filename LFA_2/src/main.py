from finite_automaton import *
from graph_view import *

nfa = FiniteAutomaton(
    states=['0', '1', '2', '3'],
    alphabet=['a', 'b', 'c'],
    transitions={
        ('0', 'a'): ['0', '1'],
        ('2', 'a'): ['2'],
        ('1', 'b'): ['2'],
        ('2', 'c'): ['3'],
        ('3', 'c'): ['3']
    },
    start_state='0',
    final_states=['3']
)

print("Is NFA deterministic?")
print(is_deterministic(nfa))
visualize_finite_automaton(nfa, 'nfa')

print("\nDFA from NFA:")
dfa = convert_ndfa_to_dfa(nfa)
visualize_finite_automaton(dfa, 'dfa')
print(dfa)

rg = convert_to_regular_grammar(nfa)
print("\nRegular Grammar from NFA:")
for state, productions in rg.items():
    for production in productions:
        print(f"{state} -> {production}")