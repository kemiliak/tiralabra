import numpy as np

# Nuotit, joista sekvenssi tuotetaan
chords = ["C", "D", "E", "F", "G", "A", "H"]

# Tässä vaiheessa siirtymämatriisissa käytössä on satunnaiset todennäköisyydet, joita ei ole luotu opetusdatan avulla.
# Matriisissa on siis todennäköisyydet siirtyä nuotista toiseen.
transition_matrix = np.array([
    [0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1],
    [0.1, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1],
    [0.1, 0.1, 0.2, 0.2, 0.2, 0.1, 0.1],
    [0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.1],
    [0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2],
    [0.2, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2],
    [0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.2]
])

# Valitaan aloitusnuotti
current_chord = "C"

# Halutun sekvenssin pituus
chord_length = 20

# Nuottien määräytyminen:
# Jokaisessa iteraatiossa käytetään nykyistä nuottia etsimään vastaavaa riviä siirtymämatriisista 
# ja valitaan satunnaisesti seuraavan nuotti kyseisen rivin todennäköisyyksien perusteella. 
# Liitetään seuraava nuotti luetteloon ja päivitetään nykyinen nuotti seuraavaa iteraatiota varten.
chord_progression = [current_chord]
for i in range(chord_length-1):
    current_index = chords.index(current_chord)
    next_index = np.random.choice(len(chords), p=transition_matrix[current_index])
    next_chord = chords[next_index]
    chord_progression.append(next_chord)
    current_chord = next_chord

print(chord_progression)
