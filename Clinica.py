import mysql.connector
        
class Doctori:
    def __init__(self,iddoctor,nume,prenume,idcalificare,idspecializare):
        self.iddoctor = iddoctor
        self.nume = nume
        self.prenume = prenume
        self.idcalificare = idcalificare
        self.idspecializare = idspecializare
    
class Pacienti:
    def __init__(self,idpacient,nume,prenume,sex,cnp,varsta):
        self.idpacient = idpacient
        self.nume = nume
        self.prenume = prenume
        self.sex = sex
        self.cnp = cnp
        self.varsta = varsta

class Calificare:
    def __init__(self,idcalificare, denumire):
        self.idcalificare = idcalificare
        self.denumire = denumire

class Specializare:
    def __init__(self,idspecializare, denumire):
        self.idspecializare = idspecializare
        self.denumire = denumire

class Programari:
    def __init__(self,idpacient,idspecializare,iddoctor):
        self.idpacient = idpacient
        self.idspecializare = idspecializare
        self.iddoctor = iddoctor
        
class Incasari:
    def __init__(self,idpacient,idspecializare,suma):
        self.idpacient = idpacient
        self.idspecializare = idspecializare
        self.suma = suma
        
    
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
    
def populate_tables():
    insert_data("C:\\Users\\Laura Haiduc\\Desktop\\HTML\\Clinica\\static\\files\\Specializare.txt","Specializare")
    insert_data("C:\\Users\\Laura Haiduc\\Desktop\\HTML\\Clinica\\static\\files\\Calificare.txt","Calificare")
    insert_data("C:\\Users\\Laura Haiduc\\Desktop\\HTML\\Clinica\\static\\files\\Doctori.txt","Doctori")
    insert_data("C:\\Users\\Laura Haiduc\\Desktop\\HTML\\Clinica\\static\\files\\Pacienti.txt","Pacienti")
    insert_data("C:\\Users\\Laura Haiduc\\Desktop\\HTML\\Clinica\\static\\files\\Programari.txt","Programari")
    insert_data("C:\\Users\\Laura Haiduc\\Desktop\\HTML\\Clinica\\static\\files\\Incasari.txt","Incasari")
          
populate_tables()

