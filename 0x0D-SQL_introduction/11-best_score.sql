-- A script to list records with scores >= 10 in second_table.
-- Results display both the score and the name (in this order)
-- Records ordered by score (top first)

SELECT score, name
FROM second_table
WHERE score >= 10 ORDER BY score DESC;
