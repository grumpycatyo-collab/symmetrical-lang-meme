import random
from grammar import Grammar
from graph_view import visualize_finite_automaton
grammar = Grammar()
def print_generated_strings(grammar):
    strings = grammar.generate_strings()
    for s in strings:
        print(s)

print("Generated strings:")
print_generated_strings(grammar)

fa = grammar.to_finite_automaton()
print(fa)

def print_test(arr):
    print("String Validation:")
    for i in arr:
        if fa.accepts(i):
            print(f"{i} (belongs to the language)")
        else:
            print(f"{i} (doens't)")
arr = ["dd", "dabca", "bbca", "acac", "bad"]
print_test(arr)

visualize_finite_automaton(fa)