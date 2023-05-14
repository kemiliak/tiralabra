import unittest
from generate import MarkovChain
from midi import notes_to_midi_file, midi_file_to_notes
import mido
import os


class TestMarkovChain(unittest.TestCase):
    def setUp(self):
        self.notes = [('note_on', 60, 0), ('note_off', 60, 100), ('note_on', 62, 100),
                      ('note_off', 62, 200), ('note_on', 64, 200), ('note_off', 64, 300),
                      ('note_on', 60, 300), ('note_off', 60, 400)]
        
        self.markov_chain_1 = MarkovChain(order=1)
        self.markov_chain_1.train(self.notes)
        
        self.markov_chain_2 = MarkovChain(order=2)
        self.markov_chain_2.train(self.notes)

        self.input_file = 'test_input.mid'
        self.output_file = 'test_output.mid'
        self.ticks_per_beat = 480
        self.tempo = 500000
        
        mid = mido.MidiFile()
        track = mido.MidiTrack()
        mid.tracks.append(track)
        track.append(mido.Message('note_on', note=60, velocity=64, time=0))
        track.append(mido.Message('note_off', note=60, velocity=64, time=480))
        mid.save(self.input_file)
        
    def test_midi_file_to_notes(self):
        expected_notes = [('note_on', 60, 0), ('note_off', 60, 480)]
        notes, ticks_per_beat, tempo = midi_file_to_notes(self.input_file)
        self.assertEqual(notes, expected_notes)
        self.assertEqual(ticks_per_beat, self.ticks_per_beat)
        self.assertEqual(tempo, self.tempo)

    def test_notes_to_midi_file(self):
        notes = [('note_on', 60, 0), ('note_off', 60, 480)]
        notes_to_midi_file(notes, self.ticks_per_beat, self.tempo, self.output_file)
        self.assertTrue(os.path.exists(self.output_file))

    def test_generate_order_1(self):
        generated_notes = self.markov_chain_1.generate(length=5)
        self.assertEqual(len(generated_notes), 5)

        possible_notes = set([(note[0], note[1], note[2]) for note in self.notes])
        generated_notes_set = set(generated_notes)
        self.assertTrue(generated_notes_set.issubset(possible_notes))

    def test_markov_chain_1_generate(self):
        generated_notes = self.markov_chain_1.generate(length=8)
        self.assertEqual(len(generated_notes), 8)

    def test_markov_chain_2_generate(self):
        generated_notes = self.markov_chain_2.generate(length=8)
        self.assertEqual(len(generated_notes), 8)
    
    def test_train_order_1(self):
        new_notes = [('note_on', 60, 0), ('note_off', 60, 100), ('note_on', 62, 100),
                     ('note_off', 62, 200), ('note_on', 64, 200), ('note_off', 64, 300),
                     ('note_on', 67, 300), ('note_off', 67, 400)]

        new_markov_chain = MarkovChain(order=1)
        new_markov_chain.train(new_notes)

        generated_notes = new_markov_chain.generate(length=5)
        self.assertEqual(len(generated_notes), 5)

        possible_notes = set([(note[0], note[1], note[2]) for note in new_notes])
        generated_notes_set = set(generated_notes)
        self.assertTrue(generated_notes_set.issubset(possible_notes))

    def test_train_order_2(self):
        new_notes = [('note_on', 60, 0), ('note_off', 60, 100), ('note_on', 62, 100),
                     ('note_off', 62, 200), ('note_on', 64, 200), ('note_off', 64, 300),
                     ('note_on', 67, 300), ('note_off', 67, 400)]

        new_markov_chain = MarkovChain(order=2)
        new_markov_chain.train(new_notes)

        generated_notes = new_markov_chain.generate(length=5)
        self.assertEqual(len(generated_notes), 5)

if __name__ == '__main__':
    unittest.main()