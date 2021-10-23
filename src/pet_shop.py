# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop_name):
    return pet_shop_name["name"]

def get_total_cash(pet_shop_name):
    return pet_shop_name["admin"]["total_cash"]
    
def add_or_remove_cash(pet_shop_name, amount):
    pet_shop_name["admin"]["total_cash"] += amount
    
def get_pets_sold(pet_shop_name):
    return pet_shop_name["admin"]["pets_sold"]
    
def increase_pets_sold(pet_shop_name, num_sold):
    pet_shop_name["admin"]["pets_sold"] += num_sold

def get_stock_count(pet_shop_name):
    return len(pet_shop_name["pets"])

def get_pets_by_breed(pet_shop_name, breed):
    pets_found = []
    for pet in pet_shop_name["pets"]:
        if pet["breed"] == breed:
            pets_found.append(pet)
    return pets_found

def get_pets_by_breed(pet_shop_name, breed):
    pets_not_found = []
    for pet in pet_shop_name["pets"]:
        if pet["breed"] == breed:
            pets_not_found.append(pet)
    return pets_not_found

def find_pet_by_name(pet_shop_name, pet_name):
    for pet in pet_shop_name["pets"]:
        if pet["name"] == pet_name:
            return pet
    
def remove_pet_by_name(pet_shop_name, pet_name):
    delete_pet = find_pet_by_name(pet_shop_name, pet_name)
    pet_shop_name["pets"].remove(delete_pet)

def add_pet_to_stock(pet_shop_name, new_pet):
    pet_shop_name["pets"].append(new_pet)

def get_customer_cash(pet_shop_name):
    return pet_shop_name["cash"]

def remove_customer_cash(customer_name, amount):
    customer_name["cash"] -= amount 
    
def get_customer_pet_count(pet_shop_name):
    return len(pet_shop_name['pets'])

def add_pet_to_customer(customer_name, pet):
    customer_name['pets'].append(pet)
