import requests
import psycopg2
from collections import namedtuple
# from database_data import database_cann
from pprint import pprint


url='https://dummyjson.com/users/'
respons=requests.get(url)
# pprint(respons.json())
# print(respons.json()['users'])
# for user in respons.json()['users']:
#     print(user)


db_name = 'shoping'
password ='5760'
host = 'localhost'
port = 5432
user = 'postgres'
conn = psycopg2.connect(dbname=db_name,
                            password=password,
                            host=host,
                            port=port,
                            user=user)
cur=conn.cursor()
create_table_query="""CREATE TABLE IF NOT EXISTS users(
                    id serial primary key,
                    first_name varchar(50),
                    last_name varchar(50),
                    age int,
                    gender varchar(50),
                    email varchar(50),
                    phone varchar(20),
                    username varchar(50),
                    password varchar(50),
                    birthdate date,
                    image varchar(250),
                    city varchar(50))"""
# cur.execute(create_table_query)
# conn.commit()
insert_into_query="""INSERT INTO users(first_name,last_name,age,gender,email,phone,username,password,birthdate,image)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
for user in respons.json()['users']:
    cur.execute(insert_into_query,(user['firstName'],user['lastName'],user['age'],user['gender'],user['email'],user['phone'],user['username'],
                user['password'],user['birthDate'],user['image']))
    conn.commit()


Product=namedtuple('Product','name price quantity', defaults=['nane',0,0])
phone1=Product('iphone',1200,177)
phone2=Product()
# print(phone1)
# print(phone2)

data={
    'name':'samsung',
    'price':800,
    'quantity':213
}
phone3=Product._make(data)
print(type(phone3))
select_query="""select first_name,last_name,username,age from users where id=1"""
User=namedtuple('User',['firstName','lastName','username','age'])
user1=User._make(cur.execute(select_query))
print(user1)
                                        ##Ustoz shuna qilib bazadan malumot olib namedtuple yaratsa bo`ladimi,
                                        ###  menda o`xshamadida
                                        ## Ustoz yana database ni malumotlarini bir fayilga saqlab shu fayldan
                                        ##  import qilibb  olsak boladimi shuni biron misol bilin tushuntirib berolaasmi
                                        ## misol       database_data=db_name = 'shoping'
                                               #                                 password ='5760'
                                                 #                               host = 'localhost'
                                                 #                               port = 5432
                                                   #                             user = 'postgres'
#
#
#
#                                                      # >> pastagi variantni o`rniga  conn =psycopg2.connect(database_data)
                                                       #     shakilda bersak  berib ko`rdim o`hshamadi boshqa yo`li bormi?
#                                                      conn =psycopg2.connect(dbname=db_name,
                                                                            # password=password,
                                                                            # host=host,
                                                                            # port=port,
                                                                            # user=user)