#Flask for ui handing and request handling
from flask import Flask, render_template, request
from threading import Thread
import Main as im
import writeFile as wf
import QRScanner
import datetime
import client 
import modelAccuracy as getThreand

selectedItem ="Item 0"
ItemListArray = [];
totalBill = 0
threandingArray=[["https://aldprdproductimages.azureedge.net/media/resized/$Aldi_GB/19.05.22/4088600260457_0_XL.jpg" , "https://www.bigbasket.com/media/uploads/p/xxl/20004325_10-uncle-chips-uncle-chips-potato-chips-plain-salted-flavour.jpg" , 
                  "https://m.media-amazon.com/images/W/IMAGERENDERING_521856-T2/images/I/813xqlCcX6S._SL1500_.jpg" ,
                  "https://m.media-amazon.com/images/W/IMAGERENDERING_521856-T1/images/I/813axPlVxBL.jpg"],
                 ["https://cdn.takas.lk/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/0/2/02_1.png" , "https://5.imimg.com/data5/ANDROID/Default/2020/10/YU/QD/UL/35343054/prod-20201011-0159397534769397062872599-jpg-500x500.jpg" , "https://food.fnr.sndimg.com/content/dam/images/food/products/2020/1/7/rx_vegetable-goldfish-sweet-carrot.jpg.rend.hgtvcom.616.616.suffix/1578432241151.jpeg" , "https://i0.wp.com/priyadi.lk/wp-content/uploads/2022/06/easy_day_porridge-1.png?fit=230%2C356&ssl=1"],
                 ["https://m.media-amazon.com/images/W/IMAGERENDERING_521856-T1/images/I/813axPlVxBL.jpg" , "https://images.albertsons-media.com/is/image/ABS/960123886-A1C1?$ng-ecom-pdp-mobile$&defaultImage=Not_Available" , "https://food.fnr.sndimg.com/content/dam/images/food/products/2020/1/7/rx_vegetable-goldfish-sweet-carrot.jpg.rend.hgtvcom.616.616.suffix/1578432241151.jpeg" , "https://www.onlinekade.lk/wp-content/uploads/2021/10/8901491101844-300x300.jpg"],
                 ["https://aldprdproductimages.azureedge.net/media/resized/$Aldi_GB/19.05.22/4088600260457_0_XL.jpg" , "https://5.imimg.com/data5/ANDROID/Default/2020/10/YU/QD/UL/35343054/prod-20201011-0159397534769397062872599-jpg-500x500.jpg" , "https://food.fnr.sndimg.com/content/dam/images/food/products/2020/1/7/rx_vegetable-goldfish-sweet-carrot.jpg.rend.hgtvcom.616.616.suffix/1578432241151.jpeg" , "https://i0.wp.com/priyadi.lk/wp-content/uploads/2022/06/easy_day_porridge-1.png?fit=230%2C356&ssl=1"],
                 ["https://aldprdproductimages.azureedge.net/media/resized/$Aldi_GB/19.05.22/4088600260457_0_XL.jpg" , "https://5.imimg.com/data5/ANDROID/Default/2020/10/YU/QD/UL/35343054/prod-20201011-0159397534769397062872599-jpg-500x500.jpg" , "https://food.fnr.sndimg.com/content/dam/images/food/products/2020/1/7/rx_vegetable-goldfish-sweet-carrot.jpg.rend.hgtvcom.616.616.suffix/1578432241151.jpeg" , "https://i0.wp.com/priyadi.lk/wp-content/uploads/2022/06/easy_day_porridge-1.png?fit=230%2C356&ssl=1"],
                 ["https://aldprdproductimages.azureedge.net/media/resized/$Aldi_GB/19.05.22/4088600260457_0_XL.jpg" , "https://5.imimg.com/data5/ANDROID/Default/2020/10/YU/QD/UL/35343054/prod-20201011-0159397534769397062872599-jpg-500x500.jpg" , "https://food.fnr.sndimg.com/content/dam/images/food/products/2020/1/7/rx_vegetable-goldfish-sweet-carrot.jpg.rend.hgtvcom.616.616.suffix/1578432241151.jpeg" , "https://i0.wp.com/priyadi.lk/wp-content/uploads/2022/06/easy_day_porridge-1.png?fit=230%2C356&ssl=1"]
                 ]
currentThreandArray=[]
app = Flask(__name__)
headings=("Name","Number","Price","Amount","Total price")

#find current threand
def findCurrentThreandArray():
    global currentThreandArray
   
    global threandingArray
    #get current threand
    month = datetime.datetime.now().month
    gender = 0
    itemNum =  getThreand.getCurrentThreand(month,gender)
    print(month,gender)
    print(itemNum)
    currentThreandArray.append(threandingArray[itemNum])

    
@app.route('/')
def load():
    findCurrentThreandArray()
    return render_template('home.html',threandingArray=currentThreandArray)


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


@app.route("/checkout", methods =['POST',"GET"])
def checkout():
    global ItemListArray
    global totalBill
    totalBill = 0
    ItemListArray =[]
    data=ItemListArray
    return render_template("home.html",headings=headings,data=data,totalBill=totalBill)

def flask_thread():
    app.run()

if __name__ == '__main__':
    t = Thread(target=app.run, kwargs={'port': 5001})
    t.start()
    # client.backgroudNetworkProcess()
