ALTER TABLE reviews
ALTER COLUMN rating TYPE INTEGER
USING rating::integer;