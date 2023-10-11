class TrieNode:
    # TrieNode luokka
    def __init__(self, note_event=None):
        self.note_event = note_event
        self.children = {}
        self.count = 0