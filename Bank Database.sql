create database bank5;
use bank5;
drop table users;
create table users(ACCNO integer(5) primary key, NAME varchar(50), PHNO varchar(12), AMOUNT integer(20));
 create table admins(USERNAME varchar(20) primary key, NAME varchar(50), PASS varchar(12));

select * from users;
select * from admins;
insert into admins(USERNAME,NAME,PASS) values('DS','imdr',2022);
insert into users(ACCNO,NAME,PHNO,AMOUNT) values(100,'mahesh',999999999,1000);
