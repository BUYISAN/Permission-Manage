/*
 Navicat Premium Data Transfer

 Source Server         : Mysql
 Source Server Type    : MySQL
 Source Server Version : 50717
 Source Host           : localhost:3306
 Source Schema         : flask-demo

 Target Server Type    : MySQL
 Target Server Version : 50717
 File Encoding         : 65001

 Date: 17/01/2018 19:52:54
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for groups
-- ----------------------------
DROP TABLE IF EXISTS `groups`;
CREATE TABLE `groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(64) DEFAULT NULL,
  `menu_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `menu_id` (`menu_id`),
  CONSTRAINT `groups_ibfk_1` FOREIGN KEY (`menu_id`) REFERENCES `menu` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of groups
-- ----------------------------
BEGIN;
INSERT INTO `groups` VALUES (1, '用户组', 1);
INSERT INTO `groups` VALUES (2, '订单', 2);
COMMIT;

-- ----------------------------
-- Table structure for menu
-- ----------------------------
DROP TABLE IF EXISTS `menu`;
CREATE TABLE `menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of menu
-- ----------------------------
BEGIN;
INSERT INTO `menu` VALUES (1, '菜单一');
INSERT INTO `menu` VALUES (2, '菜单二');
COMMIT;

-- ----------------------------
-- Table structure for permission
-- ----------------------------
DROP TABLE IF EXISTS `permission`;
CREATE TABLE `permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) DEFAULT NULL,
  `url` varchar(64) DEFAULT NULL,
  `code` varchar(32) DEFAULT NULL,
  `menu_gp_id` int(11) DEFAULT NULL,
  `groups_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `groups_id` (`groups_id`),
  KEY `menu_gp_id` (`menu_gp_id`),
  CONSTRAINT `permission_ibfk_1` FOREIGN KEY (`groups_id`) REFERENCES `groups` (`id`),
  CONSTRAINT `permission_ibfk_2` FOREIGN KEY (`menu_gp_id`) REFERENCES `permission` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of permission
-- ----------------------------
BEGIN;
INSERT INTO `permission` VALUES (1, '查看用户', '/user', 'list', NULL, 1);
INSERT INTO `permission` VALUES (2, '编辑用户', '/user/edit/d+', 'edit', 1, 1);
INSERT INTO `permission` VALUES (3, '添加用户', '/user/add/', 'add', 1, 1);
INSERT INTO `permission` VALUES (4, '删除用户', '/user/del/d+', 'del', 1, 1);
INSERT INTO `permission` VALUES (5, '查看订单', '/order/', 'list', NULL, 2);
INSERT INTO `permission` VALUES (6, '编辑订单', '/order/edit/d+', 'edit', 5, 2);
INSERT INTO `permission` VALUES (7, '添加订单', '/order/add/', 'add', 5, 2);
INSERT INTO `permission` VALUES (8, '删除订单', '/order/del/', 'del', 5, 2);
COMMIT;

-- ----------------------------
-- Table structure for position
-- ----------------------------
DROP TABLE IF EXISTS `position`;
CREATE TABLE `position` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of position
-- ----------------------------
BEGIN;
INSERT INTO `position` VALUES (1, 'CEO');
INSERT INTO `position` VALUES (2, '部长');
INSERT INTO `position` VALUES (3, '业务员');
COMMIT;

-- ----------------------------
-- Table structure for position2permission
-- ----------------------------
DROP TABLE IF EXISTS `position2permission`;
CREATE TABLE `position2permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `position_id` int(11) DEFAULT NULL,
  `permission_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `permission_id` (`permission_id`),
  KEY `position_id` (`position_id`),
  CONSTRAINT `position2permission_ibfk_1` FOREIGN KEY (`permission_id`) REFERENCES `permission` (`id`),
  CONSTRAINT `position2permission_ibfk_2` FOREIGN KEY (`position_id`) REFERENCES `position` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of position2permission
-- ----------------------------
BEGIN;
INSERT INTO `position2permission` VALUES (1, 1, 1);
INSERT INTO `position2permission` VALUES (2, 1, 2);
INSERT INTO `position2permission` VALUES (3, 1, 3);
INSERT INTO `position2permission` VALUES (4, 1, 4);
INSERT INTO `position2permission` VALUES (5, 1, 5);
INSERT INTO `position2permission` VALUES (6, 1, 6);
INSERT INTO `position2permission` VALUES (7, 1, 7);
INSERT INTO `position2permission` VALUES (8, 1, 8);
INSERT INTO `position2permission` VALUES (9, 3, 1);
INSERT INTO `position2permission` VALUES (10, 3, 2);
COMMIT;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `password` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_user_username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
BEGIN;
INSERT INTO `user` VALUES (1, 'egon', '123');
INSERT INTO `user` VALUES (2, 'alex', '123');
COMMIT;

-- ----------------------------
-- Table structure for user2position
-- ----------------------------
DROP TABLE IF EXISTS `user2position`;
CREATE TABLE `user2position` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `position_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `position_id` (`position_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `user2position_ibfk_1` FOREIGN KEY (`position_id`) REFERENCES `position` (`id`),
  CONSTRAINT `user2position_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user2position
-- ----------------------------
BEGIN;
INSERT INTO `user2position` VALUES (1, 1, 1);
INSERT INTO `user2position` VALUES (2, 2, 3);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
