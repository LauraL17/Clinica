import mysql.connector

def get_table_column_names(tableName):
    mydb = mysql.connector.connect(
    host="DESKTOP-AFTVT3M",
    user="LH",
    password="MySQL2020!",
    database="Clinica"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE " +
                     "TABLE_SCHEMA = 'Clinica' AND TABLE_NAME = '" + 
                     tableName + "'")

    myresult = mycursor.fetchall()

    result = []
    for x in myresult:
        result.append(x[0])

    mycursor.close()

    return result

def insert_data(fileName,tableName):
    
    mydb = mysql.connector.connect(
    host="DESKTOP-AFTVT3M",
    user="LH",
    password="MySQL2020!",
    database="Clinica"
    )
    mycursor = mydb.cursor()
    file = open(fileName, 'r')
      
    colNames = get_table_column_names(tableName)
    
    lines = file.readlines()
    for line in lines:
        query = "Insert Into " + tableName + "("
        i = 0
        strCols = ''
        for colName in colNames:
            strCols += colName + ","
            i += 1
        strCols = strCols[:-1]
        query += strCols + ") values ("
        
        for j in range(0,i):
            print(j)
            query += "%s," 
        query = query[:-1]
        
        query += ")"
        print(query)

        values = line.split(",")
        mycursor.execute(query, values)
        mydb.commit()

    mycursor.close()

def generate_report():
    mydb = mysql.connector.connect(
    host="DESKTOP-AFTVT3M",
    user="LH",
    password="MySQL2020!",
    database="Clinica"
    )
    mycursor = mydb.cursor()
    
    
# 1. Raport Programarile pacientilor

query = """
Select 
    Pacienti.IDPacient,
    Pacienti.Nume as Nume_pacient,
    Pacienti.Prenume as Prenume_pacient,
    Pacienti.CNP,
    Pacienti.Sex,
    Specializare.Denumire as Specializare,
    Doctori.Nume as Nume_doctor,
    Doctori.Prenume as Prenume_doctor
   
FROM Programari
INNER JOIN Doctori ON Programari.IDDoctor = Doctori.IDDoctor
INNER JOIN Pacienti ON Pacienti.IDPacient = Programari.IDPacient
INNER JOIN Specializare ON Doctori.IDSpecializare = Specializare.IDSpecializare
"""
def generate_report():
    mydb = mysql.connector.connect(
    host="DESKTOP-AFTVT3M",
    user="LH",
    password="MySQL2020!",
    database="Clinica"
    )
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    mycursor.close()
    mydb.close()

    return myresult

def write_data(file, results, forHtml):
    forHtml = "C:\\Users\\Laura Haiduc\\Desktop\\HTML\\Clinica\\templates\\Raport.html"
    f = open(file,"w")
    if forHtml:
        f.writelines("IDPacient Nume_Pacient Prenume_Pacient CNP Sex Specializare Nume_Doctor \n")
    for result in results:
        strLine = str(result)
        if forHtml:
            strLine = strLine.replace("(","").replace(")","")
            #f.writelines(strLine)
        #else:
            #f.writelines(strLine)
        strLines = strLine.split(",")
        for word in strLines:
            word = word.replace("\n","").replace("'","") + "    "
            f.write(word)
        f.writelines("\n")
    f.close()
    
def process_data(filename):
    #populate_tables()
    report = generate_report()
    filename = "C:\\Users\\Laura Haiduc\\Desktop\\HTML\\Clinica\\static\\files\\Raport_Programari_Pacienti.txt"
    write_data(filename, report, True)
    return filename   

if input("Doriti sa populati baza de date?(y/n)") == "y":
    process_data("C:\\Users\\Laura Haiduc\\Desktop\\HTML\\Clinica\\static\\files\\Raport_Programari_Pacienti.txt")
print("Se genereaza raportul ...")
report  = generate_report()
print("Raportul a fost generat!")
write_data("C:\\Users\\Laura Haiduc\\Desktop\\HTML\\Clinica\\static\\files\\Raport_Programari_Pacienti.txt",report,"C:\\Users\\Laura Haiduc\\Desktop\\HTML\\Clinica\\templates\\Raport.html")
print("Raportul a fost tiparit in fisierul report.txt din directorul curent!")

# 2. Raport Specializare/Calificare doctori

query = """
SELECT
    Doctori.Nume,
    Doctori.Prenume,
    Specializare.Denumire as Specializare,
    Calificare.Denumire as Calificare

FROM Doctori
INNER JOIN Specializare on Specializare.IDSpecializare = Doctori.IDSpecializare
INNER JOIN Calificare on Calificare.IDCalificare = Doctori.IDCalificare
"""
def generate_report():
    mydb = mysql.connector.connect(
    host="DESKTOP-AFTVT3M",
    user="LH",
    password="MySQL2020!",
    database="Clinica"
    )
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    mycursor.close()
    mydb.close()

    return myresult

def write_data(file, results, forHtml):
    forHtml = "C:\\Users\\Laura Haiduc\\Desktop\\HTML\\Clinica\\templates\\Raport.html"
    f = open(file,"w")
    if forHtml:
        f.writelines("Nume_Doctor Prenume_Doctor Specializare Calificare \n")
    for result in results:
        strLine = str(result)
        if forHtml:
            strLine = strLine.replace("(","").replace(")","")
            #f.writelines(strLine)
        #else:
            #f.writelines(strLine)
        strLines = strLine.split(",")
        for word in strLines:
            word = word.replace("\n","").replace("'","") + "    "
            f.write(word)
        f.writelines("\n")
    f.close()
    
