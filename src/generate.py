import random
from collections import defaultdict
#import time
import mido
import music21 as m

# ei toimi tällä hetkellä


# MIDI tiedostoissa tarvittava tieto on tallennettu "note_on" kohtaan

# ladataan MIDI tiedosto
midi_file = mido.MidiFile('imperial.mid')

note_sequence = []
transition_dict = defaultdict(list)

for msg in midi_file.play():
    #print(msg)
    if msg.type == 'note_on':
        note_sequence.append(msg.note)

for i in range(len(note_sequence)-1):
    transition_dict[note_sequence[i]].append(note_sequence[i+1])

transition_trie = Trie()

for note, transitions in transition_dict.items():
    for transition in transitions:
        transition_trie.insert(str(note) + ',' + str(transition))


# generoidaan sekvenssi Markovin ketjua käyttäen
def generate_sequence(transition_dict, start_note, length):
    sequence = [start_note]
    current_note = start_note
    for i in range(length-1):
        possible_transitions = transition_dict[current_note]
        if not possible_transitions:
            break
        next_note = random.choice(possible_transitions)
        sequence.append(next_note)
        current_note = next_note
    return sequence

# valitaan aloittava nuotti ja tuotettava pituus
start_note = random.choice(0,127)
length = 100
new_sequence = generate_sequence(transition_dict, start_note, length)

# midiutil parempi? 
stream1 = m.stream.Stream()
for note in new_sequence:
    new_note = m.note.Note()
    new_note.pitch.midi = note
    stream1.append(new_note)

stream1.write('midi', fp='generated_music.mid')