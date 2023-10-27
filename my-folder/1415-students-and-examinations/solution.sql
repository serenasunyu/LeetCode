# Write your MySQL query statement below
SELECT st.student_id, st.student_name, su.subject_name, COUNT(e.subject_name) AS attended_exams
FROM Students st
JOIN Subjects su
LEFT JOIN Examinations e
ON st.student_id = e.student_id
AND e.subject_name = su.subject_name
GROUP BY st.student_id, su.subject_name
ORDER BY student_id, subject_name;
