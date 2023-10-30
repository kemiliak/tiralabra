from midi import midi_file_to_notes, notes_to_midi_file
from generate import MarkovChain
import sys

def main():
    """ Pääohjelma, käyttäjä voi antaa tiedoston ja Markovin ketjun orderin argumentteina """

    try:
        input_file = sys.argv[2]
        order = sys.argv[3]

    except:
        input_file = 'clairdelune.mid'
        order = 2

    output_file = 'output.mid'

    notes, ticks_per_beat,tempo = midi_file_to_notes(input_file)
    markov_chain = MarkovChain(order)
    markov_chain.insert(notes)

    print("Generoidaan sekvenssi...")
    generated_notes = markov_chain.generate(length=200)
    #Luodaan uusi MIDI tiedosto
    notes_to_midi_file(generated_notes, ticks_per_beat, tempo, output_file)

    print("Uuden MIDI tiedoston luominen onnistui!\nSe löytyy nimellä output.mid samasta kansiosta alkuperäisen MIDI tiedoston kanssa.")

if __name__ == '__main__':
    main()