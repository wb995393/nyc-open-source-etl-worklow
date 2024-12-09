SELECT  
    created_date_hour,
	complaint_type,
    COUNT(complaint_type) AS count
FROM "raw"
GROUP BY 
	created_date_hour,    
	complaint_type
    
ORDER BY 
    created_date_hour DESC;

