-- Popolamento della tabella Cliente
INSERT INTO Cliente (email, nome, cognome, tipo_utente, data_nascita, numero_carta, mese_scadenza, anno_scadenza, verificato, password) VALUES
('sofiaesposito@gmail.com', 'Sofia', 'Esposito', 'Studente', '2001-03-10', '3546746378291034', 1, 2025, true, 'Passsofy1@'),
('matteobianchi@gmail.com', 'Matteo', 'Bianchi', 'Studente', '2003-07-25', '9857362548907847', 12, 2024, true, 'matt7Passurh@.'),
('kekkamancini@gmail.com', 'Francesca', 'Mancini', 'Locatore', '1982-08-30', '1265783490875645', 6, 2024, true, 'kekkaLoc007@.'),
('gioromano@gmail.com', 'Giorgia', 'Romano', 'Studente', '2000-09-05', '6574837392817454', 1, 2024, true, 'GiogioRom@pass1.'),
('lucaferrari@gmail.com', 'Luca', 'Ferrari', 'Studente', '1999-11-05', '1234768590432345', 2, 2025, true, 'LucaPassURH!.'),
('marcorossi@gmail.com', 'Marco', 'Rossi', 'Locatore', '1970-01-10', '5678901234567890', 3, 2024, false, 'UniPass7@.'),
('sofybianchi@gmail.com', 'Sofy', 'Bianchi', 'Locatore', '1985-07-22', '1945637890987453', 10, 2024, true, 'PassSof7@!.'),
('lucaambruoso@gmail.com', 'Luca', 'Ambruoso', 'Locatore', '1978-04-18', '3456789012345678', 9, 2024, false, 'LucPass@!!.1'),
('giogioespo@gmail.com', 'Giovanni', 'Esposito', 'Locatore', '1975-11-30', '2345678901234567', 8, 2024, true, 'PassValid@Uh7.'),
('saramarti@gmail.com', 'Sara', 'Martini', 'Studente', '1999-02-14', '4321098765432109', 7, 2024, true, 'Pass7word@.'),
('giorgioferraro@gmail.com', 'Giorgio', 'Ferraro', 'Studente', '2005-09-08', '9085362718192346', 6, 2024, true, 'giorGioPass7@.'),
('antoalbanese@gmail.com', 'Antonio', 'Albanese', 'Studente', '2001-09-18', '3546374789092364', 7, 2024, true, 'AntoUrh7!!.'),
('paolomoretti@gmail.com', 'Paolo', 'Moretti', 'Locatore', '1970-08-17', '7646893475091237', 11, 2024, true, 'LucMor70@.'),
('francescopixcont@gmail.com', 'Francesco Pio', 'Contaldo', 'Studente', '2000-09-22', '4657283767900123', 2, 2024, true, 'pixPass9@.'),
('cristyanesp@gmail.com', 'Cristyan', 'Esposito', 'Studente', '2001-04-21', '9085362718192346', 7, 2024, true, 'UniRentHpass@!.'),
('andreaconti@gmail.com', 'Andrea', 'Conti', 'Locatore', '1969-05-12', '8647362787980967', 2, 2024, true, 'And@99pass.'),
('ilianofaso@gmail.com', 'Iliano', 'Fasolino', 'Studente', '2000-09-08', '8573653989023647', 1, 2024, true, 'gPassfaso@..'),
('marcogreco@gmail.com', 'Marco', 'Greco', 'Studente', '2000-09-08', '9046276473892912', 2, 2024, true, 'urhPass54!.'),
('giupiosorr@gmail.com', 'Giuseppe Pio', 'Sorrentino', 'Studente', '2000-09-08', '4536174783921224', 6, 2024, true, 'giupiPass65!.'),
('chiararusso@gmail.com', 'Chiara', 'Russo', 'Locatore', '1980-09-15', '9075645362718175', 3, 2024, true, 'locPassSic7..'),
('marticosta@gmail.com', 'Martina', 'Costa', 'Locatore', '1987-04-08', '9075643678932346', 7, 2024, true, 'Passurh89@.'),
('giugatti@gmail.com', 'Giulia', 'Gatti', 'Locatore', '1967-11-03', '7684093400543456', 10, 2024, true, 'giuCat@1.');



