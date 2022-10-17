# Import all the modules
from admin_classes import prod_admin as prod
from admin_classes import beta_admin as beta
from admin_classes import test_admin as test

# initialize the prod_admin class
water_prod=prod()
food_prod=prod()
bathroom_prod=prod()
forage_prod=prod()
# initialize the beta_admin class
water_beta=beta()
food_beta=beta()
bathroom_beta=beta()
forage_beta=beta()
# initialize the test_admin class
water_test=test()
food_test=test()
bathroom_test=test()
forage_test=test()

# initialize the prod db reference
water_db_prod=water_prod.water_db_live
food_db_prod=food_prod.food_db_live
bathroom_db_prod=bathroom_prod.bathroom_db_live
forage_db_prod=forage_prod.forage_db_live

# initialize the beta db reference
water_db_beta=water_beta.water_db_live
food_db_beta=food_beta.food_db_live
bathroom_db_beta=bathroom_beta.bathroom_db_live
forage_db_beta=forage_beta.forage_db_live

# initialize the test db reference
water_db_test=water_test.water_db_live
food_db_test=food_test.food_db_live
bathroom_db_test=bathroom_test.bathroom_db_live
forage_db_test=forage_test.forage_db_live


def update_beta():
    prod.update_db(water_db_beta,water_db_prod)
    prod.update_db(food_db_beta,food_db_prod)
    prod.update_db(bathroom_db_beta,bathroom_db_prod)
    prod.update_db(forage_db_beta,forage_db_prod)

def update_test():
    prod.update_db(water_db_test,water_db_prod)
    prod.update_db(food_db_test,food_db_prod)
    prod.update_db(bathroom_db_test,bathroom_db_prod)
    prod.update_db(forage_db_test,forage_db_prod)

def full_update():
    update_beta()
    update_test()

def full_test():
    print(prod.get_db(water_db_prod))

    # print(prod.get_db(food_db_prod))
    # print(prod.get_db(bathroom_db_prod))

# full_test()

example=prod.get_tap(water_db_prod,274)

# for key, value in example.items():
    #return all the values in the dictionary
#iterate through the dictionary for specific values 
#example = {"access": value["Access"], "address": value["Address"], "city": value["City"], "description": value["Description"]}
# taps=[]
# bucket1=example["access"]
# bucket2=example["address"]
# bucket3=example["city"]
# bucket4=example["description"]
# bucket=[bucket1,bucket2,bucket3,bucket4]
# for i in bucket:
#     print(i)
#     taps.append(i)
# bucket.index(bucket1)

# print(taps)
# bigexample=(example["access"], example["address"], example["city"], example["description"])
# taps.append(bigexample)
# print(type(taps))

# for i in taps:
#     print (i)



# for key, value in example.items():
#     print(key, value)
water_prod_1=prod.get_tap(water_db_prod, 1)
water_prod_2=prod.get_tap(water_db_prod, 2)
water_prod_3=prod.get_tap(water_db_prod, 3)
water_prod_4=prod.get_tap(water_db_prod, 4)
water_prod_list = [water_prod_1, water_prod_2, water_prod_3, water_prod_4]
for db in water_prod_list:
    taps=[]
    for key, value in db.items():
        if key == "access":
            taps.append(value)
        if key == "address":
            taps.append(value)
        if key == "city":
            taps.append(value)
        if key == "description":
            taps.append(value)
    print(taps)

# for value in example:
#     taps.append({value["Access"], value["Address"],value["City"], value["Description"]})
#             # taps.append(value)


# #Example calls for the classes
# print(prod.get_db(water_db_prod))
# print("----------------------------------------------")
# print("Checking if water_db and food_db contain the same data: "), prod.db_comparison(water_db,food_db), print("----------------------------------------------")
# #    print("-----------------")