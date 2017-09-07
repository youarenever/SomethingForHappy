PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE hello (id INTEGER PRIMARY KEY,texts VARCHAR(100),profilesId INTEGER NOT NULL,status INTEGER,weight INTEGER,defaultweight INTEGER,CreatedTime TimeStamp NOT NULL DEFAULT (datetime('now','localtime')));
INSERT INTO hello VALUES(1,'HELLO WORLD',1,1,60,60,'2017-09-07 14:10:49');
INSERT INTO hello VALUES(2,'HELLO BOSS',1,1,60,60,'2017-09-07 14:10:49');
INSERT INTO hello VALUES(3,'早上好',2,1,100,100,'2017-09-07 14:10:49');
INSERT INTO hello VALUES(4,'一年之计在于晨',2,1,100,100,'2017-09-07 14:10:49');
INSERT INTO hello VALUES(5,'起来了呀',2,1,100,100,'2017-09-07 14:10:49');
CREATE TABLE jokes (id INTEGER PRIMARY KEY,texts VARCHAR(255),status INTEGER,CreatedTime TEXT);
CREATE TABLE interaction (id INTEGER PRIMARY KEY,command VARCHAR(50),description VARCHAR(100),actionId INTEGER NOT NULL ,status INTEGER,CreatedTime TEXT);
CREATE TABLE actions (id INTEGER PRIMARY KEY,description VARCHAR(100),status INTEGER,CreatedTime TEXT);
CREATE TABLE helloProfiles (id INTEGER PRIMARY KEY,description VARCHAR(100),status INTEGER NOT NULL ,begintime TEXT,endtime TEXT,usedate TEXT,week TEXT);
INSERT INTO helloProfiles VALUES(1,'随时可用',2,'','','','');
INSERT INTO helloProfiles VALUES(2,'早上使用',1,'06','18','2017-09-06','1');
INSERT INTO helloProfiles VALUES(3,'早上使用',1,'06','18','2017-09-06','6');
INSERT INTO helloProfiles VALUES(4,'早上使用',1,'06','18','2017-09-06','4');


COMMIT;
