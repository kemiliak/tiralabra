import mido
import random

# funktio käy läpi kaikki trakit ja viestit MIDI-tiedostossa ja luo niistä listan nuotteja
def midi_file_to_notes(file_path):
    mid = mido.MidiFile(file_path)

    notes = []
    ticks_per_beat = mid.ticks_per_beat
    tempo = 500000  # oletustempo

    for track in mid.tracks:
        time = 0

        for msg in track:
            time += msg.time

            if msg.type == "set_tempo":
                tempo=msg.tempo

            if msg.type == 'note_on':
                if msg.velocity == 0:
                    notes.append(('note_off', msg.note, time))
                else:
                    notes.append(('note_on', msg.note, time))
            elif msg.type == 'note_off':
                notes.append(('note_off', msg.note, time))
    
    return notes, ticks_per_beat, tempo

# funktio luo MIDI-tiedoston
def notes_to_midi_file(notes, ticks_per_beat, tempo, file_path):
    mid = mido.MidiFile()
    track = mido.MidiTrack()
    mid.tracks.append(track)

    program = 0  # Piano
    track.append(mido.Message('program_change', program=program, time=0))
    track.append(mido.MetaMessage('set_tempo', tempo=tempo, time=0))

    for note in notes:
        msg = None
        if note[0] == 'note_on':
            duration_ticks = int((random.randint(2, 4) * ticks_per_beat)/10)
            msg = mido.Message('note_on', note=note[1], velocity=64, time=duration_ticks)
        elif note[0] == 'note_off':
            duration_ticks = int((random.randint(2, 4) * ticks_per_beat)/10)
            msg = mido.Message('note_off', note=note[1], velocity=64, time=duration_ticks)

        if msg is not None:
            track.append(msg)

    mid.save(file_path)