class FiniteAutomaton:
    def __init__(self, states, alphabet, transitions, start_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = {k: v if isinstance(v, list) else [v] for k, v in transitions.items()}
        self.start_state = start_state
        self.final_states = final_states

    def __str__(self):
        fa_representation = "\n"
        fa_representation += f"States: {self.states}\n"
        fa_representation += f"Alphabet: {self.alphabet}\n\n"
        fa_representation += "Transitions:\n"
        fa_representation += "It's read as: δ(state, symbol) = next_state\n"
        for (state, symbol), next_states in self.transitions.items():
            fa_representation += f"    δ({state}, '{symbol}') = {next_states}\n"
        fa_representation += f"Start State: {self.start_state}\n"
        fa_representation += f"Final States: {self.final_states}\n"
        return fa_representation



def convert_to_regular_grammar(fa):
    """
    Converts a finite automaton to a regular grammar.

    Args:
        fa (FiniteAutomaton): The finite automaton to be converted.

    Returns:
        dict: The regular grammar representation of the finite automaton.
    """
    grammar = {}
    for (state, symbol), next_states in fa.transitions.items():
        if state not in grammar:
            grammar[state] = []
        for next_state in next_states:
            grammar[state].append(f"{symbol}{next_state}")
    for final_state in fa.final_states:
        if final_state in grammar:
            grammar[final_state].append("ε")  # ε represents the empty string
        else:
            grammar[final_state] = ["ε"]
    return grammar


def is_deterministic(fa):
    """
    Check if a finite automaton is deterministic.

    Args:
        fa (FiniteAutomaton): The finite automaton to check.

    Returns:
        bool: True if the finite automaton is deterministic, False otherwise.
    """
    for next_states in fa.transitions.values():
        if len(next_states) > 1:
            return False
    return True


def convert_ndfa_to_dfa(ndfa):
    """
    Converts a non-deterministic finite automaton (NDFA) to a deterministic finite automaton (DFA).

    Args:
        ndfa (FiniteAutomaton): The NDFA to be converted.

    Returns:
        FiniteAutomaton: The DFA resulting from the conversion.
    """
    dfa_states = {frozenset([ndfa.start_state]): '0'}  
    dfa_transitions = {}
    dfa_final_states = []
    unmarked_states = [frozenset([ndfa.start_state])]

    while unmarked_states:
        current_dfa_state = unmarked_states.pop()
        for symbol in ndfa.alphabet:
            next_states = set()
            for ndfa_state in current_dfa_state:
                if (ndfa_state, symbol) in ndfa.transitions:
                    next_states.update(ndfa.transitions[(ndfa_state, symbol)])
            if not next_states:
                continue
            next_states_frozenset = frozenset(next_states)
            if next_states_frozenset not in dfa_states:
                new_state_name = str(len(dfa_states)) 
                dfa_states[next_states_frozenset] = new_state_name
                unmarked_states.append(next_states_frozenset)
            dfa_transitions[(dfa_states[current_dfa_state], symbol)] = dfa_states[next_states_frozenset]

    for dfa_state, label in dfa_states.items():
        if any(state in ndfa.final_states for state in dfa_state):
            dfa_final_states.append(label)

    return FiniteAutomaton(list(dfa_states.values()), ndfa.alphabet, dfa_transitions, '0', dfa_final_states)
