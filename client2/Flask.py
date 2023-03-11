#Flask for ui handing and request handling
from flask import Flask, render_template, request
import threading
import Main as im
import writeFile as wf
import serverSock
import QRScanner
import datetime

selectedItem ="Item 0"

app = Flask(__name__)

@app.route('/')
def login():
    current_date = datetime.date.today()
    # QRScanner.QRReader()
    return render_template('index.html',  currentDate=current_date)

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
    gender = output["gender"]
    wf.writetoCSV(month, item, gender)
    res = im.datasetAnalize()
    return render_template("index.html",currentDate=current_date)

@app.route("/start", methods =['POST',"GET"])
def start():
    im.initProject()
    return render_template("index.html")

@app.route('/getItems', methods =['POST',"GET"])
def getItems():

    current_date = datetime.date.today()
    results = QRScanner.QRReader()
    global selectedItem
    selectedItem = results
    print("Return successful")
    return render_template('index.html',selectItem=selectedItem,  currentDate=current_date)

if __name__ == '__main__':
    # Create two threads: one for running the Flask app, the other for running server connections
    flask_thread = threading.Thread(target=app.run, kwargs={'port': 5002})
    # train_thread = threading.Thread(target=serverSock.serverConnect)

    # QRScanner_thread = threading.Thread(target=QRScanner.QRReader)
    # Start the threads
    # train_thread.start()
    flask_thread.start()
    # QRScanner_thread.start()
    
    # Wait for the threads to finish
    flask_thread.join()
    # train_thread.join()
    # QRScanner_thread.join()



