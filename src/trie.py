from collections import defaultdict

# TrieNode määrittelee jokaisen solmun rakenteen triessa 
class TrieNode:
    def __init__(self):
        self.children = defaultdict(int)
        self.count = 0