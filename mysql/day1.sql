CREATE TABLE class (
	cid INT auto_increment PRIMARY KEY,# 自增主键
	caption VARCHAR(20)
) ENGINE = INNODB DEFAULT CHARSET utf8;# 支持原子性操作，默认编码为UTF8

CREATE TABLE student(
	sid INT auto_increment PRIMARY KEY,
	sname varchar(20),
	gender enum('男', '女'),# 枚举值
	class_id int,
	constraint fk_sid_cid FOREIGN KEY(class_id) REFERENCES class(cid)# 单个外键
)ENGINE = INNODB DEFAULT CHARSET utf8;

CREATE TABLE teacher(
	tid int auto_increment PRIMARY KEY,
	tname VARCHAR(10)
)ENGINE = INNODB DEFAULT CHARSET utf8;

create table course(
	cid INT auto_increment PRIMARY KEY,
	cname varchar(20),
	teacher_id INT,
	CONSTRAINT fk_tid_course_id FOREIGN KEY (teacher_id) REFERENCES teacher(tid)# 外键约束
)ENGINE = INNODB DEFAULT CHARSET utf8;

CREATE TABLE score(
	sid int auto_increment PRIMARY KEY,
	student_id INT,
	course_id INT,
	num INT,
	CONSTRAINT fk_sid_ss_id FOREIGN KEY (student_id) REFERENCES student(sid),
	CONSTRAINT fk_sid_sc_id FOREIGN KEY (course_id) REFERENCES course(cid)
)ENGINE = INNODB DEFAULT CHARSET utf8;

show tables;
insert into class(caption) values ('一班');
insert into student(sname,gender,class_id) values ('陆远','男',1)

SELECT s.sname,c.caption from student s,class c where c.cid = s.class_id;

create table t1(
	id  int auto_increment ,
	na varchar(20) not null,
	age int,
  PRIMARY KEY (id,na)# 组合主键
) ENGINE = innodb default CHARSET utf8;

create table t2(
	id  int auto_increment PRIMARY key,
	num int,
	na varchar(20),
	CONSTRAINT fk_id FOREIGN KEY (num,na) REFERENCES t1(id,na)# 组合外键
) ENGINE = innodb default CHARSET utf8;
show SESSION VARIABLES;# 当前会话变量
show GLOBAL VARIABLES;# 全局变量
set session auto_increment_increment=2;# 设置会话自增步长
create table test(
	id int not null auto_increment primary key,
	num int,
	age int,
	UNIQUE uq1(num,age)# 组合索引
  # UNIQUE (age) #单个索引
)ENGINE=INNODB DEFAULT CHARSET=utf8;