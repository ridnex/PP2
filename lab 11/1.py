import psycopg2

conn = psycopg2.connect(
	database="phone",
	user='phone_user',
	password='Esko28:)',
	host='localhost',
	port='5432'
)
''' my SQL in DATAGRIP:
create or replace function getStudentNameSurnamePhone(name varchar)
    returns setof phonebook
as
$$
begin
    return query
        select *  from phonebook
        where (phonebook.first_name = $1) or (phonebook.last_name = $1);
end
$$ language plpgsql;'''


cursor = conn.cursor()
conn.autocommit = True

name = str(input("name: "))
cursor.callproc('getStudentNameSurnamePhone', [name])
result = cursor.fetchall()
print(result)