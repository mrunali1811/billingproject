create database billingpy;
use billingpy;
create table customers(Bill_no varchar(500) primary key ,Customer_name varchar(500),phone_no varchar(500),
laptop_price double,phone_price double,led_price double ,laptop_tax varchar(500),phone_tax varchar(500),
led_tax varchar(500), Total_Bill double);
select * from customers;

-- Indiviual product table agar banana hai to isme maine sirf laptop ka banaya hai ap phone or led ka bana sakte hai
create table Laptop(Bill_no varchar(500) primary key,Customer_Name varchar(500),Phone_no varchar(500),Hp double,Dell double,
lenovo double,Asus double,Apple double,Acer double,laptop_Price double,laptop_tax varchar(500),Total_Bill double);
select * from Laptop;

create table Phones(Bill_no varchar(500) primary key,Customer_Name varchar(500),Phone_no varchar(500),Appleiphone double,samsung double,
Oneplus double,Realme double,Oppo double,Vivo double,phone_Price double,phone_tax varchar(500),Total_Bill double);
select * from Phones;

create table LEDs(Bill_no varchar(500) primary key,Customer_Name varchar(500),Phone_no varchar(500),sony double,samsungled double,
chroma double,Xiaomi double,Toshiba double,Panasonic double,LED_Price double,LED_tax varchar(500),Total_Bill double);
select * from LEDs;
