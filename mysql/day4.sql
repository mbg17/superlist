#1、自行创建测试数据
select a.student_id
  from (select s1.student_id, s1.num
          from score s1
         where s1.course_id =1) a inner
  join (select s1.student_id, s1.num
          from score s1
         where s1.course_id =2) b on a.student_id = b.student_id
 where a.num > b.num;
#2、查询“生物”课程比“物理”课程成绩高的所有学生的学号；
select a.student_id from 
(select score.num as num,score.student_id from score left join course on score.course_id = course.cid where course.cname ='生物' ) as a,
(select score.num as num,score.student_id from score left join course on score.course_id = course.cid where course.cname ='物理' ) as b
where a.num>b.num and a.student_id = b.student_id GROUP BY a.student_id;
#3、查询平均成绩大于60分的同学的学号和平均成绩； 
select student_id,avg(num) from score GROUP BY student_id HAVING avg(num)>60;
#4、查询所有同学的学号、姓名、选课数、总成绩；
select student.sid as '学号',student.sname as '姓名',count(score.course_id) as '课程数',sum(score.num) as '总成绩' from score
left join student on student.sid = score.student_id GROUP BY student.sid;
#5、查询姓“李”的老师的个数；
select count(tid) from teacher where tname like '李%';
#6、查询没学过“叶平”老师课的同学的学号、姓名；
select student.sid,student.sname from student where student.sid not in (select student.sid from student left join score on student.sid = score.student_id 
left JOIN course on score.course_id = course.cid LEFT JOIN teacher on course.teacher_id = teacher.tid where teacher.tname like '李平%'
GROUP BY  student.sid );
#7、查询学过“001”并且也学过编号“002”课程的同学的学号、姓名；
select a.student_id,student.sname from score a LEFT JOIN student on a.student_id = student.sid 
left join score b on a.student_id = b.student_id where a.course_id in (1) and b.course_id in (2)  GROUP BY a.student_id ;
#8、查询学过“叶平”老师所教的所有课的同学的学号、姓名；
select student.sid,student.sname FROM student left join score on student.sid = score.student_id where score.course_id in (
SELECT course.cid from course left join teacher on course.teacher_id = teacher.tid where teacher.tname = '李平老师' GROUP BY course.cid
) GROUP BY student.sid HAVING count(course_id) = 
(select count(cid) from course LEFT JOIN teacher on teacher.tid = course.teacher_id where teacher.tname = '李平老师');
select a.student_id,student.sname from score a LEFT JOIN student on a.student_id = student.sid 
left join score b on a.student_id = b.student_id where a.course_id in (2) and b.course_id in (4)  GROUP BY a.student_id ;
#9、查询课程编号“002”的成绩比课程编号“001”课程低的所有同学的学号、姓名；
select student.sid,student.sname from student 
left join (select student_id,score.num as num from score where score.course_id = 1 ) as a on a.student_id = student.sid
left join (select student_id,score.num as num from score where score.course_id = 2 ) as b on b.student_id = student.sid
where b.num <a.num GROUP BY student.sid;
#10、查询有课程成绩小于60分的同学的学号、姓名；
select student.sid,student.sname from student left JOIN score on student.sid = score.student_id WHERE
score.num <60 group by student.sid;
#11、查询没有学全所有课的同学的学号、姓名
select sid,sname from student ,(select student_id from score GROUP BY student_id having count(course_id)<(select count(cid) from course)) as B 
where student.sid = B.student_id;
select student.sid,student.sname from student LEFT JOIN score on score.student_id = student.sid LEFT JOIN 
course on course.cid=score.course_id GROUP BY student_id having count(course_id)<(select count(cid) from course);
#12、查询至少有一门课与学号为“001”的同学所学相同的同学的学号和姓名；
SELECT student.sid ,student.sname from student LEFT JOIN score on score.student_id = student.sid 
where score.course_id in (select course_id from score where student_id =1) and score.student_id<>1 GROUP BY student.sid;
#13、查询至少学过学号为“001”同学所选课程中任意一门课的其他同学学号和姓名；
select sid ,sname from student LEFT JOIN (select student_id from score where course_id in 
(select course_id from score WHERE student_id = 1) GROUP BY student_id) as b on  b.student_id = student.sid where student.sid <>1 ;
#14、查询和“002”号的同学学习的课程完全相同的其他同学学号和姓名；
 select student_id,sname from score left join student on score.student_id = student.sid where student_id in (
select student_id from score  
/*筛选学号不为2且课程数和2号同学一样的学生id*/
where student_id != 2 group by student_id HAVING 
/*筛选课程数和2号同学一样的*/
count(course_id) = (select count(1) from score where student_id = 2))
/*筛选2号同学学过的课程id 通过学号分组*/
and course_id in (select course_id from score where student_id = 2) group by student_id 
/*课程数和2号同学一样*/
HAVING count(course_id) = (select count(2) from score where student_id = 2);
#15、删除学习“叶平”老师课的SC表记录；
DELETE FROM score where course_id in (select course_id from score LEFT JOIN course on course.cid = course_id 
LEFT JOIN teacher on course.teacher_id  = teacher.tid where teacher.tname like '李平%' group by course_id
)
#16、向SC表中插入一些记录，这些记录要求符合以下条件：①没有上过编号“002”课程的同学学号；②插入“002”号课程的平均成绩； 
INSERT INTO score(student_id,course_id,num) select 
a.student_id,b.course_id,(select avg(num) from score where course_id = 2)
from (select score.student_id from score where score.student_id not in 
(select student_id from score where course_id =2 GROUP BY student_id)
) as a,(select course_id from score group by course_id) as b ;
#17、按平均成绩从低到高显示所有学生的“语文”、“数学”、“英语”三门的课程成绩，按如下形式显示： 学生ID,语文,数学,英语,有效课程数,有效平均分；
select student_id as a,
IFNULL((select num from score LEFT JOIN course on course.cid = score.course_id where course.cname = '生物' and score.student_id =a),0) as '生物',
IFNULL((select num from score LEFT JOIN course on course.cid = score.course_id where course.cname = '物理' and score.student_id =a),0) as '物理',
IFNULL((select num from score LEFT JOIN course on course.cid = score.course_id where course.cname = '体育' and score.student_id =a),0) as '体育',
(select avg(num) from score LEFT JOIN course on course.cid = score.course_id where course.cname in('生物','物理','体育') and score.student_id =a) as pj
from score GROUP BY a ORDER BY pj;
#18、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；
select course_id as '课程ID',max(num)as '最高分',min(num)as '最低分' from score GROUP BY course_id;
#19、按各科平均成绩从低到高和及格率的百分数从高到低顺序；
select course_id as 课程编号,AVG(num) as 平均成绩,sum(case when num<60 then 0 else 1 END)/sum(1) as 及格率 from score GROUP BY course_id order by 平均成绩
,及格率 desc;
#20、课程平均分从高到低显示（现实任课老师）；
select IFNULL(course_id,0) as 课程ID,tname as 教师姓名,IFNULL(avg(score.num),0) as 平均成绩 from teacher 
LEFT JOIN course on course.teacher_id = teacher.tid 
LEFT JOIN score on score.course_id = course.cid
GROUP BY course_id order by avg(score.num) desc;
#21、查询各科成绩前三名的记录:(不考虑成绩并列情况) 
select * from (
select student_id,course_id as c,num,
if(isnull((select num from score where course_id = c group by num ORDER BY num desc limit 0,1)),0,(select num from score where course_id = c group by num ORDER BY num desc limit 0,1)) as 第一名, 
if(isnull((select num from score where course_id = c group by num ORDER BY num desc limit 1,1)),0,(select num from score where course_id = c group by num ORDER BY num desc limit 0,1)) as 第二名, 
if(isnull((select num from score where course_id = c group by num ORDER BY num desc limit 2,1)),0,(select num from score where course_id = c group by num ORDER BY num desc limit 2,1)) as 第三名
 from score) as b where b.num >= b.第三名 order by b.c ;
