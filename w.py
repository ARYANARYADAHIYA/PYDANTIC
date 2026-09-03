from pydantic import validate_call

def create_usser(first name : str , last_name: str, age : int) -> dict;
email=f'{first_name.lower()}_{last_name.lower()}@example.com"


return{
    "first_name": first_name,
    "last_name": last_name,
    "email": email,
    "age": age

}

def insert_data(name, age):

print(name)
print(age)
print("inserted into database")

insert_data('aryan','thirty')