-- Popolamento della tabella Dipendente
INSERT INTO Dipendente (email, nome, cognome, tipo_dipendente, password) VALUES
('simodellaporta@gmail.com', 'Simone', 'Della Porta', 'Admin', 'SimoDP@23.'),
('roccoiuliano@gmail.com', 'Rocco', 'Iuliano', 'Admin', 'RoccIul89.'),
('alexdeluca@gmail.com', 'Alessando', 'De Luca', 'Homechecker', 'AlexDL@65.'),
('alessandramaione@gmail.com', 'Alessanda', 'Maione', 'Homechecker', 'AlessMatt45.!'),
('mariomuratore@gmail.com', 'Mario', 'Muratore', 'Homechecker', 'MarMur89@.'),
('stefdecaro@gmail.com', 'Stefano', 'De Caro', 'Homechecker', 'steDeC@pass.7');

-- Popolamento della tabella Post
INSERT INTO Post (titolo, descrizione, email) VALUES
('Ricerca di un coinquilino', "Sto cercando un coinquilino con cui condividere l'affitto per questo anno e condividere allenamenti in palestra. Io sto seguendo il secondo anno di magistrale ad Unisa", 'matteobianchi@gmail.com'),
('Ragazzo/a a cui piace l arte?', 'Sono alla ricerca di un ragazzo o una ragazza che ha la passione per l arte. Io sto seguendo il secondo anno alla Sapienza', 'gioromano@gmail.com'),
('Qualcuno in cerca di un appartamento a Fisciano?', 'Ho appena trovato un alloggio a Fisciano nelle zone dell università di Fisciano, c è qualcuno che è interessato a condividere l alloggio con me per questo anno? Io sto seguendo il terzo anno di triennale ad UniMi Milano', 'saramarti@gmail.com'),
('Ricerca di un coinquilino', "Sto cercando un coinquilino con cui condividere l'affitto per questo anno e che è iscritto al corso di Informatica alla Federico II", 'francescopixcont@gmail.com'),
('Ragazzo/a a cui piace allenarsi?', 'Sono alla ricerca di un ragazzo o una ragazza che ha voglia di allenarsi in compagnia nelle zone di Roma Tre', 'giorgioferraro@gmail.com');

-- Popolamento della tabella Passione
INSERT INTO Passione (nome) VALUES
('Viaggi'),
('Calcio'),
('Basket'),
('Nuoto'),
('Gym'),
('Lettura'),
('Cinema'),
('Serie tv'),
('Giardinaggio'),
('Cucina'),
('Musica'),
('Arte'),
('Fotografia'),
('Tecnologia'),
('Programmazione');

-- Popolamento della tabella Assegnazione
INSERT INTO Assegnazione (id_passione, email) VALUES
(1, 'sofiaesposito@gmail.com'),
(6, 'sofiaesposito@gmail.com'),
(7, 'sofiaesposito@gmail.com'),
(8, 'sofiaesposito@gmail.com'),
(2, 'matteobianchi@gmail.com'),
(8, 'matteobianchi@gmail.com'),
(11, 'matteobianchi@gmail.com'),
(1, 'gioromano@gmail.com'),
(5, 'gioromano@gmail.com'),
(8, 'gioromano@gmail.com'),
(10, 'gioromano@gmail.com'),
(2, 'lucaferrari@gmail.com'),
(3, 'lucaferrari@gmail.com'),
(1, 'lucaferrari@gmail.com'),
(7, 'lucaferrari@gmail.com'),
(5, 'lucaferrari@gmail.com'),
(7, 'saramarti@gmail.com'),
(8, 'saramarti@gmail.com'),
(11, 'giorgioferraro@gmail.com'),
(12, 'giorgioferraro@gmail.com');

-- Popolamento della tabella Segnalazione
INSERT INTO Segnalazione (email, emailS, stato, motivo) VALUES
('sofiaesposito@gmail.com', 'andreaconti@gmail.com', 'Aperta', 'Annuncio non rispecchia correttamente quello che ho trovato all arrivo nell alloggio'),
('lucaferrari@gmail.com', 'andreaconti@gmail.com', 'Aperta', 'Le condizioni in cui ho trovato l alloggio al mio arrivo erano davvero pessime. Il locatore ha indicato nell annuncio tutt altro rispetto a quello che ho ritrovato nell alloggio.'),
('gioromano@gmail.com', 'giugatti@gmail.com', 'Chiusa', 'Proprietario non molto affidabile.'),
('cristyanesp@gmail.com', 'giorgioferraro@gmail.com' ,'Aperta', 'Ragazzo non molto educato, una cattiva compagnia con cui condividere un affitto. Sconsigliato.'),
('marcogreco@gmail.com', 'giugatti@gmail.com', 'Chiusa', 'Problema col pagamento, non riesco ad effettuare il pagamento per procedeere all affitto');

