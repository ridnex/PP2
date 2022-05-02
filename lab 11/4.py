import psycopg2

conn = psycopg2.connect(
	database="phone",
	user='phone_user',
	password='Esko28:)',
	host='localhost',
	port='5432'
)

'''my SQL in DATAGRIP:
create or replace function getAllPhone(lim integer, ofs integer )
    returns setof phonebook
as
$$
begin
    return query
        select * from phonebook limit $1 offset $2;
end;
$$ language plpgsql;

select *
from getAllPhone(1,2);
'''

cursor = conn.cursor()
conn.autocommit = True
limit = int(input("Limit: "))
offset = int(input("Offset: "))

cursor.callproc('getAllPhone', (limit, offset))
result = cursor.fetchall()
print(result)
