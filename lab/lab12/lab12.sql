.read sp19data.sql

-- Q2
CREATE TABLE obedience AS
  SELECT seven, animal FROM students;

-- Q3
CREATE TABLE smallest_int AS
  SELECT time, smallest FROM students WHERE smallest > 2 ORDER BY smallest LIMIT 20;

-- Q4
CREATE TABLE matchmaker AS
  SELECT s1.pet, s1.song, s1.color, s2.color FROM students AS s1, students AS s2
  WHERE s1.time < s2.time AND s1.pet = s2.pet AND s1.song = s2.song;
