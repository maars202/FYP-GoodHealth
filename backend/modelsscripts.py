

drop table if exists `User`;
drop table if exists `Roles_users`;
drop table if exists `Role`;
CREATE TABLE IF NOT EXISTS User(
    id INT AUTO_INCREMENT NOT NULL,
    email VARCHAR(250),
    username VARCHAR(250),
    PASSWORD VARCHAR(250),
    active BOOLEAN,
    primary key (id),
    CONSTRAINT uc_studentId UNIQUE (email)  
); CREATE TABLE IF NOT EXISTS Role(
    id INT AUTO_INCREMENT NOT NULL,
    NAME VARCHAR(250),
    description VARCHAR(250),
    primary key (id),
    CONSTRAINT uc_studentId UNIQUE (NAME)  
); 
CREATE TABLE IF NOT EXISTS Roles_users(
    id INT AUTO_INCREMENT NOT NULL,
    user_id INT,
    role_id INT,
    primary key (id),
    CONSTRAINT uc_studentId UNIQUE (user_id, role_id)  
);

INSERT INTO `Roles_users` ( `user_id`, `role_id`) VALUES
(1, 1),
(2, 2);

INSERT INTO `Role` (`NAME`, `description`) VALUES
('Admin', 'creating residents and editting views'),
('User', 'cannot view some pages');

INSERT INTO `User` (`id`, `email`, `username`, `PASSWORD`, `active`) VALUES
(1, 'maarunip.2020@scis.smu.edu.sg', 'mmm', 'sha256$l7EdBUN0tJ1aSx3j$aa7650b88ad704f171c286fede0f6df714bcaa12243e7e982aca2eb9475b58c9', 1),
(2, 'paarunip.2020@scis.smu.edu.sg', 'ppp', 'sha256$QD1RcpBg5uZgwMkP$1854213e1b9e7782429694838a0a0786d4c4486fdca0ce2b25435bea7f7d7ac7', 1);


    CONSTRAINT FK_PersonOrder2 FOREIGN KEY(role_id) REFERENCES Role(id),
    CONSTRAINT FK_PersonOrder1 FOREIGN KEY(user_id) REFERENCES User(id)



