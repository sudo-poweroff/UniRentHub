DROP SCHEMA URHTestDB;
CREATE  SCHEMA URHTestDB;
use unirenthub;


-- Creazione della tabella Cliente
CREATE TABLE Cliente (
    email VARCHAR(255) PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    cognome VARCHAR(50) NOT NULL,
    tipo_utente ENUM('Studente', 'Locatore') NOT NULL,
    data_nascita DATE,
    numero_carta VARCHAR(16) CHECK(numero_carta >= 16),
    mese_scadenza INT NOT NULL,
    anno_scadenza INT NOT NULL,
    verificato BOOLEAN,
    password VARCHAR(255) CHECK(LENGTH(password) >= 8) NOT NULL,
    data_blocco DATE
);

CREATE TABLE Dipendente (
    email VARCHAR(255) PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    cognome VARCHAR(50) NOT NULL,
    tipo_dipendente ENUM('Homechecker', 'Admin') NOT NULL,
    password VARCHAR(255) CHECK(LENGTH(password) >= 8) NOT NULL
);


-- Creazione della tabella Post
CREATE TABLE Post (
    id_post INT AUTO_INCREMENT PRIMARY KEY,
    titolo VARCHAR(255) NOT NULL,
    descrizione LONGTEXT NOT NULL,
    email VARCHAR(255),
    FOREIGN KEY (email) REFERENCES Cliente(email) ON DELETE SET NULL ON UPDATE CASCADE
);

-- Creazione della tabella Passione
CREATE TABLE Passione (
    id_passione INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);

