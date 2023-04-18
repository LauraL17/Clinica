
--Create database
CREATE DATABASE Clinica;

--Create Tables
--Specializare

USE Clinica;
CREATE TABLE IF NOT EXISTS Specializare (
    IDSpecializare int,
    Denumire varchar(100)
);
    ALTER TABLE Specializare ADD PRIMARY KEY (IDSpecializare);

--Calificare
USE Clinica;
CREATE TABLE IF NOT EXISTS Calificare (
    IDCalificare int,
    Denumire varchar(100)
);
    ALTER TABLE Calificare ADD PRIMARY KEY (IDCalificare);

--Doctori
USE Clinica;
CREATE TABLE IF NOT EXISTS Doctori (
    IDDoctor int,
    Nume varchar(50) not null default('Ionescu'),
    Prenume varchar(100),
    IDCalificare int,
    IDSpecializare int
);
    ALTER TABLE Doctori 
    ADD PRIMARY KEY (IDDoctor),
    ADD  FOREIGN KEY (IDCalificare)
        REFERENCES Calificare(IDCalificare),
    ADD FOREIGN KEY (IDSpecializare)
        REFERENCES Specializare(IDSpecializare);


--Pacienti
USE Clinica;
CREATE TABLE IF NOT EXISTS Pacienti (
    IDPacient int,
    Nume varchar(50) not null default('Ionescu'),
    Prenume varchar(100),
    Sex varchar(50),
    CNP bigint,
    Varsta int
);
    ALTER TABLE Pacienti ADD PRIMARY KEY (IDPacient);

--Programari
USE Clinica;
CREATE TABLE IF NOT EXISTS Programari (
    IDPacient int,
    IDSpecializare int,
    IDDoctor int
);
    ALTER TABLE Programari
        ADD FOREIGN KEY (IDDoctor)
            REFERENCES Doctori(IDDoctor),
        ADD FOREIGN KEY (IDSpecializare)
            REFERENCES Specializare(IDSpecializare),
        ADD FOREIGN KEY (IDPacient)
            REFERENCES Pacienti(IDPacient);

--Incasari
USE Clinica;
CREATE TABLE IF NOT EXISTS Incasari (
    IDPacient int,
    IDSpecializare int,
    Suma int
);
    ALTER TABLE Incasari
        ADD FOREIGN KEY (IDPacient)
            REFERENCES Pacienti(IDPacient),
        ADD FOREIGN KEY (IDSpecializare)
            REFERENCES Specializare(IDSpecializare);

#Programarile pacientilor - Nume/Prenume/CNP --> IdDoctor/Specializarea/Nume/Prenume
Select 
    Pacienti.IDPacient,
    Pacienti.Nume as Nume_pacient,
    Pacienti.Prenume as Prenume_pacient,
    Pacienti.CNP,
    Pacienti.Sex,
    Specializare.Denumire as Specializare,
    Doctori.Nume as Nume_doctor,
    Doctori.Prenume as Prenume_doctor
   
FROM (Programari
INNER JOIN Doctori ON Programari.IDDoctor = Doctori.IDDoctor
INNER JOIN Pacienti ON Pacienti.IDPacient = Programari.IDPacient
INNER JOIN Specializare ON Doctori.IDSpecializare = Specializare.IDSpecializare
);

#Specializarile si calificarea doctorilor
SELECT
    Doctori.Nume,
    Doctori.Prenume,
    Specializare.Denumire as Specializare,
    Calificare.Denumire as Calificare

FROM(Doctori
INNER JOIN Specializare on Specializare.IDSpecializare = Doctori.IDSpecializare
INNER JOIN Calificare on Calificare.IDCalificare = Doctori.IDCalificare
);

#Suma platita de fiecare pacient
SELECT
    Pacienti.Nume,
    Pacienti.Prenume,
    Specializare.Denumire as Specializare,
    Incasari.Suma
    
FROM (Incasari
INNER JOIN Programari on Programari.IDPacient = Incasari.IDPacient
INNER JOIN Specializare on Specializare.IDSpecializare = Incasari.IDSpecializare
INNER JOIN Pacienti on Pacienti.IDPacient = Incasari.IDPacient
);

#Totalul Incasarilor grupate pe specializari
SELECT
    Incasari.IDSpecializare,
    Specializare.Denumire as Specializare,
    SUM(Suma) as Total_incasari
FROM Incasari
INNER JOIN Specializare on Specializare.IDSpecializare = Incasari.IDSpecializare
GROUP BY IDSpecializare;
