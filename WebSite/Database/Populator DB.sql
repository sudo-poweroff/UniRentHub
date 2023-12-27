-- Popolamento della tabella Cliente
INSERT INTO Cliente (email, nome, cognome, tipo_utente, data_nascita, numero_carta, data_scadenza, verificato, password) VALUES
('cliente1@example.com', 'Mario', 'Rossi', 'Studente', '1990-01-15', '1234567812345670', '2025-01-01', true, 'password123'),
('cliente2@example.com', 'Luigi', 'Verdi', 'Locatore', '1985-05-20', '9876543298765432', '2024-12-01', true, 'securepass'),
('cliente3@example.com', 'Anna', 'Bianchi', 'Studente', '1998-03-10', '5678901234567890', '2023-11-01', true, 'annapass'),
('cliente4@example.com', 'Giulia', 'Neri', 'Locatore', '1992-08-28', '6543210987654321', '2025-02-01', true, 'giuliapassword'),
('cliente5@example.com', 'Alessio', 'Giallo', 'Studente', '2000-12-05', NULL, NULL, true, 'alessio123'),
('cliente6@example.com', 'Francesca', 'Verde', 'Studente', '1995-07-22', '8765432109876543', '2023-10-01', true, 'francescapass'),
('cliente7@example.com', 'Davide', 'Blu', 'Locatore', '1989-04-18', '3456789012345678', '2024-09-01', true, 'davidepass'),
('cliente8@example.com', 'Elena', 'Rosa', 'Studente', '1996-11-30', '2345678901234567', '2023-08-01', true, 'elenapassword'),
('cliente9@example.com', 'Matteo', 'Arancio', 'Studente', '2003-02-14', NULL, NULL, true, 'matteo2022'),
('cliente10@example.com', 'Giorgio', 'Viola', 'Locatore', '1994-09-08', '4321098765432109', '2024-06-01', true, 'giorgiopass');

-- Popolamento della tabella Dipendente
INSERT INTO Dipendente (email, nome, cognome, tipo_dipendente, password) VALUES
('dipendente1@example.com', 'Giovanna', 'Bianchi', 'Homechecker', 'dipendente123'),
('admin@example.com', 'Admin', 'Admin', 'Admin', 'adminpass'),
('dipendente2@example.com', 'Luca', 'Verdi', 'Homechecker', 'homecheckluca');

-- Popolamento della tabella Post
INSERT INTO Post (titolo, descrizione, email) VALUES
('Titolo Post 1', 'Descrizione Post 1', 'cliente1@example.com'),
('Titolo Post 2', 'Descrizione Post 2', 'cliente2@example.com'),
('Titolo Post 3', 'Descrizione Post 3', 'cliente3@example.com'),
('Titolo Post 4', 'Descrizione Post 4', 'cliente4@example.com'),
('Titolo Post 5', 'Descrizione Post 5', 'cliente5@example.com');

-- Popolamento della tabella Passione
INSERT INTO Passione (nome) VALUES
('Viaggi'),
('Sport'),
('Cucina'),
('Musica'),
('Arte');

-- Popolamento della tabella Assegnazione
INSERT INTO Assegnazione (id_passione, email) VALUES
(1, 'cliente1@example.com'),
(2, 'cliente1@example.com'),
(2, 'cliente2@example.com'),
(3, 'cliente3@example.com'),
(4, 'cliente4@example.com'),
(5, 'cliente5@example.com'),
(1, 'cliente6@example.com'),
(2, 'cliente6@example.com'),
(3, 'cliente7@example.com'),
(4, 'cliente8@example.com');

-- Popolamento della tabella Segnalazione
INSERT INTO Segnalazione (email, emailS, stato, motivo) VALUES
('cliente1@example.com', 'cliente10@example.com', 'Aperta', 'Problema con l\'annuncio'),
('cliente2@example.com', 'cliente10@example.com', 'Chiusa', 'Richiesta informazioni'),
('cliente3@example.com', 'cliente10@example.com' ,'Aperta', 'Problema di pagamento'),
('cliente4@example.com', 'cliente10@example.com', 'Chiusa', 'Richiesta di supporto'),
('cliente5@example.com', 'cliente10@example.com', 'Aperta', 'Problema con l\'account');

