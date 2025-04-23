-- Description: Create an index on the first letter of the column 'name'
CREATE INDEX idx_name_first ON names (name(1));
