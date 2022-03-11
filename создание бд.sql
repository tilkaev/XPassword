

use XPassword

create table группы(
идгруппы int identity(1,1) primary key,
наименование varchar(50) not null
)

create table типыполей(
идполя int identity(1,1) primary key,
наименование varchar(10) not null
)

create table картотека(
идкарты int identity(1,1) primary key,
наименование varchar(10) not null
)


create table запись(
идзаписи int identity(1,1) primary key,
идполя int  not null,
идкарты int  not null,
содержание varchar(100) not null, 
foreign key(идкарты) references картотека(идкарты),
foreign key(идполя) references типыполей(идполя)
)



