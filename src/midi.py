import mido

# funktio käy läpi kaikki trakit ja viestit MIDI-tiedostossa ja luo niistä listan nuotteja
def midi_file_to_notes(file_path):
    mid = mido.MidiFile(file_path)

    notes = []
    ticks_per_beat = mid.ticks_per_beat
    tempo = 500000 

    for track in mid.tracks:
        time = 0

        for msg in track:
            time += msg.time

            if msg.type == 'set_tempo':
                tempo = msg.tempo

            if msg.type == 'note_on':
                if msg.velocity == 0:
                    notes.append(('note_off', msg.note, time))
                else:
                    notes.append(('note_on', msg.note, time))
            elif msg.type == 'note_off':
                notes.append(('note_off', msg.note, time))

    return notes, ticks_per_beat, tempo

# funktio luo MIDI-tiedoston listasta nuotteja
def notes_to_midi_file(notes, ticks_per_beat, tempo, file_path):
    mid = mido.MidiFile(ticks_per_beat=ticks_per_beat)
    track = mido.MidiTrack()
    mid.tracks.append(track)

    ticks_per_second = mido.second2tick(1, ticks_per_beat, tempo)
    time = 0

    program = 0  # Piano

    for note in notes:
        msg = None
        if note[0] == 'note_on':
            track.append(mido.Message('program_change', program=program, time=0))
            duration_ticks = int(note[2] * ticks_per_second) - time
            msg = mido.Message('note_on', note=note[1], velocity=64, time=duration_ticks)
        elif note[0] == 'note_off':
            duration_ticks = int(note[2] * ticks_per_second) - time
            msg = mido.Message('note_off', note=note[1], velocity=64, time=duration_ticks)

        if msg is not None:
            track.append(msg)
            time += duration_ticks

    mid.save(file_path)