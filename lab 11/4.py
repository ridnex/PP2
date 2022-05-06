import psycopg2

conn = psycopg2.connect(
	database="phone",
	user='phone_user',
	password='Esko28:)',
	host='localhost',
	port='5432'
)

'''my SQL in DATAGRIP:
select *  from phonebook_lab11 limit 1 offset 2;

create or replace function getAllPhone(lim integer, ofs integer )
    returns setof phonebook_lab11
as
$$
begin
    return query
        select * from phonebook_lab11 limit $1 offset $2;
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
