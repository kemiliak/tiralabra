Työ on jaettu karkeasti neljään osaan: trie tietorakenteeseen, Markovin 
ketjuun, MIDI tiedoston luomiseen sekä pääohjelmaan.

trie.py:

Trie-luokka: Tämä luokka edustaa trie-tietorakennetta, joka tallentaa 
todennäköisyydet siirtymisestä yhdestä nuotista toiseen. 
Siinä on init() -metodi, joka ottaa order-argumentin, joka määrittää aiempien
nuottien määrän, jotka otetaan huomioon todennäköisyyksien laskemisessa. 
Siinä on myös add_sequence() -metodi, joka lisää nuottijonon 
trie-tietorakenteeseen, ja generate_sequence() -metodi, joka generoi uuden 
nuottijonon trie-tietorakenteessa tallennettujen todennäköisyyksien perusteella.

TrieNode-luokka: Luokka edustaa solmua triessa. Siinä on value-attribuutti, 
joka tallentaa nuotin, joka liittyy solmuun ja children-attribuutti, 
joka tallentaa luettelon lapsisolmuista. Siinä on myös get_child() -metodi, 
joka palauttaa lapsisolmun, joka liittyy annettuun nuottiarvoon, ja 
insert() -metodi, joka lisää uuden nuottijonon trie-tietorakenteeseen.

generate.py:

generate_markov_model() -funktio: Funktio ottaa nuottijonon ja order-argumentin 
ja palauttaa MarkovTrie-olion, joka edustaa nuottijonon Markov-mallia. Se 
tekee tämän luomalla uuden MarkovTrie-olion, lisäämällä nuottijonon 
trie-tietorakenteeseen käyttäen add_sequence() -metodia, ja palauttamalla trien.

generate_sequence_from_model() -funktio: Funktio ottaa MarkovTrie-olion, joka
edustaa Markov-mallia, length-argumentin, joka edustaa generoitavan uuden 
nuottijonon pituutta, ja num_notes-argumentin, joka edustaa generoitavien 
nuottien määrää kerralla. Se generoi uuden nuottijonon aloittamalla trien 
juurisolmusta, valitsemalla satunnaisen lapsisolmun trie-tietorakenteessa 
tallennettujen todennäköisyyksien perusteella, ja liittämällä seuraavat 
num_notes nuottia uuteen nuottijonoon. Se päivittää sitten nykyisen solmun 
ja nykyisen fragmentin vastaamaan uutta nuottijonoa, ja toistaa prosessin, 
kunnes haluttu pituus saavutetaan.

midi.py:

Funktio ottaa nuottien sekvenssin, tempon ja tiedostonimen ja luo uuden 
MIDI-tiedoston annetun nuottisekvenssin perusteella. Se luo uuden 
music21.stream.Stream-olion, asettaa tempon käyttäen 
music21.tempo.MetronomeMark-oliota ja käy läpi nuottisekvenssin luodakseen 
music21.note.Note- ja music21.chord.Chord-objekteja tarvittaessa. Sitten se 
kirjoittaa streamin MIDI-tiedostoon annetulla tiedostonimellä.

main.py:

generate_sequence() -funktio: Funktio ottaa vastaan tiedoston nimen, 
order-parametrin, pituusparametrin uuden sekvenssin pituutta varten, 
num_notes-parametrin, joka edustaa kerralla generoitavien nuottien määrää ja 
tempo-parametrin, joka edustaa uuden sekvenssin tempoa. Se generoi uuden 
nuottisekvenssin lukemalla MIDI-tiedoston annetulla tiedostonimellä käyttäen 
music21.converter.parse() -funktiota ja erottamalla nuottisekvenssin 
recurse() -metodilla. Sitten se generoi nuottisekvenssin Markov-mallin 
note_ sequencesta käyttäen generate_markov_model() -funktiota ja generoi 
uuden nuottisekvenssin mallin perusteella käyttäen 
generate_sequence_from_model() -funktiota ja luomalla uuden MIDI-tiedoston 
sekvenssistä create_midi_file() -funktiolla.
