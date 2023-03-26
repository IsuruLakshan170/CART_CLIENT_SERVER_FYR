#Flask for ui handing and request handling
from flask import Flask, render_template, request
from threading import Thread
import Main as im
import writeFile as wf
import QRScanner
import datetime
import client 

selectedItem ="Item 0"
ItemListArray = [];
totalBill = 0

app = Flask(__name__)
headings=("Name","Number","Price","Amount","Total price")

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
    global selectedItem
    global totalBill
    
    current_date = datetime.date.today()
    results = QRScanner.QRReader()
    selectedItem=results
    data =ItemListArray
   
    # print(results)
    return render_template('home.html',Item_Name=results[0],Item_No=results[1],Item_Price=results[2], currentDate=current_date,headings=headings,data=data,totalBill=totalBill)

@app.route("/result", methods =['POST',"GET"])
def result():
    global selectedItem
    global ItemListArray
    global totalBill
    current_date = datetime.date.today()
    output = request.form.to_dict()
    month = datetime.datetime.now().month
    item = 0
    selectedItemItemNo =selectedItem[1]
    if selectedItemItemNo == "Item 1":
        item =1
    elif selectedItemItemNo == "Item 2":
        item =2
    elif selectedItemItemNo == "Item 3":
        item =3
    elif selectedItemItemNo == "Item 4":
        item =4
    elif selectedItemItemNo == "Item 5":
        item =5
    elif selectedItemItemNo == "Item 6":
        item =6
    gender = output["gender"]
    itemCount = output["itemCount"]
    selectedItem[3] = itemCount
    itemPrice=selectedItem[2]
    selectedItem[4] =int(itemPrice)*int(itemCount)
    totalBill=int(totalBill)+int(selectedItem[4])
     #update the globle array
    ItemListArray.append(selectedItem)
    print(selectedItem)
    print(ItemListArray)
    data =ItemListArray
    wf.writetoCSV(month, item, gender)
    # im.datasetAnalize()
    return render_template("home.html" ,cartData=ItemListArray,currentDate=current_date,headings=headings,data=data,totalBill=totalBill)

def flask_thread():
    app.run()

if __name__ == '__main__':
    t = Thread(target=app.run, kwargs={'port': 5002})
    t.start()
    # client.backgroudNetworkProcess()
