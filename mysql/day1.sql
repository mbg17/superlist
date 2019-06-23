CREATE TABLE class (
	cid INT auto_increment PRIMARY KEY,
	caption VARCHAR(20)
) ENGINE = INNODB DEFAULT CHARSET utf8;

CREATE TABLE student(
	sid INT auto_increment PRIMARY KEY,
	sname varchar(20),
	gender enum('男', '女'),
	class_id int,
	constraint fk_sid_cid FOREIGN KEY(class_id) REFERENCES class(cid)
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