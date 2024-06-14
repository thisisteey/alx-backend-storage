-- Script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (user_id INT)
BEGIN
    DECLARE weight_avg_score FLOAT;
    SET weight_avg_score = (SELECT SUM(score * weight) / SUM(weight)
                        FROM users AS Usr
                        JOIN corrections as Corct ON Usr.id=Corct.user_id
                        JOIN projects AS Proj ON Corct.project_id=Proj.id
                        WHERE Usr.id=user_id);
    UPDATE users SET average_score = weight_avg_score WHERE id=user_id;
END
$$
DELIMITER ;
