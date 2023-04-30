import music21

# Funktio ottaa nuottijonon, tempon ja tiedostonimen, ja luo uuden MIDI-tiedoston nuottijonosta.
def create_midi_file(sequence, tempo, filename):
    new_midi = music21.stream.Stream()
    new_midi.insert(0, music21.tempo.MetronomeMark(number=tempo))
    for note in sequence:
        if '.' in note:
            notes = note.split('.')
            new_chord = music21.chord.Chord(notes)
            new_midi.append(new_chord)
        elif note is not None:
            new_note = music21.note.Note(note)
            new_midi.append(new_note)

    new_midi.write("midi", fp=filename.replace('.mid', '_generated.mid'))