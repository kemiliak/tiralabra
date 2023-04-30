import random

# Trie-tietorakenne, joka tallentaa todennäköisyydet siirtymisestä yhdestä nuotista toiseen.
class Trie:
    def __init__(self, order):
        self.order = order
        self.root = TrieNode(None)

    def add_sequence(self, sequence):
        sequence = [None] * self.order + sequence + [None] * self.order
        for i in range(len(sequence) - self.order):
            fragment = tuple(sequence[i:i + self.order])
            self.root.insert(fragment, sequence[i + self.order])

    def generate_sequence(self, length, num_notes):
        current_node = self.root
        current_fragment = [None] * self.order
        sequence = []

        for i in range(length):
            current_node = current_node.get_child(tuple(current_fragment))
            if current_node is None:
                break
            next_element = random.choice(current_node.children)
            sequence.extend(next_element[:num_notes])
            current_fragment = current_fragment[1:] + next_element[:self.order-1]

        return sequence

# Tämä luokka edustaa solmua triessa. 
class TrieNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def get_child(self, value):
        for child in self.children:
            if child.value == value:
                return child
        return None

    def insert(self, sequence, value):
        if len(sequence) == 0:
            self.children.append((value,))
            return
        child = self.get_child(sequence[0])
        if child is None:
            child = TrieNode(sequence[0])
            self.children.append(child)
        child.insert(sequence[1:], value)