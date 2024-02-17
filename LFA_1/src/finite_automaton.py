import random
class FiniteAutomaton:
    """
    Represents a finite automaton.

    Attributes:
        states (list): List of states in the automaton.
        alphabet (list): List of symbols in the alphabet of the automaton.
        transitions (dict): Dictionary representing the transitions of the automaton.
            The keys are tuples of the form (state, symbol), and the values are lists of next states.
        start_state: The start state of the automaton.
        final_states (list): List of final states in the automaton.
    """

    def __init__(self, states, alphabet, transitions, start_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.final_states = final_states

    def __str__(self):
        fa_representation = "Finite Automaton:\n"
        fa_representation += f"States: {self.states}\n"
        fa_representation += f"Alphabet: {self.alphabet}\n"
        fa_representation += "Transitions: {\n"
        for (state, symbol), next_states in self.transitions.items():
            for next_state in next_states:
                fa_representation += f"    '{state}' ('{symbol}': {next_state}),\n"
        fa_representation += "}\n"
        fa_representation += f"Start State: {self.start_state}\n"
        fa_representation += f"Final States: {self.final_states}\n"
        return fa_representation

    def accepts(self, string):
        """
        Determines whether the automaton accepts a given string.

        Args:
            string (str): The input string.

        Returns:
            bool: True if the automaton accepts the string, False otherwise.
        """
        def _accepts(state, remaining_string):
            if not remaining_string:
                return state in self.final_states
            current_char = remaining_string[0]
            if (state, current_char) in self.transitions:
                for next_state in self.transitions[(state, current_char)]:
                    if _accepts(next_state, remaining_string[1:]):
                        return True
            return False

        return _accepts(self.start_state, string)