-- Popolamento della tabella Università
INSERT INTO Università (denominazione, email, indirizzo) VALUES
('Federico II', 'uniFede@example.com', 'Via Universitaria, 123'),
('Politecnico di Milano', 'polimi@example.com', 'Via Politecnico, 456'),
('Università Roma Tre', 'uniRoma@example.com', 'Via Napoletana, 789'),
('Università degli Studi di Salerno', 'salerno@example.com', 'Via Napoletana, 789'),
('La Sapienza', 'lasapienza@example.com', 'Via Napoletana, 789');

-- Popolamento della tabella Iscrizione
INSERT INTO Iscrizione (denominazione, email) VALUES
('Federico II', 'cliente1@example.com'),
('Politecnico di Milano', 'cliente2@example.com'),
('La Sapienza', 'cliente3@example.com'),
('Università Roma Tre', 'cliente4@example.com'),
('La Sapienza', 'cliente5@example.com'),
('Università Roma Tre', 'cliente6@example.com'),
('Politecnico di Milano', 'cliente7@example.com'),
('Università degli Studi di Salerno', 'cliente8@example.com'),
('Università degli Studi di Salerno', 'cliente9@example.com'),
('Università degli Studi di Salerno', 'cliente10@example.com');

-- Popolamento della tabella Chat
INSERT INTO Chat (titolo) VALUES
('Chat Viaggi'),
('Chat Sport'),
('Chat Cucina'),
('Chat Musica'),
('Chat Arte');

-- Popolamento della tabella Partecipazione
INSERT INTO Partecipazione (id_chat, email) VALUES
(1, 'cliente1@example.com'),
(1, 'cliente2@example.com'),
(2, 'cliente3@example.com'),
(2, 'cliente4@example.com'),
(3, 'cliente5@example.com'),
(3, 'cliente6@example.com'),
(4, 'cliente7@example.com'),
(4, 'cliente8@example.com'),
(5, 'cliente9@example.com'),
(5, 'cliente10@example.com');

-- Popolamento della tabella Messaggio
INSERT INTO Messaggio (email, id_chat, contenuto) VALUES
('cliente1@example.com', 1, 'Ciao a tutti!'),
('cliente2@example.com', 1, 'Salve! Dove avete viaggiato di recente?'),
('cliente3@example.com', 2, 'Qualcuno vuole condividere ricette?'),
('cliente4@example.com', 2, 'Ho appena corso una maratona, qualcuno vuole unirsi?'),
('cliente5@example.com', 3, 'Qualcuno sa suonare uno strumento musicale?'),
('cliente6@example.com', 3, 'Amo dipingere, chi condivide questa passione?'),
('cliente7@example.com', 4, 'Consigli su libri d\'arte?'),
('cliente8@example.com', 4, 'Qualcuno vuole fare una visita al museo?'),
('cliente9@example.com', 5, 'Qualcuno vuole fare una passeggiata artistica?'),
('cliente10@example.com', 5, 'Quali artisti preferite?');

-- Popolamento della tabella Alloggio
INSERT INTO Alloggio (tipo_alloggio, disponibilità, titolo, mq, n_camere_letto, n_bagni, classe_energetica, arredamenti, data_pubblicazione, pannelli_solari, pannelli_fotovoltaici, descrizione, verifica, prezzo, n_ospiti, n_stanze, tasse, email_dip, email_loc, data_verifica) VALUES
('Camera', TRUE, 'Camera singola in centro', 20, 1, 1, 'A', TRUE, '2023-01-10', TRUE, FALSE, 'Bellissima camera in pieno centro della città', TRUE, 50.00, 1, 1, 10.00, 'dipendente1@example.com', 'cliente1@example.com', '2023-01-15'),
('Monolocale', TRUE, 'Monolocale moderno', 40, 1, 1, 'B', TRUE, '2023-01-12', FALSE, TRUE, 'Monolocale con tutti i comfort', TRUE, 80.00, 2, 2, 15.00, 'dipendente1@example.com', 'cliente2@example.com', '2023-01-20'),
('Stanza condivisa', TRUE, 'Stanza condivisa per studenti', 30, 2, 1, 'C', TRUE, '2023-02-01', FALSE, TRUE, 'Stanza condivisa in zona universitaria', TRUE, 40.00, 2, 2, 5.00, 'dipendente2@example.com', 'cliente3@example.com', '2023-02-10'),
('Villa', TRUE, 'Villa con piscina', 200, 4, 3, 'A+', TRUE, '2023-02-15', TRUE, TRUE, 'Villa di lusso con vista panoramica', TRUE, 300.00, 6, 5, 50.00, 'dipendente2@example.com', 'cliente4@example.com', '2023-03-01'),
('Bilocale', TRUE, 'Bilocale vicino al campus', 50, 1, 1, 'B', TRUE, '2023-03-01', FALSE, FALSE, 'Bilocale ideale per studenti', TRUE, 60.00, 2, 2, 10.00, 'dipendente1@example.com', 'cliente5@example.com', '2023-03-10');

