/*
Navicat MySQL Data Transfer

Source Server         : test
Source Server Version : 50562
Source Host           : localhost:3306
Source Database       : db1

Target Server Type    : MYSQL
Target Server Version : 50562
File Encoding         : 65001

Date: 2019-06-27 21:41:21
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for class
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `caption` char(20) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of class
-- ----------------------------
INSERT INTO `class` VALUES ('1', '一班');
INSERT INTO `class` VALUES ('2', '二班');
INSERT INTO `class` VALUES ('3', '三班');
INSERT INTO `class` VALUES ('4', '四班');
INSERT INTO `class` VALUES ('5', '五班');

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `cname` varchar(20) DEFAULT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`cid`),
  KEY `fk_tid_course_id` (`teacher_id`),
  CONSTRAINT `fk_tid_course_id` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`tid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of course
-- ----------------------------
INSERT INTO `course` VALUES ('1', '语文', '2');
INSERT INTO `course` VALUES ('2', '英语', '1');
INSERT INTO `course` VALUES ('3', '生物', '3');
INSERT INTO `course` VALUES ('4', '物理', '1');

-- ----------------------------
-- Table structure for score
-- ----------------------------
DROP TABLE IF EXISTS `score`;
CREATE TABLE `score` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `num` int(11) NOT NULL,
  PRIMARY KEY (`sid`),
  UNIQUE KEY `S_C_UQ` (`student_id`,`course_id`),
  KEY `fk_sid_sc_id` (`course_id`),
  CONSTRAINT `fk_sid_ss_id` FOREIGN KEY (`student_id`) REFERENCES `student` (`sid`),
  CONSTRAINT `fk_sid_sc_id` FOREIGN KEY (`course_id`) REFERENCES `course` (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of score
-- ----------------------------
INSERT INTO `score` VALUES ('1', '2', '1', '60');
INSERT INTO `score` VALUES ('2', '3', '3', '70');
INSERT INTO `score` VALUES ('3', '8', '1', '90');
INSERT INTO `score` VALUES ('4', '7', '4', '60');
INSERT INTO `score` VALUES ('5', '5', '4', '50');
INSERT INTO `score` VALUES ('6', '4', '4', '60');
INSERT INTO `score` VALUES ('7', '6', '3', '50');
INSERT INTO `score` VALUES ('20', '6', '2', '50');
INSERT INTO `score` VALUES ('21', '3', '4', '70');
INSERT INTO `score` VALUES ('22', '8', '4', '90');
INSERT INTO `score` VALUES ('23', '7', '1', '60');
INSERT INTO `score` VALUES ('24', '5', '3', '90');
INSERT INTO `score` VALUES ('25', '4', '2', '80');
INSERT INTO `score` VALUES ('26', '6', '4', '50');
INSERT INTO `score` VALUES ('27', '8', '2', '70');
INSERT INTO `score` VALUES ('28', '8', '3', '70');
INSERT INTO `score` VALUES ('29', '6', '1', '70');
INSERT INTO `score` VALUES ('30', '5', '1', '70');
INSERT INTO `score` VALUES ('31', '4', '1', '70');
INSERT INTO `score` VALUES ('32', '3', '1', '70');

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `sname` varchar(20) DEFAULT NULL,
  `gender` enum('男','女') DEFAULT NULL,
  `class_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`sid`),
  KEY `fk_sid_cid` (`class_id`),
  CONSTRAINT `fk_sid_cid` FOREIGN KEY (`class_id`) REFERENCES `class` (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('2', '陆远', '男', '1');
INSERT INTO `student` VALUES ('3', '张三', '男', '2');
INSERT INTO `student` VALUES ('4', '李四', '女', '1');
INSERT INTO `student` VALUES ('5', '王五', '女', '3');
INSERT INTO `student` VALUES ('6', '哈哈', '男', '4');
INSERT INTO `student` VALUES ('7', '接触', '男', '5');
INSERT INTO `student` VALUES ('8', '筛子', '男', '5');

-- ----------------------------
-- Table structure for teacher
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher` (
  `tid` int(11) NOT NULL AUTO_INCREMENT,
  `tname` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`tid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of teacher
-- ----------------------------
INSERT INTO `teacher` VALUES ('1', '叶平');
INSERT INTO `teacher` VALUES ('2', '李伟');
INSERT INTO `teacher` VALUES ('3', '李杰');
INSERT INTO `teacher` VALUES ('4', '陆远');

-- ----------------------------
-- Table structure for test
-- ----------------------------
DROP TABLE IF EXISTS `test`;
CREATE TABLE `test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `num` int(11) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq1` (`num`,`age`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of test
-- ----------------------------