-- Popolamento della tabella Università
INSERT INTO Università (denominazione, email, indirizzo) VALUES
('Università di Napoli Federico II', 'urp@pec.unina.it', 'Corso Nicolangelo Protopisani, San Giovanni a Teduccio, Municipalità 6, Marianella, Napoli, Campania, 80146, Italia'),
('Politecnico di Milano - Sede Leonardo', 'pecateneo@cert.polimi.it', 'Via Nicola Antonio Porpora, Città Studi, Municipio 3, Milano, Lombardia, 20133, Italia'),
('Università Roma Tre', 'uniRoma@example.com', '133, Via Ostiense, Municipio Roma VIII, Roma, Lazio, 00154, Italia'),
('Università degli Studi di Salerno', 'ammicent@pec.unisa.it', 'Via Salvador Allende, Sava, Baronissi, Salerno, Campania, 84081, Italia'),
('Università La Sapienza', 'urp@uniroma1.it', 'Piazzale del Verano, San Lorenzo, Municipio Roma II, Roma, Lazio, 00161, Italia');

-- Popolamento della tabella Iscrizione
INSERT INTO Iscrizione (denominazione, email) VALUES
('Università di Napoli Federico II', 'sofiaesposito@gmail.com'),
('Politecnico di Milano - Sede Leonardo', 'matteobianchi@gmail.com'),
('Università La Sapienza', 'giorgioferraro@gmail.com'),
('Università Roma Tre', 'kekkamancini@gmail.com'),
('Università La Sapienza', 'gioromano@gmail.com'),
('Università Roma Tre', 'lucaferrari@gmail.com'),
('Politecnico di Milano - Sede Leonardo', 'saramarti@gmail.com'),
('Università degli Studi di Salerno', 'antoalbanese@gmail.com'),
('Università degli Studi di Salerno', 'francescopixcont@gmail.com'),
('Università degli Studi di Salerno', 'cristyanesp@gmail.com'),
('Università degli Studi di Salerno', 'ilianofaso@gmail.com'),
('Università degli Studi di Salerno', 'marcogreco@gmail.com'),
('Università degli Studi di Salerno', 'giupiosorr@gmail.com');

-- Popolamento della tabella Chat
INSERT INTO Chat (titolo) VALUES
('Chat Viaggi'),
('Chat Sport'),
('Chat Cucina'),
('Chat Musica'),
('Chat Lettura'),
('Chat Cinema'),
('Chat Film e Serie tv'),
('Chat Arte');

-- Popolamento della tabella Partecipazione
INSERT INTO Partecipazione (id_chat, email) VALUES
(1, 'sofiaesposito@gmail.com'),
(1, 'kekkamancini@gmail.com'),
(2, 'chiararusso@gmail.com'),
(2, 'sofybianchi@gmail.com'),
(3, 'cristyanesp@gmail.com'),
(3, 'francescopixcont@gmail.com'),
(4, 'matteobianchi@gmail.com'),
(4, 'saramarti@gmail.com'),
(5, 'chiararusso@gmail.com'),
(5, 'gioromano@gmail.com');

-- Popolamento della tabella Messaggio
INSERT INTO Messaggio (email, id_chat, contenuto) VALUES
('sofiaesposito@gmail.com', 1, 'Ciao!'),
('kekkamancini@gmail.com', 1, 'Salve!'),
('sofiaesposito@gmail.com', 1, "Vorrei avere delle informazioni aggiuntive sull'alloggio da lei pubblicato"),
('kekkamancini@gmail.com', 1, 'Va bene, cosa vuoi sapere di preciso?'),
('chiararusso@gmail.com', 2, 'Ciao, a me piace cucinare, per caso nel suo alloggio posso trovare lo stresso necessario per cucinare?'),
('sofybianchi@gmail.com', 2, "Si, nell'alloggio puoi trovare tutto lo stretto necessario per cucinare."),
('cristyanesp@gmail.com', 3, 'Ciao'),
('cristyanesp@gmail.com', 3, 'ho visto che anche tu ti alleni in palestra, ti va di allenarci insieme?'),
('francescopixcont@gmail.com', 3, 'Va bene, per me possiamo organizzarci.'),
('francescopixcont@gmail.com', 3, 'In che palestra vai ad allenarti tu?'),
('cristyanesp@gmail.com', 3, "nella palestra dell'università, quando vuoi possiamo andare anche dopo i corsi"),
('matteobianchi@gmail.com', 4, 'Ciao! Consigli su libri d arte?'),
('saramarti@gmail.com', 4, 'Se ti piace il genere fantasy, ti consiglio i libri di Harry Potter.'),
('chiararusso@gmail.com', 5, 'Ciao, ti va di conoscerci?'),
('gioromano@gmail.com', 5, 'Ciao! piacere');

