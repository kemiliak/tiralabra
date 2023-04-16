import random
from collections import defaultdict
import time
import mido
from midiutil import MIDIFile
from generate import generate_sequence
from trie import Trie, TrieNode

midi_file = mido.MidiFile('../imperial.mid')

note_sequence = []
transition_dict = defaultdict(list)

for msg in midi_file.play():
    if msg.type == 'note_on':
        note_sequence.append(msg.note)

for i in range(len(note_sequence)-1):
    transition_dict[note_sequence[i]].append(note_sequence[i+1])

transition_trie = Trie()

for note, transitions in transition_dict.items():
    for transition in transitions:
        transition_trie.insert(str(note) + ',' + str(transition))

start_note = 53
length = 100
new_sequence = generate_sequence(transition_dict, start_note, length)

# Luodaan miditiedosto luodulla sekvenssillä
midi_file = MIDIFile(numTracks=1)
track = 0
midi_time = 0
tempo = 120
midi_file.addTrackName(track, midi_time, "Generated Music")
midi_file.addTempo(track, midi_time, tempo)

for note in new_sequence:
    pitch = note
    duration = 1
    volume = 100
    midi_file.addNote(track, 0, pitch, midi_time, duration, volume)
    midi_time += 1

with open('generated_music.mid', 'wb') as file:
    midi_file.writeFile(file)

output = mido.open_output()
midi_file = mido.MidiFile('generated_music.mid')
for msg in midi_file.play():
    output.send(msg)
    time.sleep(msg.time)