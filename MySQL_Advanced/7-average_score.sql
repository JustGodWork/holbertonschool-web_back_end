-- Description: Create a procedure to compute the average score for a user
DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT;

    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = user_id;

    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END$$

DELIMITER;
