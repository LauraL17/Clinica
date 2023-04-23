from flask import Flask, render_template, request, redirect, url_for
#import Clinica as c 

app = Flask(__name__)

@app.route("/acasa",methods=['GET'])
def GetAcasa():
    if request.method == 'GET':
        return render_template("Acasa.html")

@app.route("/specializari",methods=['GET'])
def GetSpecializari():
    if request.method == 'GET':
        return render_template("Specializari.html")

@app.route("/echipa",methods=['GET'])
def GetEchipa_Medicala():
    if request.method == 'GET':
        return render_template("Echipa_medicala.html")
    
@app.route("/programari",methods=['GET'])
def GetProgramari():
    if request.method == 'GET':
        return render_template("Programari.html")

@app.route("/rezultate_analize",methods=['GET'])
def GetRezultate():
    if request.method == 'GET':
        return render_template("Rezultate_analize.html")  

@app.route("/tarife",methods=['GET'])
def GetTarife():
    if request.method == 'GET':
        return render_template("Tarife.html")
    
@app.route("/contact",methods=['GET'])
def GetContact():
    if request.method == 'GET':
        return render_template("Contact.html")
    
@app.route("/rapoarte",methods=['GET'])
def GetRapoarte():
    if request.method == 'GET':
        return render_template("Raport.html")
    
# 1. Raport Lista Medici - Specializare/Calificare

@app.route("/raport_specializare_calificare", methods=['POST',"GET"])  
def GenerateReport_Specializare_Calificare():
    if request.method == 'POST':
        data = request.form['Raport_Specializari_Calificare.txt']
        #filename = c.process_data(data)
        
        return render_template("Raport_Specializare_Calificare.html",filename=data)

    return render_template("Raport_Specializare_Calificare.html")

@app.route("/display/Raport_Specializare_Calificare.txt")
def DisplayReport_Specializare_Calificare(filename):
    return redirect(url_for('static',filename= "/files/Raport_Specializari_Calificare.html",code=301))

# 2. Raport Programare Pacienti

@app.route("/raport_programari_pacienti", methods=['POST',"GET"])  
def GenerateReport_Programari_Pacienti():
    if request.method == 'POST':
        data = request.form['Raport_Programari_Pacienti.txt']
        #filename = c.process_data(data)
        
        return render_template("Raport_Programari_Pacienti.html",filename=data)

    return render_template("Raport_Programari_Pacienti.html")

@app.route("/display/Raport_Programari_Pacienti.txt")
def DisplayReport_Programari_Pacienti(filename):
    return redirect(url_for('static',filename= "/files/Raport_Programari_Pacienti.txt",code=301))


# 3. Raport Suma platita de Pacienti
@app.route("/raport_suma_pacienti", methods=['POST',"GET"])  
def GenerateReport_Suma_Pacienti():
    if request.method == 'POST':
        data = request.form['Raport_Suma_Pacienti.txt']
        #filename = c.process_data(data)
        
        return render_template("Raport_Suma_Pacienti.html",filename=data) 

    return render_template("Raport_Suma_Pacienti.html")

@app.route("/display/Raport_Suma_Pacienti.txt")
def DisplayReport_Suma_Pacienti(filename):
    return redirect(url_for('static',filename= "/files/Raport_Suma_Pacienti.txt",code=301))


# 4. Raport - Total Incasari/Specializari
 
@app.route("/raport_total_incasari", methods=['POST',"GET"])  
def GenerateReport_Total_Incasari():
    if request.method == 'POST':
        data = request.form['Raport_Total_Incasari.txt']
        #filename = c.process_data(data) 
        
        return render_template("Raport_Total_Incasari.html",filename=data)

    return render_template("Raport_total_Incasari.html")

@app.route("/display/Raport_Total_Incasari.txt")
def DisplayReport_Total_Incasari(filename):
    return redirect(url_for('static',filename= "/files/Raport_Total_Incasari.html",code=301))
    
app.run(port=5000)   