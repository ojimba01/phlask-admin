from flask import Flask, render_template, request, redirect
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from admin_classes import prod_admin as prod, beta_admin as beta, test_admin as test

# initialize the prod_admin class
water_prod=prod().water_db_live
food_prod=prod().food_db_live
bathroom_prod=prod().bathroom_db_live
forage_prod=prod().forage_db_live
# initialize the beta_admin class
water_beta=beta().water_db_live
food_beta=beta().food_db_live
bathroom_beta=beta().bathroom_db_live
forage_beta=beta().forage_db_live
# initialize the test_admin class
water_test=test().water_db_live
food_test=test().food_db_live
bathroom_test=test().bathroom_db_live
forage_test=test().forage_db_live

def db_iterator(db, range):
    for i in range:
        prod.get_taps(db, i)


dashboard = Flask(__name__)

def connectDB():
    cred = credentials.Certificate("/Users/olayinkajimba/Desktop/CodeForPhilly/PHLASK/phlask-admin/dashboard/phlask.json")
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://phlask-web-map-prod-water-live.firebaseio.com/" #Your database URL
    })
    return water_prod
	

@dashboard.route("/")
def main():
    try:
    
        water_prod_1=prod.get_tap(water_prod, 1)
        water_prod_2=prod.get_tap(water_prod, 2)
        water_prod_3=prod.get_tap(water_prod, 3)
        water_prod_4=prod.get_tap(water_prod, 4)
        taps = [water_prod_1, water_prod_2, water_prod_3, water_prod_4]
    

        return render_template("taplist.html", taps=taps)
        
    except:

        pass

@dashboard.route("/addtap", methods = ['GET','POST'])
def addtapp():
    tapcount = prod.get_count(water_prod)
    if request.method == 'GET':
        return render_template("addtap.html", tap = {})
    if request.method == 'POST':
        access = str(request.form["access"])
        address = str(request.form["address"])
        city = str(request.form["city"])
        description = str(request.form["description"])
        filteration = str(request.form["filteration"])
        gp_id = str(request.form["gp_id"])
        handicap = str(request.form["handicap"])
        # hours = str(request.form["hours"])
        latitude = int(request.form["lat"])
        longitude = int(request.form["lon"])
        norms = str(request.form["norms"])
        organization = str(request.form["organization"])
        permanently_closed = str(request.form["permanently_closed"])
        phone = str(request.form["phone"])
        quality = str(request.form["quality"])
        service= str(request.form["service"])
        statement = str(request.form["statement"])
        status = str(request.form["status"])
        tap_type = str(request.form["tap_type"])
        tapnum = int(request.form["tapnum"])
        vessel = str(request.form["vessel"])
        zip_code = str(request.form["zip_code"])

        water_prod.update({tapcount: { "access": access, "address": address, "city": city, "description": description, "filteration": filteration, "gp_id":gp_id,"handicap":handicap , "latitude": latitude, "longitude": longitude, "norms": norms, "organization": organization, "permanently_closed": permanently_closed, "phone": phone, "quality": quality, "service": service, "statement": statement, "status": status, "tap_type": tap_type, "tapnum": tapnum, "vessel": vessel, "zip_code": zip_code } } )
        return redirect('/')

# @dashboard.route('/updatecar/<int:id>',methods = ['GET','POST'])
# def updatecar(id):
#     cr = []
#     tblCars = dbconn.get()

#     if request.method == 'GET':
#         for key, value in tblCars.items():
#             if(value["ID"] == id):
#                 global updatekey
#                 updatekey = key
#                 cr.append({"id": value["ID"], "name": value["Name"], "year": value["Year"], "price": value["Price"]})
#         return render_template("addcar.html", car = cr[0])
#     if request.method == 'POST':
#         name = str(request.form["name"])
#         year = int(request.form["year"])
#         price = float(request.form["price"])
#         updateitem = dbconn.child(updatekey)
#         updateitem.update( { "ID": id, "Name": name, "Year": year, "Price": price } )
#         return redirect('/')

@dashboard.route('/deletetap/<int:tapnum>')
def deletetap(tapnum):
    prod.delete_tap(water_prod, str(tapnum))
    return redirect('/') 

if(__name__ == "__main__"):
    dbconn = connectDB()
    dashboard.run()