#22、查询每门课程被选修的学生数；
select count(student_id) from score GROUP BY course_id;
#23、查询出只选修了一门课程的全部学生的学号和姓名；
select sid,sname from student where sid in  (select student_id from score GROUP BY student_id HAVING count(student_id) =1) ;
#24、查询男生、女生的人数；
select count(*) from student where gender ='男' ;
#25、查询姓“张”的学生名单；
select * from student where sname like '张%';
#26、查询同名同姓学生名单，并统计同名人数；
select count(a.sid) from student as  a,student as b where a.sid <> b.sid and a.sname = b.sname; 
#27、查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列；
select avg(num),course_id from score GROUP BY course_id order by avg(num),course_id desc;
#28、查询平均成绩大于85的所有学生的学号、姓名和平均成绩；
select student.sid ,student.sname ,(select avg(num) from score where student_id = student.sid ) as '平均成绩' FROM
student LEFT join score on score.student_id = student.sid GROUP BY student.sid HAVING avg(num) >85;
#29、查询课程名称为“数学”，且分数低于60的学生姓名和分数；
select student.sname,score.num from student LEFT JOIN score on score.student_id = student.sid 
LEFT JOIN course on course.cid = score.course_id WHERE
score.course_id = (select cid from course where cname = '物理') and score.num <60 GROUP BY score.student_id;

