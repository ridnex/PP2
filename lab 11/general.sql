-------------------1-----------------
create or replace function getStudentNameSurnamePhone(name varchar)
    returns setof phonebook
as
$$
begin
    return query
        select *  from phonebook
        where (phonebook.first_name = $1) or (phonebook.last_name = $1);



end
$$ language plpgsql;

select *
from getStudentNameSurnamePhone('Kil');



------------------------2------------

create or replace procedure addPhone(first_name varchar, last_name varchar, phone_number numeric)
as
$$
begin
    update phonebook
    set phone_num = $3
    where (phonebook.first_name = $1) and (phonebook.last_name = $2);
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
    from phonebook as p
    where (p.first_name = $1) and(p.last_name = $2);
end;
$$
    LANGUAGE plpgsql;

call deleteName('ridnex', 'krak');


---------------------------------5(2)-------------------
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

call deleteNum(29);