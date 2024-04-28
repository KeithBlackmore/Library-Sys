/*
 Navicat Premium Data Transfer

 Source Server         : my_link
 Source Server Type    : MySQL
 Source Server Version : 50562
 Source Host           : localhost:3306
 Source Schema         : library

 Target Server Type    : MySQL
 Target Server Version : 50562
 File Encoding         : 65001

 Date: 02/12/2022 20:29:37
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for book
-- ----------------------------
DROP TABLE IF EXISTS `book`;
CREATE TABLE `book`  (
  `ID` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `NAME` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `AUTHOR` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `TYPE` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `STATE` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `STORGE` int(30) NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of book
-- ----------------------------
INSERT INTO `book` VALUES ('1', '东方快车谋杀案', '阿加莎克里斯蒂', '悬疑', '可借', 2);
INSERT INTO `book` VALUES ('2', '无人生还', '阿加莎克里斯蒂', '悬疑', '可借', 10);
INSERT INTO `book` VALUES ('3', '巴普洛夫的猎犬', '柯南道尔', '悬疑', '可借', 17);
INSERT INTO `book` VALUES ('4', '尼罗河上的惨案', '阿加莎克里斯蒂', '悬疑', '可借', 1);
INSERT INTO `book` VALUES ('5', '三体', '刘慈欣', '科幻', '可借', 1);

-- ----------------------------
-- Table structure for client
-- ----------------------------
DROP TABLE IF EXISTS `client`;
CREATE TABLE `client`  (
  `ID` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `CODE` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `RATE` int(100) NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of client
-- ----------------------------
INSERT INTO `client` VALUES ('2', '123', 11);
INSERT INTO `client` VALUES ('3', '3', 0);

-- ----------------------------
-- Table structure for manager
-- ----------------------------
DROP TABLE IF EXISTS `manager`;
CREATE TABLE `manager`  (
  `ID` int(10) NOT NULL,
  `CODE` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of manager
-- ----------------------------
INSERT INTO `manager` VALUES (2, '2');
INSERT INTO `manager` VALUES (22, 'dwe2');
INSERT INTO `manager` VALUES (32, '11');

-- ----------------------------
-- Table structure for root_manager
-- ----------------------------
DROP TABLE IF EXISTS `root_manager`;
CREATE TABLE `root_manager`  (
  `ID` int(10) NOT NULL,
  `CODE` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of root_manager
-- ----------------------------
INSERT INTO `root_manager` VALUES (1, '1');

SET FOREIGN_KEY_CHECKS = 1;
