create table books(
book_id integer GENERATED ALWAYS as identity primary key,
title varchar(50),
author varchar(50),
quantity int
);

create table users(
user_id integer generated always as identity primary key,
user_name varchar(255),
ddd int,
phone_number varchar(9)
);

create table loan(
user_id integer references users (user_id),
book_id integer references books (book_id)
);



select * from books;