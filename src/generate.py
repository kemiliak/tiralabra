import random
from trie import TrieNode

class MarkovChain:
    """ Luokka Markovin ketjua hyödyntävälle Trielle 
        Attribuutit
        order : Markovin ketjun aste, määrittää kuinka monta edellistä nuottia otetaan huomioon
        start_states : lista kaikista mahdollisista aloitustiloista
        root : Trien juurisolmu """
    
    def __init__(self, order=4):
        self.order = order
        self.start_states = []
        self.root = TrieNode()

    
    def insert(self, notes):
        """ Metodi 'siirtymien' lisäämiseen, mikäli ei löydy triestä, lisätään se ja 
            kasvatetaan kyseistä 'count' arvoa (käytetään esiintyvyyksien todennäköisyyksien laskemiseen)
            Parametrit
            notes : lista nuoteista
            
            history : nykyinen arvo ja x määrä edellisiä, orderin mukaan"""

        history = [''] * self.order

        for msg,note,time in notes:
            
            state = tuple(history)
            self.start_states.append(state)

            current_node = self.root

            for step in state:
                if step not in current_node.children.keys():
                    current_node.children[step] = TrieNode(step)
                current_node = current_node.children[step]

            current_node.count += 1
            current_node.children[(msg,note)] = current_node.children.get((msg,note), TrieNode((msg,note)))
            current_node.children[(msg,note)].count += 1
            history.pop(0)
            history.append((msg,note))

    
    def generate(self, length):
        """ Funktio generoi sekvenssin todennäköisyyksien mukaan(funktioon on implementoitu trien haku (search funktio)).
            Ensin arvotaan aloitustila satunnaisesti, seuraava arvo/siirtymä arvotaan todennäköisyyksien mukaan,
        mitä suurempi count sitä suurempi todennäköisyys on olla seuraava nuotti.
        Parametri
        length : generoitavan sekvenssin pituus"""
        
        state = random.choice(self.start_states)
        history = list(state)
        notes = []

        for _ in range(length):
            node = self.root

            for step in state:
                if step in node.children:
                    node = node.children[step]
            
            total_count = sum(child_node.count for child_node in node.children.values())
            rand_val = random.randint(1, total_count)
            cumulative_count = 0
            for note, child_node in node.children.items():
                cumulative_count += child_node.count
                if rand_val <= cumulative_count:
                    selected_note = note
                    break
            
            notes.append((selected_note))
            history.pop(0)
            history.append(selected_note)
            state = tuple(history)

        return notes