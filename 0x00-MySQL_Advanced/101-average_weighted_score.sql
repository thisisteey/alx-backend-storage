-- Script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    UPDATE users AS Usr,
        (SELECT Usr.id, SUM(score * weight) / SUM(weight) AS weight_avg 
        FROM users AS Usr
        JOIN corrections as Corct ON Usr.id=Corct.user_id 
        JOIN projects AS Proj ON Corct.project_id=Proj.id
        GROUP BY Usr.id)
    AS WAVG
    SET Usr.average_score = WAVG.weight_avg
    WHERE Usr.id=WAVG.id;
END
$$
DELIMITER ;
