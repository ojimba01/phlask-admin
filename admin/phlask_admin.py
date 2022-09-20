from gc import get_count
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebaseadmin_module import get_db, get_changed_data, db_dry_count, db_comparison, update_changed_db_iter, update_changed_db, update_db, update_db_iter
from firebaseadmin_module import ListenerClass as ls

#----------------------------------------------------------------------------------------------------------------------
# DONT ALTER CONFIG CODE BELOW #
#----------------------------------------------------------------------------------------------------------------------
# Prod database URL's
pointer_url = "https://phlask-web-map-food-hours.firebaseio.com/"
prod_water_url_live = "https://phlask-web-map-prod-water-live.firebaseio.com/"
prod_water_url_verify = "https://phlask-web-map-prod-water-verify.firebaseio.com/"
prod_food_url_live = 'https://phlask-web-map-prod-food-live.firebaseio.com/'
prod_food_url_verify = 'https://phlask-web-map-food-hours.firebaseio.com/'
prod_forage_url_live = "https://phlask-web-map-prod-foraging-live.firebaseio.com/"
prod_forage_url_verify = 'https://phlask-web-map-prod-foraging-verify.firebaseio.com/'
prod_bathroom_url_live = "https://phlask-web-map-prod-bathroom-live.firebaseio.com/"
prod_bathroom_url_verify = "https://phlask-web-map-prod-bathroom-verify.firebaseio.com/"
#----------------------------------------------------------------------------------------------------------------------
# Beta database URL's 
beta_water_url_live = "https://phlask-web-map-beta-water-live.firebaseio.com/"
beta_water_url_verify = "https://phlask-web-map-beta-water-verify.firebaseio.com/"
beta_food_url_live = 'https://phlask-web-map-beta-food-live.firebaseio.com/'
beta_food_url_verify = 'https://phlask-web-map-beta-food-verify.firebaseio.com/'
beta_forage_url_live = "https://phlask-web-map-beta-foraging-live.firebaseio.com/"
beta_forage_url_verify = "https://phlask-web-map-beta-foraging-verify.firebaseio.com/"
beta_bathroom_url_live = "https://phlask-web-map-beta-bathroom-live.firebaseio.com/"
beta_bathroom_url_verify = "https://phlask-web-map-beta-bathroom-verify.firebaseio.com/"
#----------------------------------------------------------------------------------------------------------------------
# Test database URL's
test_water_url_live = "https://phlask-web-map-test-water-live.firebaseio.com/"
test_water_url_verify = "https://phlask-web-map-test-water-verify.firebaseio.com/"
test_food_url_live = 'https://phlask-web-map-test-food-live.firebaseio.com/'
test_food_url_verify = 'https://phlask-web-map-test-food-verify.firebaseio.com/'
test_forage_url_live = "https://phlask-web-map-test-foraging-live.firebaseio.com/"
test_forage_url_verify = "https://phlask-web-map-test-foraging-verify.firebaseio.com/"
test_bathroom_url_live = "https://phlask-web-map-test-bathroom-live.firebaseio.com/"
test_bathroom_url_verify = "https://phlask-web-map-test-bathroom-verify.firebaseio.com/"
#----------------------------------------------------------------------------------------------------------------------
#creds for initializing firebase admin
cred = credentials.Certificate(r'C:\Users\Loaner\Desktop\cfp\phlask-admin\admin\phlask.json')
#----------------------------------------------------------------------------------------------------------------------
# initialize firebase admin Prod DB's
pointer_init =  firebase_admin.initialize_app(cred, { 'databaseURL': pointer_url}, name="pointer_app")
prod_water_live=firebase_admin.initialize_app(cred, { 'databaseURL': prod_water_url_live }, name="prod_water_live") #name is the app name
prod_food_live=firebase_admin.initialize_app(cred, { 'databaseURL': prod_food_url_live }, name="prod_food_live") #name is the app name
prod_forage_live=firebase_admin.initialize_app(cred, { 'databaseURL': prod_forage_url_live }, name="prod_forage_live") #name is the app name
prod_bathroom_live=firebase_admin.initialize_app(cred, { 'databaseURL': prod_bathroom_url_live }, name="prod_bathroom_live") #name is the app name
#----------------------------------------------------------------------------------------------------------------------
# initialize firebase admin Beta DB's
beta_water_live=firebase_admin.initialize_app(cred, { 'databaseURL': beta_water_url_live }, name="beta_water_live") #name is the app name
beta_food_live=firebase_admin.initialize_app(cred, { 'databaseURL': beta_food_url_live }, name="beta_food_live") #name is the app name
beta_forage_live=firebase_admin.initialize_app(cred, { 'databaseURL': beta_forage_url_live }, name="beta_forage_live") #name is the app name
beta_bathroom_live=firebase_admin.initialize_app(cred, { 'databaseURL': beta_bathroom_url_live }, name="beta_bathroom_live") #name is the app name
#----------------------------------------------------------------------------------------------------------------------
# initialize firebase admin Test DB's
test_water_live=firebase_admin.initialize_app(cred, { 'databaseURL': test_water_url_live }, name="test_water_live") #name is the app name
test_food_live=firebase_admin.initialize_app(cred, { 'databaseURL': test_food_url_live }, name="test_food_live") #name is the app name
test_forage_live=firebase_admin.initialize_app(cred, { 'databaseURL': test_forage_url_live }, name="test_forage_live") #name is the app name
test_bathroom_live=firebase_admin.initialize_app(cred, { 'databaseURL': test_bathroom_url_live }, name="test_bathroom_live") #name is the app name
#----------------------------------------------------------------------------------------------------------------------
# Database References for all of the prod databases
prod_water_db_live = db.reference('/', app= prod_water_live)
prod_food_db_live = db.reference('/', app= prod_food_live)
prod_forage_db_live = db.reference('/', app= prod_forage_live)
prod_bathroom_db_live = db.reference('/', app= prod_bathroom_live)
#----------------------------------------------------------------------------------------------------------------------
# Database References for all of the beta databases
beta_water_db_live = db.reference('/', app= beta_water_live)
beta_food_db_live = db.reference('/', app= beta_food_live)
beta_forage_db_live = db.reference('/', app= beta_forage_live)
beta_bathroom_db_live = db.reference('/', app= beta_bathroom_live)
#----------------------------------------------------------------------------------------------------------------------
# Database References for all of the test databases
test_water_db_live = db.reference('/', app= test_water_live)
test_food_db_live = db.reference('/', app= test_food_live)
test_forage_db_live = db.reference('/', app= test_forage_live)
test_bathroom_db_live = db.reference('/', app= test_bathroom_live)
#----------------------------------------------------------------------------------------------------------------------
# DONT ALTER CONFIG CODE ABOVE #
#----------------------------------------------------------------------------------------------------------------------

# Active Code for AWS Lambda function
def update_beta_db():
    update_db(beta_water_db_live, prod_water_db_live)
    update_db(beta_food_db_live, prod_food_db_live)
    update_db(beta_forage_db_live, prod_forage_db_live)
    update_db(beta_bathroom_db_live, prod_bathroom_db_live)

def update_test_db():
    update_db(test_water_db_live, prod_water_db_live)
    update_db(test_food_db_live, prod_food_db_live)
    update_db(test_forage_db_live, prod_forage_db_live)
    update_db(test_bathroom_db_live, prod_bathroom_db_live)

def full_update():
    update_beta_db()
    update_test_db()

#Test code
#print(get_db(prod_bathroom_db_live))

#----------------------------------------------------------------------------------------------------------------------
#Structure for targeting specific phlask DB's 
# Ex: **[STATE]_[RESOURCE]_[DB]_[LIVE/VERIFY] -> prod_water_db_live or beta_food_db_verify
# ** all characters must be lowercase **
#----------------------------------------------------------------------------------------------------------------------
#For more help refer to the firebaseadmin_module.py file for examples of how to use the functions
