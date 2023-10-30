class TrieNode:
    """ TrieNode luokka 
        Attribuutit
        note_event :  "avain", jolla haetaan esim. generate.py rivi 40: (msg,note)
        children : solmun lapset
        count : esiintyvyydet, joiden perusteella todennäköisyys lasketaan """
    
    def __init__(self, note_event=None):
        self.note_event = note_event
        self.children = {}
        self.count = 0