-- Creazione della tabella Assegnazione
CREATE TABLE Assegnazione (
    id_passione INT,
    email VARCHAR(255),
    FOREIGN KEY (id_passione) REFERENCES Passione(id_passione) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (email) REFERENCES Cliente(email) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Creazione della tabella Segnalazione
CREATE TABLE Segnalazione (
    email VARCHAR(255),
    emailS VARCHAR(255),
    stato VARCHAR(255) NOT NULL,
    motivo VARCHAR(255) NOT NULL,
    FOREIGN KEY (email) REFERENCES Cliente(email) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (emailS) REFERENCES Cliente(email) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Creazione della tabella Università
CREATE TABLE Università (
    denominazione ENUM('Università di Napoli Federico II', 'Politecnico di Milano - Sede Leonardo', 'Università Roma Tre', 'Università degli Studi di Salerno', 'Università La Sapienza') PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    indirizzo VARCHAR(255) NOT NULL
);


-- Creazione della tabella Iscrizione
CREATE TABLE Iscrizione (
    denominazione ENUM('Università di Napoli Federico II', 'Politecnico di Milano - Sede Leonardo', 'Università Roma Tre', 'Università degli Studi di Salerno', 'Università La Sapienza'),
    email VARCHAR(255),
    FOREIGN KEY (denominazione) REFERENCES Università(denominazione) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (email) REFERENCES Cliente(email) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Creazione della tabella Chat
CREATE TABLE Chat (
    id_chat INT AUTO_INCREMENT PRIMARY KEY,
    titolo VARCHAR(255) NOT NULL
);

-- Creazione della tabella Partecipazione
CREATE TABLE Partecipazione (
    id_chat INT AUTO_INCREMENT,
    email VARCHAR(255),
    FOREIGN KEY (id_chat) REFERENCES Chat(id_chat) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (email) REFERENCES Cliente(email) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Creazione della tabella Messaggio
CREATE TABLE Messaggio (
    id_messaggio INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255),
    id_chat INT,
    contenuto VARCHAR(255) NOT NULL,
    FOREIGN KEY (id_chat) REFERENCES Chat(id_chat) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (email) REFERENCES Cliente(email) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Creazione della tabella Alloggio
CREATE TABLE Alloggio (
    id_alloggio INT AUTO_INCREMENT,
    tipo_alloggio ENUM('Stanza condivisa', 'Camera', 'Monolocale', 'Bilocale', 'Trilocale', 'Villa') NOT NULL,
    disponibilità BOOLEAN NOT NULL,
    titolo VARCHAR(255) NOT NULL,
    mq INT CHECK(mq >= 1) NOT NULL,
    n_camere_letto INT DEFAULT 1 CHECK(n_camere_letto > 0) NOT NULL,
    n_bagni INT DEFAULT 1 CHECK(n_bagni > 0) NOT NULL,
    classe_energetica ENUM('A++', 'A+', 'A', 'B', 'C', 'D') NOT NULL,
    arredamenti BOOLEAN NOT NULL,
    data_pubblicazione DATE NOT NULL,
    pannelli_solari BOOLEAN NOT NULL,
    pannelli_fotovoltaici BOOLEAN NOT NULL,
    descrizione LONGTEXT NOT NULL,
    verifica BOOLEAN NOT NULL,
    prezzo DOUBLE CHECK(prezzo >= 0) NOT NULL,
    n_ospiti INT DEFAULT 1 CHECK(n_ospiti > 0) NOT NULL,
    n_stanze INT CHECK(n_stanze >= 1) NOT NULL,
    tasse DOUBLE NOT NULL DEFAULT '5',
    email_dip VARCHAR(255),
    email_loc VARCHAR(255),
    data_verifica DATE,
    PRIMARY KEY (id_alloggio),
    FOREIGN KEY (email_dip) REFERENCES Dipendente(email) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (email_loc) REFERENCES Cliente(email) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Creazione della tabella Indirizzo
CREATE TABLE Indirizzo (
    id_alloggio INT,
    via VARCHAR(255) NOT NULL,
    cap VARCHAR(5) NOT NULL,
    civico VARCHAR(5) NOT NULL,
    citta VARCHAR(255) NOT NULL,
    provincia VARCHAR(2) CHECK(LENGTH(provincia) = 2) NOT NULL,
    FOREIGN KEY (id_alloggio) REFERENCES Alloggio(id_alloggio) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Trigger per aggiungere gli zeri iniziali al cap quando presenti
DELIMITER //
CREATE TRIGGER add_zero_cap BEFORE INSERT ON Indirizzo
FOR EACH ROW
BEGIN
    SET NEW.cap = LPAD(NEW.cap, 5, '0');
END;
// DELIMITER ;

-- Creazione della tabella Immagine
CREATE TABLE Immagine (
    id_immagine INT AUTO_INCREMENT PRIMARY KEY,
    id_alloggio INT,
    path VARCHAR(255) NOT NULL,
    FOREIGN KEY (id_alloggio) REFERENCES Alloggio(id_alloggio) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Creazione della tabella Affittare
CREATE TABLE Affittare (
    id_alloggio INT,
    email VARCHAR(255),
    data_inizio DATE NOT NULL,
    data_fine DATE NOT NULL,
    numero_carta VARCHAR(16) CHECK(numero_carta >= 16) NOT NULL,
    mese_scadenza INT,
    anno_scadenza INT,
    prezzo DOUBLE DEFAULT 0 CHECK(prezzo >= 0) NOT NULL,
    FOREIGN KEY (id_alloggio) REFERENCES Alloggio(id_alloggio) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (email) REFERENCES Cliente(email) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Creazione della tabella Prenotazione
CREATE TABLE Prenotazione (
    id_alloggio INT,
    email VARCHAR(255),
    data_visita DATETIME NOT NULL,
    disponibilita boolean,
    FOREIGN KEY (id_alloggio) REFERENCES Alloggio(id_alloggio) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (email) REFERENCES Cliente(email) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Creazione della tabella Recensione
CREATE TABLE Recensione (
    id_alloggio INT,
    email VARCHAR(255),
    titolo VARCHAR(255) NOT NULL,
    voto INT CHECK(voto >= 0 AND voto <= 5) NOT NULL,
    descrizione VARCHAR(255) NOT NULL,
    data_recensione DATE NOT NULL,
    FOREIGN KEY (id_alloggio) REFERENCES Alloggio(id_alloggio) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (email) REFERENCES Cliente(email) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Creazione della tabella Servizi
CREATE TABLE Servizi (
    id_servizio INT AUTO_INCREMENT PRIMARY KEY,
    descrizione VARCHAR(255) NOT NULL
);

-- Creazione della tabella Possedimento
CREATE TABLE Possedimento (
    id_servizio INT,
    id_alloggio INT,
    FOREIGN KEY (id_alloggio) REFERENCES Alloggio(id_alloggio) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_servizio) REFERENCES Servizi(id_servizio) ON DELETE CASCADE ON UPDATE CASCADE
);
