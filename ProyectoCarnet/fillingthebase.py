import sqlite3
import datetime
import random as rd

db_name = 'db.sqlite3' 


def run_query(query, parameters=(), database=db_name):
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters)
        conn.commit()

    return result

fields = [
    'password',
    'username',
    'first_name',
    'last_name',
    'email',
    'is_staff',
    'dni',
    'nacimiento',
    'is_superuser',
    'is_active',
    'date_joined',
    'phone',
]

#-----------------> UN REGISTRO EJEMPLO <----------------
""" 
parameters = (
    '123456789',
    'danielito1',
    'daniel',
    'benitez',
    'daniel@benitez.com',
    0,
    123456789,
    random_date(),        
    1,
    0,
    0,
    datetime.datetime.now(),
)
 """

#<-------------------------------------------------------->

#--------------RANDOM DATES-----------------
def random_date():
    start_date = datetime.date(1940, 1, 1)
    end_date = datetime.date(2002, 2, 1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = rd.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

#----------------------------------------------------



first_names = [
    'Maria',
    'Ramon',
    'Ezequiel',
    'Lucas',
    'Gabriel',
    'Martin',
    'Jose',
    'Pedro',
    'Estefania',
    'Soledad',
    'Ivan',
    'Mateo',
    'Tomas',
    'Daniel',
    'Vanina',
    'Rolando',
    'Carlos',
    'Agustin',
    'Simon',
    'Pablo',
    'Julieta',

]

last_names = [
    'Ibalo',
    'Carabajal',
    'Andino',
    'Benitez',
    'Baez',
    'Martinez',
    'Chuconuk',
    'Gonzalez',
    'Campestrini',
    'Parera',
    'Perez',
    'Cuneo',
    'Comechingon',
    'Venegas',
    'Parra',
]

N = 10                              #Record number
records = list()                    #Record Collection
str_fields = ', '.join(fields)
n_fields = ', '.join(['?' for _ in fields])
table = 'user_usuario'
add_query = 'INSERT INTO %s (%s) VALUES (%s)' % (table, str_fields, n_fields)

for _ in range(N):
    name = rd.choice(first_names)
    l_name = rd.choice(last_names)

    parameters = [    
        '123456789',                                     #password
        f'{name}_{l_name}{rd.randint(1,100)}',           #username
        name,                                            #first name
        l_name,                                          #last_name
        f'{name}_{rd.randint(1,100)}@{l_name}.com',      #email
        0,                                               #is staff
        rd.randint(10000000, 45000000),                  #dni
        random_date(),                                   #born_date
        1,                                               #is_active
        0,                                               #is_superuser 
        datetime.datetime.now(),                         #date_joined
        rd.randint(1111111, 9999999),                    #phone_number
    ]
    run_query(add_query, parameters)