select student.sid,student.sname from student LEFT JOIN score on score.student_id = student.sid 
left JOIN course on course.cid = score.course_id where score.num <60 and course.cname = '物理';
#30、查询课程编号为003且课程成绩在80分以上的学生的学号和姓名； 
SELECT student.sid,student.sname from student left join score on score.student_id = student.sid
where score.num >80 and score.course_id =3 group by student.sid;
#31、求选了课程的学生人数
select count(a.student_id) from (select student_id from score GROUP BY student_id) as a;
#32、查询选修“杨艳”老师所授课程的学生中，成绩最高的学生姓名及其成绩；
SELECT student.sid,student.sname,score.num from student LEFT JOIN score on score.student_id = student.sid 
where score.course_id in (select cid from course LEFT JOIN teacher on teacher.tid = course.teacher_id  where teacher.tname ='李平老师' ) 
and score.num = (select max(num) from score where score.course_id in 
(select cid from course LEFT JOIN teacher on teacher.tid = course.teacher_id  
where teacher.tname ='李平老师' GROUP BY cid)) group by score.student_id;

select sname,num from score
    left join student on score.student_id = student.sid
    where score.course_id in (select course.cid from course left join teacher on course.teacher_id = teacher.tid where tname='李平老师') 
order by num desc limit 1;
#33、查询各个课程及相应的选修人数；
select score.course_id ,course.cname,count(student_id) from score left JOIN course on course.cid = score.course_id
GROUP BY score.course_id;
#34、查询不同课程但成绩相同的学生的学号、课程号、学生成绩；
select a.student_id,a.course_id,a.num from 
(select student_id,course_id,num from score) as a,
(select student_id,course_id,num from score) as b
where a.student_id<>b.student_id and a.course_id<>b.course_id and a.num=b.num GROUP by student_id;
#35、查询每门课程成绩最好的前两名；

#36、检索至少选修两门课程的学生学号；
select student_id from score GROUP BY student_id HAVING count(course_id) >=2;
#37、查询全部学生都选修的课程的课程号和课程名；
select course.cid,course.cname from course left join score on course.cid = score.course_id 
group by score.course_id HAVING count(course_id) = (select count(sid) from student);
#38、查询没学过“叶平”老师讲授的任一门课程的学生姓名；
select sname from student where sid not in (
select score.student_id from score left join course on course.cid = score.course_id
LEFT JOIN teacher on teacher.tid = course.teacher_id 
where teacher.tname = '李平老师' group by score.student_id);
#39、查询两门以上不及格课程的同学的学号及其平均成绩；
select student_id,avg(num) from score where student_id in
(select student_id from score where num <60 group by student_id HAVING count(course_id)>=2)GROUP BY student_id;
#40、检索“004”课程分数小于60，按分数降序排列的同学学号；
SELECT student_id from score where course_id =4 and num<60 ORDER BY num desc;
#41、删除“002”同学的“001”课程的成绩；
DELETE from score where student_id = 2 and course_id =1;