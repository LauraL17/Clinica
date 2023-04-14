
--Create database
CREATE DATABASE Clinica;

--Create Tables
--Specializare

USE Clinica;
CREATE TABLE IF NOT EXISTS Specializare (
    IDSpecializare int PRIMARY KEY,
    Denumire varchar(100)
);

--Calificare
USE Clinica;
CREATE TABLE IF NOT EXISTS Calificare (
    IDCalificare int PRIMARY KEY,
    Denumire varchar(100)
);

--Doctori
USE Clinica;
CREATE TABLE IF NOT EXISTS Doctori (
    IDDoctor int PRIMARY KEY,
    Nume varchar(50) not null default('Ionescu'),
    Prenume varchar(100),
    IDCalificare int,
    IDSpecializare int,
    FOREIGN KEY (IDCalificare)
        REFERENCES Calificare(IDCalificare),
    FOREIGN KEY (IDSpecializare)
        REFERENCES Specializare(IDSpecializare)
);

--Pacienti
USE Clinica;
CREATE TABLE IF NOT EXISTS Pacienti (
    IDPacient int PRIMARY KEY,
    Nume varchar(50) not null default('Ionescu'),
    Prenume varchar(100),
    Sex varchar(50),
    CNP bigint,
    Varsta int
);

--Programari
USE Clinica;
CREATE TABLE IF NOT EXISTS Programari (
    IDPacient int,
    IDSpecializare int,
    IDDoctor int,
    FOREIGN KEY (IDSpecializare)
        REFERENCES Specializare(IDSpecializare),
    FOREIGN KEY (IDDoctor)
        REFERENCES Doctori(IDDoctor),
    FOREIGN KEY (IDPacient)
        REFERENCES Doctori(IDDoctor)
);

--Incasari
USE Clinica;
CREATE TABLE IF NOT EXISTS Incasari (
    IDPacient int,
    IDSpecializare int,
    Suma int,
    FOREIGN KEY (IDPacient)
        REFERENCES Pacienti(IDPacient),
    FOREIGN KEY (IDSpecializare)
        REFERENCES Specializare(IDSpecializare)
);

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

#Totalul Incasarilor pe specializari
SELECT
    Incasari.IDSpecializare,
    Specializare.Denumire as Specializare,
    SUM(Suma) AS Total_incasari
FROM Incasari
INNER JOIN Specializare on Specializare.IDSpecializare = Incasari.IDSpecializare
GROUP BY IDSpecializare




