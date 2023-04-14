from flask import Flask, render_template, request, redirect, url_for
#import Clinica as c 

app = Flask(__name__)

@app.route("/acasa", methods=['POST',"GET"])  
def GenerateReport():
    if request.method == 'POST':
        data = request.form['filename']
        #filename = c.process_data(data)
        
        return render_template("Acasa.html",filename=data)

    return render_template("Acasa.html")

@app.route("/display/<filename>")
def DisplayReport(filename):
    return redirect(url_for('static',filename= '/files/'+filename),code=301)

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

app.run(port=5000)