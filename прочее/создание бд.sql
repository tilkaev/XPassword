

use XPassword

create table ������(
�������� int identity(1,1) primary key,
������������ varchar(50) not null
)

create table ���������(
������ int identity(1,1) primary key,
������������ varchar(10) not null
)

create table ���������(
������� int identity(1,1) primary key,
������������ varchar(10) not null
)


create table ������(
�������� int identity(1,1) primary key,
������ int  not null,
������� int  not null,
���������� varchar(100) not null, 
foreign key(�������) references ���������(�������),
foreign key(������) references ���������(������)
)