-- Popolamento della tabella Alloggio
INSERT INTO Alloggio (tipo_alloggio, disponibilità, titolo, mq, n_camere_letto, n_bagni, classe_energetica, arredamenti, data_pubblicazione, pannelli_solari, pannelli_fotovoltaici, descrizione, verifica, prezzo, n_ospiti, n_stanze, tasse, email_dip, email_loc, data_verifica) VALUES
('Camera', TRUE, 'Camera singola in centro', 20, 1, 1, 'A', TRUE, '2023-01-10', TRUE, FALSE, 'Bellissima camera in pieno centro della città', TRUE, 50.00, 1, 1, 22, 'alexdeluca@gmail.com', 'kekkamancini@gmail.com', '2023-01-15'),
('Monolocale', TRUE, 'Monolocale moderno', 40, 1, 1, 'B', TRUE, '2023-01-12', FALSE, TRUE, 'Monolocale con tutti i comfort', FALSE, 80.00, 2, 2, 22, 'alexdeluca@gmail.com', 'marcorossi@gmail.com', '2023-01-20'),
('Stanza condivisa', TRUE, 'Stanza condivisa per studenti', 30, 2, 1, 'C', TRUE, '2023-02-01', FALSE, TRUE, 'Stanza condivisa in zona universitaria', FALSE, 40.00, 2, 2, 22, 'alessandramaione@gmail.com', 'sofybianchi@gmail.com', '2023-02-10'),
('Villa', TRUE, 'Villa con piscina', 200, 4, 3, 'A+', TRUE, '2023-02-15', TRUE, TRUE, 'Villa di lusso con vista panoramica', FALSE, 300.00, 6, 5, 22, 'alessandramaione@gmail.com', 'lucaambruoso@gmail.com', '2023-03-01'),
('Bilocale', TRUE, 'Bilocale vicino al campus', 50, 1, 1, 'B', TRUE, '2023-03-01', FALSE, FALSE, 'Bilocale ideale per studenti', TRUE, 60.00, 2, 2, 22, 'alexdeluca@gmail.com', 'giogioespo@gmail.com', '2023-03-10');

-- Popolamento della tabella Indirizzo
INSERT INTO Indirizzo (id_alloggio, via, cap, civico, citta, provincia) VALUES
(1, 'Via Principale', 12345, '12A', 'Roma', 'RM'),
(2, 'Via Moderna', 56789, '34B', 'Milano', 'MI'),
(3, 'Via Universitaria', 34567, '45', 'Roma', 'RM'),
(4, 'Via Panoramica', 10123, '78', 'Napoli', 'NA'),
(5, 'Via Campus', 54321, '56', 'Milano', 'MI');

-- Popolamento della tabella Immagine
INSERT INTO Immagine (id_alloggio, path) VALUES
(1, 'static/alloggi/1/GaiaBrunello_1.jpg'),
(1, 'static/alloggi/1/GaiaBrunello_2_500x500.jpg'),
(1, 'static/alloggi/1/GaiaBrunello_3_500x500.jpg'),
(2, 'static/alloggi/2/GaiaBrunello_1.jpg'),
(2, 'static/alloggi/2/GaiaBrunello_2_500x500.jpg'),
(2, 'static/alloggi/2/GaiaBrunello_3_500x500.jpg'),
(3, 'static/alloggi/3/GaiaBrunello_1.jpg'),
(3, 'static/alloggi/3/GaiaBrunello_2_500x500.jpg'),
(3, 'static/alloggi/3/GaiaBrunello_3_500x500.jpg'),
(4, 'static/alloggi/4/GaiaBrunello_1.jpg'),
(4, 'static/alloggi/4/GaiaBrunello_2_500x500.jpg'),
(4, 'static/alloggi/4/GaiaBrunello_3_500x500.jpg'),
(5, 'static/alloggi/5/GaiaBrunello_1.jpg'),
(5, 'static/alloggi/5/GaiaBrunello_2_500x500.jpg'),
(5, 'static/alloggi/5/GaiaBrunello_3_500x500.jpg');

