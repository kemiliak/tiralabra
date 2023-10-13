## Ohjelman yleisrakenne ##

trie.py:

Luokka TrieNode: alustaa trie solmun: 
note_event = "avain", jolla haetaan esim. generate.py rivi 29: (msg,note)
children = solmun lapset
count = esiintyvyydet, joiden perusteella todennäköisyys lasketaan

generate.py:

Luokka MarkovChain (voisi olla myös Trie class): 
order = Markovin ketjun order, käytännössä määrittää kuinka monta edellistä 
nuottia otetaan huomioon seuraavan määrittämisessä
start_states = lista, joka sisältää kaikki mahdolliset aloitustilat

insert(self, notes) funktio:
Käy läpi trieä, jos nuottia ei löydy (esim. order=2) kahden edeltävän tilan jälkeen,
lisätään se, mikäli siirtymä kuitenkin on jo olemassa kasvatetaan sen count-arvoa

generate(self, length) funktio:
Valitaan satunnaisesti aloitustila start_states-listasta.
Lasketaan total_count eli kaikki count-arvot yhteen, tämän jälkeen arvotaan luku 
1 ja total_count välillä. Seuraava nuotti valitaan todennäköisyyksien mukaan, siten että
suurempi count-arvo tarkoittaa suurempaa todennäköisyyttä olla seuraava nuotti.

midi.py:

Funktio midi_file_to_notes(file_path): lukee MIDI-tiedoston ja palauttaa 
nuottilistan. Se käyttää mido-kirjastoa MIDI-tiedoston lukemiseen ja muuntaa 
jokaisen nuottiviestin tupleksi, joka sisältää nuotin tyypin 
(note_on tai note_off), MIDI-nuotin numeron ja ajan.

Funktio notes_to_midi_file(notes, ticks_per_beat, tempo, file_path): 
kirjoittaa nuottilistan MIDI-tiedostoon. Se käyttää mido-kirjastoa uuden 
MIDI-tiedoston luomiseen.


## Analyysi koodista ##

midi_file_to_notes: Tämä funktio käy läpi kaikki trakit ja 
viestit MIDI-tiedostossa ja luo niistä listan nuotteja. Funktion 
aikavaativuus on O(n), missä n on MIDI-tiedostossa olevien viestien 
kokonaismäärä.

MarkovChain: 
Sekä trien insert että search funktion aikavaativuus on O(n).

generate: Funktion aikavaativuus on O(l * k), 
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

### Lähteet ###

* [https://medium.com/@stevehiehn/how-to-generate-music-with-python-the-basics-62e8ea9b99a5](https://medium.com/@stevehiehn/how-to-generate-music-with-python-the-basics-62e8ea9b99a5)
* [https://towardsdatascience.com/markov-chain-for-music-generation-932ea8a88305](https://towardsdatascience.com/markov-chain-for-music-generation-932ea8a88305)
* [https://www.geeksforgeeks.org/trie-insert-and-search/](https://www.geeksforgeeks.org/trie-insert-and-search/)
* [https://towardsdatascience.com/making-music-when-simple-probabilities-outperform-deep-learning-75f4ee1b8e69](https://towardsdatascience.com/making-music-when-simple-probabilities-outperform-deep-learning-75f4ee1b8e69)

