--creates a database hbtn_)d_2 and the user user_0d_2
--creates a database
CREATE DATABASE IF NOT EXIST htbn_0d_2;
--Create a user
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd'
--Grants select privileges to a user
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
