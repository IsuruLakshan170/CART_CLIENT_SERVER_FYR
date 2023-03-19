#Flask for ui handing and request handling
from flask import Flask, render_template, request
from threading import Thread
import Main as im
import writeFile as wf
import QRScanner
import datetime
import client 

selectedItem ="Item 0"

app = Flask(__name__)

@app.route('/')
def load():
    return render_template('home.html')


@app.route('/moveHome', methods =['POST',"GET"])
def moveHome():
    return render_template('home.html')

@app.route('/moveAdmin', methods =['POST',"GET"])
def moveAdmin():
    return render_template('admin.html')

@app.route("/start", methods =['POST',"GET"])
def start():
    im.initProject()
    return render_template("admin.html")

@app.route('/getItems', methods =['POST',"GET"])
def getItems():
    current_date = datetime.date.today()
    results = QRScanner.QRReader()
    global selectedItem
    selectedItem = results
    return render_template('home.html',selectItem=selectedItem,  currentDate=current_date)

@app.route("/result", methods =['POST',"GET"])
def result():
    global selectedItem
    current_date = datetime.date.today()
    output = request.form.to_dict()
    month = datetime.datetime.now().month
    item = 0
    if selectedItem == "Item 1":
        item =1
    elif selectedItem == "Item 2":
        item =2
    elif selectedItem == "Item 3":
        item =3
    elif selectedItem == "Item 4":
        item =4
    elif selectedItem == "Item 5":
        item =5
    elif selectedItem == "Item 6":
        item =6
    gender = output["gender"]
    wf.writetoCSV(month, item, gender)
    # im.datasetAnalize()
    return render_template("home.html",currentDate=current_date)

def flask_thread():
    app.run()

if __name__ == '__main__':
    t = Thread(target=app.run, kwargs={'port': 5001})
    t.start()
    client.backgroudNetworkProcess()
