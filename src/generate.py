import random
from trie import Trie

# Funktio ottaa nuottijonon ja order-argumentin ja palauttaa MarkovTrie-olion, 
# joka edustaa nuottijonon Markov-mallia.
def generate_markov_model(note_sequence, order):
    trie = Trie(order)
    trie.add_sequence(note_sequence)
    return trie

# Funktio ottaa MarkovTrie-olion, joka edustaa Markov-mallia, length-argumentin, 
# joka edustaa generoitavan uuden nuottijonon pituutta, ja num_notes-argumentin, 
# joka edustaa generoitavien nuottien määrää kerralla. 
def generate_sequence_from_model(model, length, num_notes):
    current_node = model.root
    current_fragment = [None] * model.order
    sequence = []

    for i in range(length):
        current_node = current_node.get_child(tuple(current_fragment))
        if current_node is None:
            break
        next_element = random.choice(current_node.children)
        sequence.extend(next_element[:num_notes])
        current_fragment = current_fragment[1:] + next_element[:model.order-1]

    return sequence