create database committiee;

use committiee;
create table Ternant(
	Id int primary key,
    Username nvarchar(20),
    Password nvarchar(20),
    FirstName nvarchar(20) not null,
    LastName nvarchar(20) not null,
    ApartmentId int,
    Payment decimal,
    MonthPay nvarchar(30)
);

select * from Manager;

insert into Ternant(Id,Username, Password,FirstName,LastName,ApartmentId,Payment,MonthPay)
values(1,'A','1234','Shadi','Levi',41,1200,'1 2 3 8'),
	  (2,'B','12','Bdair','Israel',1,4000,'1 2 3 4 5 6 7 8 9 10 11 12'),
      (3,'C','345','Ronaldo','Cohen',23,7000,'1 5 9');
      
create table Manager(
	Id int primary key,
    Username nvarchar(20),
    Password nvarchar(20),
    FirstName nvarchar(20) not null,
    LastName nvarchar(20) not null,
    Years int
);

insert into Manager(Id,Username, Password,FirstName,LastName,Years)
values(1,'D','1234','Ronaldinho','Malka',4),
	  (2,'E','12','Chris','Brown',2),
      (3,'F','345','Li','xavi',3)
      
