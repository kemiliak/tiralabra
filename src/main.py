from generate import generate_markov_model, generate_sequence_from_model
from midi import create_midi_file
import music21

# Ohjelma ajetaan tästä, printtien avulla voidaan seurata onnistuiko uuden MIDI 
# tiedoston luominen

def generate_sequence(filename, order, length=10000, num_notes=1, tempo=120):
    print("Ladataan MIDI tiedosto...")
    midi_data = music21.converter.parse(filename)
    notes_to_parse = None

    try:
        s2 = music21.instrument.partitionByInstrument(midi_data)
        notes_to_parse = s2.parts[0].recurse() 
    except:
        notes_to_parse = midi_data.flat.notes

    print("Puretaan nuottien sekvenssit...")
    note_sequence = []
    for element in notes_to_parse:
        if isinstance(element, music21.note.Note):
            note_sequence.append(element.pitch.nameWithOctave)
        elif isinstance(element, music21.chord.Chord):
            note_sequence.append('.'.join(str(n) for n in element.normalOrder))

    print("Luodaan malli Markovin ketjun avulla...")
    model = generate_markov_model(note_sequence, order)

    print("Generoidaan sekvenssi...")
    sequence = generate_sequence_from_model(model, length, num_notes)

    print("Luodaan uusi MIDI tiedosto...")
    create_midi_file(sequence, tempo, filename)

    print("Uuden MIDI tiedoston luominen onnistui!")

generate_sequence("../imperial.mid", order=3, length=10000, num_notes=3, tempo=100)