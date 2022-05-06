CREATE TABLE phonebook_lab11(
   first_name VARCHAR(255) NOT NULL,
   last_name VARCHAR(255),
   phone_num VARCHAR(255));

-------------------1-----------------
create or replace function getStudentNameSurnamePhone(name varchar)
    returns setof phonebook_lab11
as
$$
begin
    return query
        select *  from phonebook_lab11
        where (phonebook_lab11.first_name = $1) or (phonebook_lab11.last_name = $1);



end
$$ language plpgsql;

select *
from getStudentNameSurnamePhone('GAMBIY');



------------------------2------------

create or replace procedure addPhone(first_name varchar, last_name varchar, phone_number varchar)
as
$$
begin
    update phonebook_lab11
    set phone_num = $3
    where (phonebook_lab11.first_name = $1) and (phonebook_lab11.last_name = $2);
    IF NOT FOUND THEN
        insert into phonebook(first_name,last_name,phone_num) values ($1, $2, $3);
    END IF;
end;
$$
    LANGUAGE plpgsql;


call addPhone('Ans', 'th', 29);


------------------------5(1)-------------
create or replace procedure deleteName(first_name varchar, last_name varchar)
as
$$
begin
    delete
    from phonebook_lab11 as p
    where (p.first_name = $1) and(p.last_name = $2);
end;
$$
    LANGUAGE plpgsql;

call deleteName('ridnex', 'krak');


---------------------------------5(2)-------------------
create or replace procedure deleteNum(num varchar)
as
$$
begin
    delete
    from phonebook_lab11 as p
    where (p.phone_num = $1) ;
end;
$$
    LANGUAGE plpgsql;

call deleteNum(29);


-----------------------4------------------
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


---------------------3---------------------
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
