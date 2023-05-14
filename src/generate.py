import random
from collections import defaultdict
from trie import TrieNode

class MarkovChain:
    def __init__(self, order=1):
        self.order = order
        self.start_states = []
        self.transition_matrix = defaultdict(TrieNode)

    # funktio kouluttaa Markovin ketjun käymällä läpi kaikki nuotit ja päivittämällä siirtymiä
    def train(self, notes):
        history = [''] * self.order

        for note in notes:
            state = tuple(history)

            if history == [''] * self.order:
                self.start_states.append(state)

            self.transition_matrix[state].count += 1
            self.transition_matrix[state].children[note] += 1

            history.pop(0)
            history.append(note)

    # funktio generoi uuden nuottisekvenssin siirtymien perusteella
    def generate(self, length):
        state = random.choice(self.start_states)
        history = list(state)

        notes = []

        for _ in range(length):
            node = self.transition_matrix[state]
            total_count = node.count

            if total_count == 0 or len(node.children) == 0:
                note = random.choice(list(self.transition_matrix.keys()))
            else:
                rand_val = random.randint(1, total_count)
                for note, count in node.children.items():
                    rand_val -= count
                    if rand_val <= 0:
                        break

            notes.append(note)
            state = tuple(history)
            history.pop(0)
            history.append(note)

        return notes