import _mysql.connector


def generate_report():
    mydb = mysql.connector.connect(
    host="DESKTOP-AFTVT3M",
    user="LH",
    password="MySQL2020!",
    database="facultate"
    )
    mycursor = mydb.cursor()

    query = """Select S.NrMatricol,
                S.Nume,
                S.Prenume,
                S.An,
                SP.Descriere as DenumireSpecializare,
                S.Grupa,
                M.Denumire as Materie,
                P.Nume,
                P.Prenume,
                C.Denumire as CatedraProfesor
            From
                studenti S Inner Join Specializari SP on S.IDSpecializare = SP.IDSpecializare
                Inner Join Materii M on M.IDSpecializare = SP.IDSpecializare
                Inner Join Profesori P on M.IDMaterie = P.IDMaterie
                Inner Join Catedre C on P.IDCatedra = C.IDCatedra"""

    mycursor.execute(query)
    myresult = mycursor.fetchall()

    mycursor.close()
    mydb.close()

    return myresult

def write_data(file, results, forHtml):
    f = open(file,"w")
    if forHtml:
        f.writelines("Nume Student  Prenume Student An  Specializare    Grupa   Materie Nume Profesor   Prenume Profesor    Catedra Profesor\n")
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
    filename = "C:\\Users\\Laura Haiduc\\Desktop\\Python\\Cursuri - Practic\\Facultate\\static\\files\\" + filename
    write_data(filename, report, True)
    return filename  
 
generate_report()

# Main program

'''
if input("Doriti sa populati baza de date?(y/n)") == "y":
    populate_tables()
print("Se genereaza raportul ...")
report  = generate_report()
print("Raportul a fost generat!")
write_data("static\\report.txt",report)
print("Raportul a fost tiparit in fisierul report.txt din directorul curent!")
'''
