-- Description: Create index on the first letter of the column 'name' and the column 'score'
CREATE INDEX idx_name_first_score
ON names (name (1), score)
