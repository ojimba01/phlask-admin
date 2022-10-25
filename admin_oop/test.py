# Import all the modules
from admin_classes import prod_admin as prod
# from admin_classes import beta_admin as beta
# from admin_classes import test_admin as test

# initialize the prod_admin class
water=prod()
food=prod()

# initialize the prod water db reference
water_db=water.water_db_live
food_db=food.food_db_live

#Example calls for the classes
print(prod.get_db(water_db))
print("----------------------------------------------")
print("Checking if water_db and food_db contain the same data: "), prod.db_comparison(water_db,food_db), print("----------------------------------------------")

#    print("-----------------")