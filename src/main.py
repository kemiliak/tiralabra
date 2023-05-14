from midi import midi_file_to_notes, notes_to_midi_file
from generate import MarkovChain

# ohjelma ajetaan täältä
def main():
    input_file = 'clairdelune.mid'
    output_file = 'output.mid'

    notes, ticks_per_beat, tempo = midi_file_to_notes(input_file)

    print("Luodaan malli Markovin ketjun avulla...")
    markov_chain = MarkovChain(order=2)
    markov_chain.train(notes)

    print("Generoidaan sekvenssi...")
    generated_notes = markov_chain.generate(length=100)

    print("Luodaan uusi MIDI tiedosto...")
    notes_to_midi_file(generated_notes, ticks_per_beat, tempo, output_file)

    print("Uuden MIDI tiedoston luominen onnistui!\nSe löytyy nimellä output.mid samasta kansiosta alkuperäisen MIDI tiedoston kanssa.")

if __name__ == '__main__':
    main()