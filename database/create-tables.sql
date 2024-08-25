create table donorDemographic (donorName varchar(20), pincode varchar(6),phonenumber varchar(10) );
ALTER TABLE donorDemographic ADD CONSTRAINT UC_donorDemographic UNIQUE (phonenumber);