-- Create table
CREATE TABLE genes (
    gene_id TEXT,
    length INTEGER,
    gc_content REAL,
    species TEXT
);

-- Insert data
INSERT INTO genes VALUES ('gene1', 500, 42.3, 'Human');
INSERT INTO genes VALUES ('gene2', 800, 55.1, 'Mouse');
INSERT INTO genes VALUES ('gene3', 300, 38.5, 'Human');
INSERT INTO genes VALUES ('gene4', 1200, 60.2, 'Bacteria');

-- Queries practiced

-- Human genes
SELECT * FROM genes WHERE species = 'Human';

-- Average length
SELECT AVG(length) FROM genes;

-- Count per species
SELECT species, COUNT(*) 
FROM genes 
GROUP BY species;
