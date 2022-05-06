import psycopg2

conn = psycopg2.connect(
	database="phone",
	user='phone_user',
	password='Esko28:)',
	host='localhost',
	port='5432'
)
cursor = conn.cursor()
conn.autocommit = True

arr = [["cds", "GAMBIY", "87073700000"], ["ndsvsdvsvj", "cvsdvssdcy", "78978978"]]
for i in arr:
    postgres_insert_query = """ INSERT INTO  example(first_name, last_name, phone_num) VALUES (%s,%s,%s)"""
    record_to_insert = (i[0], i[1], i[2])
    cursor.execute(postgres_insert_query, record_to_insert)



'''My sql :
CREATE TABLE example(
   first_name VARCHAR(255) NOT NULL,
   last_name VARCHAR(255),
   phone_num VARCHAR(255));


CREATE Or REPLACE FUNCTION correct_phone()
returns setof example
as
$$
    declare r example%rowtype;
    Begin
        FOR r in
            SELECT * FROM example
        Loop
            IF not (r.phone_num  LIKE '87_________')THEN
                return next r;
                DELETE FROM example where (example.first_name = r.first_name);
            ELSE
                INSERT into phonebook_lab11(first_name, last_name, phone_num) VALUES (r.first_name, r.last_name, r.phone_num);
            end if;
        end loop;

        FOR r in
            SELECT * FROM example
        Loop
             DELETE FROM example where (example.first_name = r.first_name);
        end loop;
    end
$$language plpgsql;


select *
from correct_phone();
'''

cursor.callproc('correct_phone',)
result = cursor.fetchall()
print(result)
