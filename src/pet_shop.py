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
    found_pets = []
    for pet in pet_shop_name["pets"]:
        if pet["breed"] == breed:
            found_pets.append(pet)
    return found_pets



