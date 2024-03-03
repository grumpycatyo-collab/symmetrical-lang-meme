from graphviz import Digraph

def visualize_finite_automaton(fa, file_name):
    dot = Digraph(comment='Finite Automaton')

    # Add states to the graph
    for state in fa.states:
        if state in fa.final_states:
            dot.attr('node', shape='doublecircle')
        else:
            dot.attr('node', shape='circle')
        dot.node(state)

    # Add transitions to the graph
    for (state, symbol), next_states in fa.transitions.items():
        for next_state in next_states:
            dot.edge(state, next_state, label=symbol)

    # Mark the start state with an edge
    dot.attr('node', shape='none')
    start = 'start'
    dot.node(start, label='')
    dot.edge(start, fa.start_state)

    # Render the graph to a file (e.g., 'finite_automaton.gv')
    dot.render(file_name, view=True)

