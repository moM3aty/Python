#sort dictionaries

people =[
    {"name":"Momen" ,"job":"Web"},
    {"name":"Mohab" ,"job":"Marketing"},
    {"name":"Be3o" , "job" : "other"}
]

people.sort(key=lambda person:person["job"])

print(people)