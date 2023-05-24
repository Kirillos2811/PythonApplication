pet_name = input("name = ")
owner_name = input("owner_name = ")
age = int(input("age = "))
species = input("species = ")

pet_data = {}
pet_data[pet_name] = {}
pet_data[pet_name]["age"] = age
pet_data[pet_name]["owner_name"] = owner_name
pet_data[pet_name]["species"] = species

for pet_name in pet_data.keys():
    if pet_data[pet_name]["age"] % 10 == 1:
        prefix = "год"
    elif pet_data[pet_name]["age"] % 10 < 5:
        prefix = "года"
    else:
        prefix = "лет"
    print(f'''Это {pet_data[pet_name]['species']} по кличке "{pet_name}".'''
            + f'''Возраст питомца: {pet_data[pet_name]['age']} {prefix}. Имя владельца: {pet_data[pet_name]['owner_name']}''')