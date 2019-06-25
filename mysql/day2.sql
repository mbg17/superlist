# 多对多外键
CREATE DATABASE host default charset utf8;
use host;
create table user(
	id int not null auto_increment PRIMARY KEY,
	name varchar(6) not null,
	gender char(2) 
)ENGINE= INNODB DEFAULT charset = utf8;

create table host(
	id int not null auto_increment PRIMARY KEY,
	name char(2) 
)ENGINE=INNODB DEFAULT charset = utf8;

create table user_host_id(
	id int not null auto_increment PRIMARY KEY,
	user_id int not null,
	host_id int not null,
	CONSTRAINT u_u FOREIGN key (user_id) REFERENCES user(id),
	CONSTRAINT h_h FOREIGN key (host_id) REFERENCES host(id),
	UNIQUE uq2 (user_id,host_id)
)ENGINE=INNODB DEFAULT charset = utf8;

# 一对一外键
CREATE DATABASE user default charset utf8;
use user;
CREATE table userinfo(
	id int not null auto_increment PRIMARY KEY,
	username varchar(20) not null,
	usertype int 
)ENGINE=INNODB DEFAULT charset = utf8;

CREATE TABLE admin(
	id int not null auto_increment PRIMARY KEY,
	userid int not null,
	password VARCHAR(20) not null,
	CONSTRAINT fk_a_u FOREIGN KEY (userid) REFERENCES userinfo(id),
	UNIQUE uq1 (userid)
)ENGINE=INNODB DEFAULT charset = utf8;