import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebaseadmin_module import get_db, get_changed_data, db_dry_count, db_comparison, update_changed_db_iter, update_changed_db, update_db, update_db_iter
from firebaseadmin_module import ListenerClass as ls
#----------------------------------------------------------------------------------------------------------------------
# Prod database URL's
prod_water_url = 'https://phlask-web-map.firebaseio.com/'
prod_forage_url = 'https://phlask-web-map-forage.firebaseio.com/'
prod_bathrooms_url = 'https://phlask-web-map-bathrooms.firebaseio.com/'
prod_food_url = 'https://phlask-web-map-food-hours.firebaseio.com/'
#----------------------------------------------------------------------------------------------------------------------
cred = credentials.Certificate("phlask-web-map-firebase-adminsdk-i2ung-32bde7cd7a.json")
prod_water=firebase_admin.initialize_app(cred, { 'databaseURL': prod_water_url }, name="prod_water") #name is the app name
prod_forage=firebase_admin.initialize_app(cred, { 'databaseURL': prod_forage_url },  name="prod_forage") 
prod_bathrooms=firebase_admin.initialize_app(cred, { 'databaseURL': prod_bathrooms_url },  name="prod_bathrooms")
prod_food=firebase_admin.initialize_app(cred, { 'databaseURL': prod_food_url },  name="prod_food")
#----------------------------------------------------------------------------------------------------------------------
# Database References for all of the prod databases
prod_water_db = db.reference('/', app=prod_water)
prod_forage_db = db.reference('/', app=prod_forage)
prod_bathrooms_db = db.reference('/', app=prod_bathrooms)
prod_food_db = db.reference('/', app=prod_food)
#----------------------------------------------------------------------------------------------------------------------
# Beta database URL's for all of the beta databases (These URL are dummys for now) please replace with actual URLs when ready
beta_water_url = 'https://phlask-web-map-beta.firebaseio.com/'
beta_forage_url = 'https://phlask-web-map-forage-beta.firebaseio.com/'
beta_bathrooms_url = 'https://phlask-web-map-bathrooms-beta.firebaseio.com/'
beta_food_url = 'https://phlask-web-map-food-hours-beta.firebaseio.com/'
#----------------------------------------------------------------------------------------------------------------------
# Database References for all of the beta databases (These Ref's are dummys for now) please replace with actual URLs when ready
beta_water_db = db.reference('/', app=prod_water)
beta_forage_db = db.reference('/', app=prod_forage)
beta_bathrooms_db = db.reference('/', app=prod_bathrooms)
beta_food_db = db.reference('/', app=prod_food)
#----------------------------------------------------------------------------------------------------------------------
# Retrieves the nested data within the prod DBs 
# Returns in the form of dictionaries in a list

print(get_db(prod_water_db))

print(get_changed_data(prod_water_db,prod_bathrooms_url))

# print(prod_forage_db.get())
# print(prod_bathrooms_db.get())
# print(prod_food_db.get())
# print(prod_water_db.get())


# prod_water.reference("/phlask-struct/phlask-web-map").set(False)
# prod_water_db = db.reference("https://phlask-web-map.firebaseio.com/")

# Beta_database = db.reference('phlask-struct/phlask-web-map')
# Test_database = db.reference('phlask-struct/phlask-web-map')

# print(prod_water_db)