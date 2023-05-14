Yksikkötestauksen kattavuusraportti löytyy pdf:nä (kuva) dokumentaatio kansiosta
nimellä coverage.pdf.

Testeillä on testattu Markovin ketjun luomista ja opettamista sekä 
midi tiedostojen käsittelyä ja muodostamista.

test_midi_file_to_notes tarkistaa, muuntaako 
midi_file_to_notes -funktio MIDI-tiedoston oikein nuottilistaksi ja 
palauttaa iskujen määrän ja tempolukeman.

test_notes_to_midi_file tarkistaa, luoko notes_to_midi_file -funktio 
oikein MIDI-tiedoston nuottilistasta käyttäen annettuja iskujen määrää 
ja tempolukua.

test_generate_order_1 tarkistaa, tuottaako MarkovChain-olion generate-metodi 
järjestyksellä 1 oikein sekvenssin nuotteja annetulla pituudella. Lisäksi 
se tarkistaa, ovatko generoidut nuotit osajoukko mahdollisista nuoteista, 
jotka olisivat voineet perustua harjoitusnuotteisiin.

test_markov_chain_1_generate tarkistaa, tuottaako 
MarkovChain-olion generate-metodi järjestyksellä 1 oikein sekvenssin 
nuotteja annetulla pituudella.

test_markov_chain_2_generate tarkistaa, tuottaako 
MarkovChain-olion generate-metodi järjestyksellä 2 oikein sekvenssin 
nuotteja annetulla pituudella.

test_train_order_1 tarkistaa, päivittääkö MarkovChain-olio järjestyksellä 1 
siirtymätodennäköisyyksiä oikein, kun se on koulutettu uusilla nuottisarjoilla.
Lisäksi se tarkistaa, ovatko generoidut nuotit koulutuksen jälkeen osajoukko 
mahdollisista nuoteista, jotka olisivat voineet perustua uusiin nuottisarjoihin.

test_train_order_2 tarkistaa, päivittääkö MarkovChain-olio 
järjestyksellä 2 siirtymätodennäköisyyksiä oikein, kun se on koulutettu 
uusilla nuottisarjoilla ja tuottaako sekvenssin nuotteja annetulla pituudella. 


Suortuskykytestin tulos löytyy pdf -muodossa dokumentaatio kansiossa nimellä 
suorituskyky.pdf

Testit voidaan toistaa virtuaaliympäristössä ajamalla komento pytest src 
tiralabra hakemistossa.
