CREATE TABLE score (
  sid int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  student_id int NOT NULL,
  course_id int NOT NULL,
  num int NOT NULL,
  CONSTRAINT fk_sid_ss_id FOREIGN KEY (student_id) REFERENCES student(sid),
  CONSTRAINT fk_sid_sc_id FOREIGN KEY (course_id) REFERENCES course(cid),
	UNIQUE S_C_UQ (student_id,course_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
select * from teacher;
INSERT INTO teacher(tname) values ('叶平'),('李伟'),('李杰'),('陆远');
select * from class ;
INSERT INTO class(caption) values ('四班'),('五班');
select * from course;
INSERT into course(cname,teacher_id) VALUES ('语文',2),('英语',1),('生物',3),('物理',4);
select * from student;
INSERT into student(sname,gender,class_id) VALUES ('张三','男',2),('李四','女',1),('王五','女',3),('哈哈','男',4),('接触','男',5),('筛子','男',5);
select * from class;
insert into score(student_id,course_id,num) VALUES (6,4,50),(3,4,70),(8,4,90),(7,1,60),(5,3,90),(4,2,80);
select * from score;
-- 2、查询“生物”课程比“物理”课程成绩高的所有学生的学号；
select student.sid,score.num from student 
inner JOIN score on student.sid = score.student_id 
inner JOIN course on course.cid = score.course_id 
where 
-- 3、查询平均成绩大于60分的同学的学号和平均成绩； 
select student.sid,avg(score.num) from student 
inner JOIN score on student.sid = score.student_id 
inner JOIN course on course.cid = score.course_id 
GROUP by student.sid HAVING avg(score.num)>60;
-- 4、查询所有同学的学号、姓名、选课数、总成绩；
select student.sid,student.sname,count(course_id) as '选课数',sum(score.num) as '总成绩' from student 
inner JOIN score on student.sid = score.student_id 
inner JOIN course on course.cid = score.course_id 
GROUP BY student.sid;
-- 5、查询姓“李”的老师的个数；
select count(tname) from teacher where tname like '李%';
-- 6、查询没学过“叶平”老师课的同学的学号、姓名；
SELECT student.sid,student.sname from student 
inner JOIN score on student.sid = score.student_id 
inner JOIN course on course.cid = score.course_id 
where course.teacher_id !=1 group BY student.sid ;
-- 7、查询学过“001”并且也学过编号“002”课程的同学的学号、姓名；
-- 
-- 8、查询学过“叶平”老师所教的所有课的同学的学号、姓名；
-- 
-- 9、查询课程编号“002”的成绩比课程编号“001”课程低的所有同学的学号、姓名；
-- 
-- 10、查询有课程成绩小于60分的同学的学号、姓名；
-- 
-- 11、查询没有学全所有课的同学的学号、姓名；
-- 
-- 12、查询至少有一门课与学号为“001”的同学所学相同的同学的学号和姓名；
-- 
-- 13、查询至少学过学号为“001”同学所选课程中任意一门课的其他同学学号和姓名；
-- 
-- 14、查询和“002”号的同学学习的课程完全相同的其他同学学号和姓名；
-- 
-- 15、删除学习“叶平”老师课的SC表记录；
-- 
-- 16、向SC表中插入一些记录，这些记录要求符合以下条件：①没有上过编号“002”课程的同学学号；②插入“002”号课程的平均成绩； 
-- 
-- 17、按平均成绩从低到高显示所有学生的“语文”、“数学”、“英语”三门的课程成绩，按如下形式显示： 学生ID,语文,数学,英语,有效课程数,有效平均分；
-- 
-- 18、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；
-- 
-- 19、按各科平均成绩从低到高和及格率的百分数从高到低顺序；
-- 
-- 20、课程平均分从高到低显示（现实任课老师）；
-- 
-- 21、查询各科成绩前三名的记录:(不考虑成绩并列情况) 
-- 
-- 22、查询每门课程被选修的学生数；
-- 
-- 23、查询出只选修了一门课程的全部学生的学号和姓名；
-- 
-- 24、查询男生、女生的人数；
-- 
-- 25、查询姓“张”的学生名单；
-- 
-- 26、查询同名同姓学生名单，并统计同名人数；
-- 
-- 27、查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列；
-- 
-- 28、查询平均成绩大于85的所有学生的学号、姓名和平均成绩；
-- 
-- 29、查询课程名称为“数学”，且分数低于60的学生姓名和分数；
-- 
-- 30、查询课程编号为003且课程成绩在80分以上的学生的学号和姓名； 
-- 
-- 31、求选了课程的学生人数
-- 
-- 32、查询选修“杨艳”老师所授课程的学生中，成绩最高的学生姓名及其成绩；
-- 
-- 33、查询各个课程及相应的选修人数；
-- 
-- 34、查询不同课程但成绩相同的学生的学号、课程号、学生成绩；
-- 
-- 35、查询每门课程成绩最好的前两名；
-- 
-- 36、检索至少选修两门课程的学生学号；
-- 
-- 37、查询全部学生都选修的课程的课程号和课程名；
-- 
-- 38、查询没学过“叶平”老师讲授的任一门课程的学生姓名；
-- 
-- 39、查询两门以上不及格课程的同学的学号及其平均成绩；
select student_id,avg(num) from score where num<60  GROUP BY student_id HAVING count(course_id)>=2;
-- 40、检索“004”课程分数小于60，按分数降序排列的同学学号；
select * from score;
UPDATE score set num=50 where student_id= 5 and course_id =4;
select student_id from score where course_id = 4 and num <60 order by student_id desc;
-- 41、删除“002”同学的“001”课程的成绩；
DELETE FROM score where score.student_id =2 and score.course_id =1;