def process_data(filename):
    #populate_tables()
    report = generate_report()
    filename = "C:\\Users\\Laura Haiduc\\Desktop\\HTML\\Clinica\\static\\files\\Raport_Specializari_Calificare.txt"
    write_data(filename, report, True)
    return filename   

if input("Doriti sa populati baza de date?(y/n)") == "y":
    process_data("C:\\Users\\Laura Haiduc\\Desktop\\HTML\\Clinica\\static\\files\\Raport_Specializari_Calificare.txt")
print("Se genereaza raportul ...")
report  = generate_report()
print("Raportul a fost generat!")
write_data("C:\\Users\\Laura Haiduc\\Desktop\\HTML\\Clinica\\static\\files\\Raport_Specializari_Calificare.txt",report,"C:\\Users\\Laura Haiduc\\Desktop\\HTML\\Clinica\\templates\\Raport.html")
print("Raportul a fost tiparit in fisierul report.txt din directorul curent!")


# 3. Raport Suma platita de fiecare pacient

query = """
SELECT
    Pacienti.Nume,
    Pacienti.Prenume,
    Specializare.Denumire as Specializare,
    Incasari.Suma
    
FROM Incasari
INNER JOIN Programari on Programari.IDPacient = Incasari.IDPacient
INNER JOIN Specializare on Specializare.IDSpecializare = Incasari.IDSpecializare
INNER JOIN Pacienti on Pacienti.IDPacient = Incasari.IDPacient
"""
def generate_report():
    mydb = mysql.connector.connect(
    host="DESKTOP-AFTVT3M",
    user="LH",
    password="MySQL2020!",
    database="Clinica"
    )
    mycursor = mydb.cursor()
    
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    mycursor.close()
    mydb.close()

    return myresult

def write_data(file, results, forHtml):
    forHtml = "C:\\Users\\Laura Haiduc\\Desktop\\HTML\\Clinica\\templates\\Raport.html"
    f = open(file,"w")
    if forHtml:
        f.writelines("Nume_Pacient Prenume_Pacient Specializare Suma_Platita \n")
    for result in results:
        strLine = str(result)
        if forHtml:
            strLine = strLine.replace("(","").replace(")","")
            #f.writelines(strLine)
        #else:
            #f.writelines(strLine)
        strLines = strLine.split(",")
        for word in strLines:
            word = word.replace("\n","").replace("'","") + "    "
            f.write(word)
        f.writelines("\n")
    f.close()
    
def process_data(filename):
    #populate_tables()
    report = generate_report()
    filename = "C:\\Users\\Laura Haiduc\\Desktop\\HTML\\Clinica\\static\\files\\Raport_Suma_Pacienti.txt"
    write_data(filename, report, True)
    return filename   

if input("Doriti sa populati baza de date?(y/n)") == "y":
    process_data("C:\\Users\\Laura Haiduc\\Desktop\\HTML\\Clinica\\static\\files\\Raport_Suma_Pacienti.txt")
print("Se genereaza raportul ...")
report  = generate_report()
print("Raportul a fost generat!")
write_data("C:\\Users\\Laura Haiduc\\Desktop\\HTML\\Clinica\\static\\files\\Raport_Suma_Pacienti.txt",report,"C:\\Users\\Laura Haiduc\\Desktop\\HTML\\Clinica\\templates\\Raport.html")
print("Raportul a fost tiparit in fisierul report.txt din directorul curent!")


# 4. Raport Total Incasari/Specializari

query = """
SELECT
    Incasari.IDSpecializare,
    Specializare.Denumire as Specializare,
    SUM(Suma) as Total_incasari
FROM Incasari
INNER JOIN Specializare on Specializare.IDSpecializare = Incasari.IDSpecializare
GROUP BY IDSpecializare
"""
def generate_report():
    mydb = mysql.connector.connect(
    host="DESKTOP-AFTVT3M",
    user="LH",
    password="MySQL2020!",
    database="Clinica"
    )
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    mycursor.close()
    mydb.close()

    return myresult

def write_data(file, results, forHtml):
    forHtml = "C:\\Users\\Laura Haiduc\\Desktop\\HTML\\Clinica\\templates\\Raport.html"
    f = open(file,"w")
    if forHtml:
        f.writelines("IDSpecializare Specializare Total_incasari \n")
    for result in results:
        strLine = str(result)
        if forHtml:
            strLine = strLine.replace("(","").replace(")","")
            #f.writelines(strLine)
        #else:
            #f.writelines(strLine)
        strLines = strLine.split(",")
        for word in strLines:
            word = word.replace("\n","").replace("'","") + "    "
            f.write(word)
        f.writelines("\n")
    f.close()
    
def process_data(filename):
    #populate_tables()
    report = generate_report()
    filename = "C:\\Users\\Laura Haiduc\\Desktop\\HTML\\Clinica\\static\\files\\Raport_Total_Incasari.txt"
    write_data(filename, report, True)
    return filename   

if input("Doriti sa populati baza de date?(y/n)") == "y":
    process_data("C:\\Users\\Laura Haiduc\\Desktop\\HTML\\Clinica\\static\\files\\Raport_Total_Incasari.txt")
print("Se genereaza raportul ...")
report  = generate_report()
print("Raportul a fost generat!")
write_data("C:\\Users\\Laura Haiduc\\Desktop\\HTML\\Clinica\\static\\files\\Raport_Total_Incasari.txt",report,"C:\\Users\\Laura Haiduc\\Desktop\\HTML\\Clinica\\templates\\Raport.html")
print("Raportul a fost tiparit in fisierul report.txt din directorul curent!")







