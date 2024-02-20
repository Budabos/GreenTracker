ALTER TABLE products
ALTER COLUMN eco_rating TYPE INTEGER
USING price::integer;