-- Popolamento della tabella Indirizzo
INSERT INTO Indirizzo (id_alloggio, via, cap, civico, citta, provincia) VALUES
(1, 'Via Principale', 12345, '12A', 'Roma', 'RM'),
(2, 'Via Moderna', 56789, '34B', 'Milano', 'MI'),
(3, 'Via Universitaria', 34567, '45', 'Roma', 'RM'),
(4, 'Via Panoramica', 10123, '78', 'Napoli', 'NA'),
(5, 'Via Campus', 54321, '56', 'Milano', 'MI');

-- Popolamento della tabella Immagine
INSERT INTO Immagine (id_alloggio, path) VALUES
(1, '/images/camera.jpg'),
(2, '/images/monolocale.jpg'),
(3, '/images/stanza.jpg'),
(4, '/images/villa.jpg'),
(5, '/images/bilocale.jpg');

-- Popolamento della tabella Affittare
INSERT INTO Affittare (id_alloggio, email, data_inizio, data_fine, numero_carta, data_scadenza, prezzo) VALUES
(1, 'cliente1@example.com', '2023-02-01', '2023-02-15', '1234567812345670', '2025-01-01', 400.00),
(2, 'cliente2@example.com', '2023-02-10', '2023-02-25', '1234567812345670', '2025-01-01', 700.00),
(3, 'cliente3@example.com', '2023-03-01', '2023-03-15', '1234567812345670', '2025-01-01', 300.00),
(4, 'cliente4@example.com', '2023-03-15', '2023-03-30', '1234567812345670', '2025-01-01', 1000.00),
(5, 'cliente5@example.com', '2023-04-01', '2023-04-15', '1234567812345670', '2025-01-01', 600.00);

-- Popolamento della tabella Prenotazione
INSERT INTO Prenotazione (id_alloggio, email, data_visita) VALUES
(1, 'cliente2@example.com', '2023-01-25'),
(2, 'cliente1@example.com', '2023-02-05'),
(3, 'cliente4@example.com', '2023-02-20'),
(4, 'cliente3@example.com', '2023-03-10'),
(5, 'cliente6@example.com', '2023-04-05');

-- Popolamento della tabella Recensione
INSERT INTO Recensione (id_alloggio, email, titolo, voto, descrizione, data_recensione) VALUES
(1, 'cliente1@example.com', 'Bellissima esperienza', 5, 'La camera era pulita e accogliente. Ottima posizione!', '2023-02-20'),
(2, 'cliente2@example.com', 'Consigliato', 4, 'Il monolocale era spazioso e ben arredato. Buon rapporto qualità-prezzo.', '2023-03-01'),
(3, 'cliente3@example.com', 'Esperienza positiva', 4, 'Stanza comoda e vicina all\'università. Proprietario gentile.', '2023-03-15'),
(4, 'cliente4@example.com', 'Vacanza da sogno', 5, 'La villa è incredibile. Vista mozzafiato e tutti i comfort disponibili.', '2023-04-01'),
(5, 'cliente5@example.com', 'Buon soggiorno', 3, 'Il bilocale era nella media. Niente di eccezionale ma sufficiente per brevi periodi.', '2023-04-10');

-- Popolamento della tabella Servizi
INSERT INTO Servizi (descrizione) VALUES
('Wi-Fi'),
('TV'),
('Parcheggio'),
('Giardino'),
('Aria condizionata');

-- Popolamento della tabella Possedimento
INSERT INTO Possedimento (id_servizio, id_alloggio) VALUES
(1, 1),
(2, 1),
(3, 2),
(4, 4),
(5, 5);

