from ast import Num
import psycopg2

conn = psycopg2.connect(
	database="phone",
	user='phone_user',
	password='Esko28:)',
	host='localhost',
	port='5432'
)

''' my SQL in DATAGRIP:
1) BY NAME
create or replace procedure deleteName(first_name varchar, last_name varchar)
as
$$
begin
    delete
    from phonebook as p
    where (p.first_name = $1) and(p.last_name = $2);
end;
$$
    LANGUAGE plpgsql;
2)BY NUM
create or replace procedure deleteNum(num integer)
as
$$
begin
    delete
    from phonebook as p
    where (p.phone_num = $1) ;
end;
$$
    LANGUAGE plpgsql;
'''


cursor = conn.cursor()
conn.autocommit = True

first_name = str(input("Delete by First_name: "))
last_name = str(input("Delete by Last_name: "))

cursor.execute('CALL deleteName(%s,%s)', (first_name, last_name))

cursor.callproc('getStudentNameSurnamePhone', [first_name])
result = cursor.fetchall()
print(result)



num=int(input("Num: "))
cursor.execute(f'CALL deleteNum({num})')

sql = f"select * from phonebook";
cursor.execute(sql)
info = cursor.fetchall()
print(info)

