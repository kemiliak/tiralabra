## Ohjelman yleisrakenne ##

Työ on jaettu karkeasti neljään osaan: trieen, Markovin ketjuun, 
MIDI tiedoston luomiseen sekä pääohjelmaan.

trie.py:

Luokka TrieNode: määrittelee TrieNode-luokan, jota käytetään Markovin 
ketjun siirtymämatriisin solmun esittämiseen. Jokaisella TrieNodella on 
sanakirja lapsisolmuista ja laskuri siitä, kuinka monta kertaa se on käyty läpi.

generate.py

Luokka MarkovChain: määrittelee Markovin ketju-luokan, jota käytetään Markovin
ketjun mallin esittämiseen. Siinä on "order" -parametri, joka määrittää 
käytettävien edellisten nuottien määrän seuraavan nuotin ennustamiseksi. 
start_states-lista, joka sisältää kaikki mahdolliset aloitustilat ketjulle 
ja sanakirja, joka sisältää siirtymätodennäköisyydet tilojen välillä.

Metodi train(self, notes): Markovin ketju-luokan metodi, joka kouluttaa 
Markovin ketjun mallia käyttämällä nuottilistaa. Se käy läpi nuotit ja päivittää siirtymämatriisia nykyisten ja edellisten nuottien perusteella.

Metodi generate(self, length): Markovin ketju-luokan metodi, joka generoi 
tietyn mittaisen nuottijonon käyttäen Markovin ketjun mallia. Se valitsee 
satunnaisesti aloitustilan start_states-listasta ja generoi seuraavan nuotin 
iteratiivisesti nykyisen tilan ja siirtymätodennäköisyyksien perusteella.

midi.py

Funktio midi_file_to_notes(file_path): lukee MIDI-tiedoston ja palauttaa 
nuottilistan. Se käyttää mido-kirjastoa MIDI-tiedoston lukemiseen ja muuntaa 
jokaisen nuottiviestin tupleksi, joka sisältää nuotin tyypin 
(note_on tai note_off), MIDI-nuotin numeron ja ajan tikkeinä.

Funktio notes_to_midi_file(notes, ticks_per_beat, tempo, file_path): 
kirjoittaa nuottilistan MIDI-tiedostoon. Se käyttää mido-kirjastoa uuden 
MIDI-tiedoston luomiseen.


## Analyysi koodista ##

midi_file_to_notes: Tämä funktio käy läpi kaikki trakit ja 
viestit MIDI-tiedostossa ja luo niistä listan nuotteja. Funktion 
aikavaativuus on O(n), missä n on MIDI-tiedostossa olevien viestien 
kokonaismäärä.

MarkovChain.train: funktio kouluttaa Markovin ketjun käymällä läpi 
kaikki nuotit ja päivittämällä siirtymämatriisia. Funktion aikavaativuus 
on O(m * k), missä m on nuottien määrä ja k on Markovin ketjun aste.

MarkovChain.generate: funktio generoi uuden nuottisekvenssin 
siirtymämatriisin perusteella. Funktion aikavaativuus on O(l * k), 
missä l on generoidun sekvenssin pituus ja k on Markovin ketjun aste.

notes_to_midi_file: funktio luo MIDI-tiedoston listasta nuotteja. 
Funktion aikavaativuus on O(n), missä n on syötteessä olevien nuottien määrä.

Koodin kokonaisaikavaativuus riippuu Markovin ketjun asteesta ja 
MIDI-tiedoston koosta. Olettaen, että Markovin ketjun aste on vakio, 
koko ohjelman aikavaativuus voidaan ilmaista muodossa O(n + m + l), 
missä n on MIDI-tiedoston koko, m on MIDI-tiedostossa olevien nuottien 
määrä ja l on generoidun sekvenssin pituus.

### Puutteet ja parannusehdotukset ###

* Käyttöliittymää voisi kehittää ja lisätä esimerkiksi jonkinlaista grafiikkaa
* Rakenne ei välttämättä ole paras mahdollinen, koska trie -tietorakenne tuotti
paljon ongelmia, sitä voisi siis vielä parantaa.

### Lähteet ###

* [https://medium.com/@stevehiehn/how-to-generate-music-with-python-the-basics-62e8ea9b99a5](https://medium.com/@stevehiehn/how-to-generate-music-with-python-the-basics-62e8ea9b99a5)
* [https://towardsdatascience.com/markov-chain-for-music-generation-932ea8a88305](https://towardsdatascience.com/markov-chain-for-music-generation-932ea8a88305)
* [https://www.geeksforgeeks.org/trie-insert-and-search/](https://www.geeksforgeeks.org/trie-insert-and-search/)
* [https://towardsdatascience.com/making-music-when-simple-probabilities-outperform-deep-learning-75f4ee1b8e69](https://towardsdatascience.com/making-music-when-simple-probabilities-outperform-deep-learning-75f4ee1b8e69)