-- Popolamento della tabella Affittare
INSERT INTO Affittare (id_alloggio, email, data_inizio, data_fine, numero_carta, mese_scadenza, anno_scadenza, prezzo) VALUES
(1, 'gioromano@gmail.com', '2024-01-15', '2024-02-15', '6574837392817454', 1, 2024, 400.00),
(2, 'matteobianchi@gmail.com', '2023-12-10', '2024-01-25', '9857362548907847', 12, 2024, 700.00),
(3, 'giorgioferraro@gmail.com', '2024-02-01', '2024-03-15', '9085362718192346', 6, 2024, 300.00),
(4, 'sofiaesposito@gmail.com', '2023-11-15', '2023-12-30', '3546746378291034', 1, 2025, 1000.00),
(5, 'saramarti@gmail.com', '2024-04-01', '2024-04-15', '4321098765432109', 7, 2024, 600.00);

-- Popolamento della tabella Prenotazione
INSERT INTO Prenotazione (id_alloggio, email, data_visita, disponibilita) VALUES
(1, 'gioromano@gmail.com', '2023-01-25 15:00:00', true),
(2, 'matteobianchi@gmail.com', '2023-02-05 16:30:00', true),
(3, 'giorgioferraro@gmail.com', '2023-02-20 10:00:00', true),
(4, 'sofiaesposito@gmail.com', '2023-03-10 11:30:00', true),
(5, 'saramarti@gmail.com', '2023-04-05 12:00:00', true);

-- Popolamento della tabella Recensione
INSERT INTO Recensione (id_alloggio, email, titolo, voto, descrizione, data_recensione) VALUES
(1, 'gioromano@gmail.com', 'Bellissima esperienza', 5, 'La camera era pulita e accogliente. Ottima posizione!', '2023-02-20'),
(2, 'matteobianchi@gmail.com', 'Consigliato', 4, 'Il monolocale era spazioso e ben arredato. Buon rapporto qualità-prezzo.', '2023-03-01'),
(3, 'giorgioferraro@gmail.com', 'Esperienza positiva', 4, 'Stanza comoda e vicina all università. Proprietario gentile.', '2023-03-15'),
(4, 'sofiaesposito@gmail.com', 'Vacanza da sogno', 5, 'La villa è incredibile. Vista mozzafiato e tutti i comfort disponibili.', '2023-04-01'),
(5, 'saramarti@gmail.com', 'Buon soggiorno', 3, 'Il bilocale era nella media. Niente di eccezionale ma sufficiente per brevi periodi.', '2023-04-10');

-- Popolamento della tabella Servizi
INSERT INTO Servizi (descrizione) VALUES
('Wi-Fi'),
('TV'),
('Parcheggio'),
('Giardino'),
('Cucina attrezzata'),
('Utensili per la pulizia'),
('Utensili per la cucina'),
('Forno'),
('Lavatrice'),
('Lavastoviglie'),
('Asciugatrice'),
('Riscaldamento centralizzato'),
('Aria condizionata'),
('Armadio'),
('Cassettiera'),
('Scrivania'),
('Letto'),
('Ascensore'),
('Piscina'),
('Balcone con vista');

-- Popolamento della tabella Possedimento
INSERT INTO Possedimento (id_servizio, id_alloggio) VALUES
(1, 1),
(2, 1),
(3, 1),
(16, 1),
(17, 1),
(15, 1),
(1, 2),
(2, 2),
(3, 2),
(5, 2),
(6, 2),
(7, 2),
(8, 2),
(9, 2),
(10, 2),
(12, 2),
(13, 2),
(14, 2),
(15, 2),
(16, 2),
(17, 2),
(1, 4),
(2, 4),
(3, 4),
(4, 4),
(5, 4),
(6, 4),
(7, 4),
(8, 4),
(9, 4),
(10, 4),
(12, 4),
(13, 4),
(14, 4),
(15, 4),
(16, 4),
(17, 4),
(19, 4),
(20, 4),
(1, 5),
(2, 5),
(3, 5),
(7, 5),
(8, 5),
(9, 5),
(12, 5),
(13, 5),
(14, 5),
(15, 5),
(16, 5),
(17, 5);