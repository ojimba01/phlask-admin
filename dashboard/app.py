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
        "databaseURL": "https://phlask-pyrebase-default-rtdb.firebaseio.com/" #Your database URL
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
        # for db in water_prod_list:
        #     taps=[]
        #     for key, value in db.items():
        #         if key == "access":
        #             taps.append(value)
        #         if key == "address":
        #             taps.append(value)
        #         if key == "city":
        #             taps.append(value)
        #         if key == "description":
        #             taps.append(value)
    

        return render_template("taplist.html", taps=taps)


        # bucket=(water_prod_db["access"], water_prod_db["address"], water_prod_db["city"], water_prod_db["description"])
        # taps.append(bucket)
        
    except:
        return render_template("taplist.html", taps = taps)
        


# @dashboard.route("/addcar", methods = ['GET','POST'])
# def addcar():
#     if request.method == 'GET':
#         return render_template("addcar.html", car = {})
#     if request.method == 'POST':
#         access = int(request.form["access"])
#         city = request.form["city"]
#         address = int(request.form["year"])
#         description = float(request.form["price"])
#         dbconn.push( { "Access": access, "Address": address, "City": city, "Description": description })
#         return redirect('/')

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

# @dashboard.route('/deletecar/<int:id>')
# def deletecar(id):
#     tblCars = dbconn.get()
#     for key, value in tblCars.items():
#         if(value["ID"] == id):
#             deletekey = key
#             break
#     delitem = dbconn.child(deletekey)
#     delitem.delete()
#     return redirect('/')

if(__name__ == "__main__"):
    dbconn = connectDB()
    dashboard.run()