import unittest
from collections import defaultdict
from midiutil import MIDIFile
import mido
import random
import time
from src.trie import Trie


def parse_midi_file(midi_file):
    note_sequence = []
    transition_dict = defaultdict(list)

    for msg in midi_file.play():
        if msg.type == 'note_on':
            note_sequence.append(msg.note)

    for i in range(len(note_sequence)-1):
        transition_dict[note_sequence[i]].append(note_sequence[i+1])

    return note_sequence, transition_dict

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


class TestMusicGeneration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Ladataan midi tiedostot
        cls.imperial_midi = mido.MidiFile('imperial.mid')
        cls.generated_music_midi = mido.MidiFile('src/generated_music.mid')

        # Jäsentely
        cls.imperial_note_sequence, cls.imperial_transition_dict = parse_midi_file(cls.imperial_midi)
        cls.generated_music_note_sequence, cls.generated_music_transition_dict = parse_midi_file(cls.generated_music_midi)

        # Trien alustus
        cls.transition_trie = Trie()
        for note, transitions in cls.imperial_transition_dict.items():
            for transition in transitions:
                cls.transition_trie.insert(str(note) + ',' + str(transition))

    def test_generate_sequence(self):
        start_note = 92
        length = 100
        sequence = generate_sequence(self.imperial_transition_dict, start_note, length)
        self.assertEqual(len(sequence), length)

    def test_generated_music_sequence(self):
        self.assertTrue(self.generated_music_note_sequence)

    def test_transition_trie(self):
        note = 60
        transition = 62
        self.assertTrue(self.transition_trie.search(str(note) + ',' + str(transition)))

    def test_generated_music_file(self):
        # Testataan saadaanko tuotettu midi tiedosto ladattua ilman virhettä
        self.assertTrue(self.generated_music_midi)

    def test_generated_music_playback(self):
        # Testataan saadaanko tuotettu midi tiedosto soitettua ilman virhettä
        output = mido.open_output()
        for msg in self.generated_music_midi.play():
            output.send(msg)
            time.sleep(msg.time)

    # def test_generated_music_file_structure(self):
    #     # Testataan miditiedoston rakenne
    #     midi_file = MIDIFile(numTracks=1)
    #     track = 0
    #     midi_time = 0
    #     tempo = 120
    #     midi_file.addTrackName(track, midi_time, "Generated Music")
    #     midi_file.addTempo(track, midi_time, tempo)
    #     for note in self.generated_music_note_sequence:
    #         pitch = note
    #         duration = 1
    #         volume = 100
    #         midi_file.addNote(track, 0, pitch, midi_time, duration, volume)
    #         midi_time += 1
    #     with open('generated_music_test.mid', 'wb') as file:
    #         midi_file.writeFile(file)
    #     test_midi_file = mido.MidiFile('generated_music_test.mid')
    #     self.assertEqual(test_midi_file, self.generated_music_midi)

    @classmethod
    def tearDownClass(cls):
        pass