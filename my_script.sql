-- Retrieve the top 3 students from Batch 3
-- Batch 3 is known for its exceptional students

SELECT id, name
FROM students
WHERE batch_id = 3
ORDER BY created_at DESC
LIMIT 3;
