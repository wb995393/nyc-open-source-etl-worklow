# Will Buckhout's GIS Team Data Challenge Results

## Hello! I've put together a step by step guide on how to complete the GIS Team Data Challenge using **[NYC Open Data](https://opendata.cityofnewyork.us/)**. 
My challenge results reflect open source data downloaded from the specified **311 Service Requests from 2010 to Present** dataset during the one week (7 day) period of **11/29/2024 to 12/05/2024**

# Step 1
- After navigating to the 311 Service Requests from 2010 to Present dataset and filtering for my specific 'Created_Date' dates and required 'Agency', the data is ready to be exported and I will need the API endpoint URL to do so. After selecting CSV file type, I can copy the auto-generated API URL (as shown in the screenshot below). ![image](https://github.com/user-attachments/assets/e8d19438-a628-4ccf-bcf1-f73711ebd189)
- In order for me to download the very large dataset quickly and efficiently, I wrote a Python script (INSERT LINK) that would make a request using the copied API endpoint, convert the table to a dataframe using PANDAS and output the requested data as a CSV file.
- Once the script was complete, I still needed to add a LIMIT clause to the API endpoint in order to specify the maximum records to download. Since NYC Open Data uses Socrata API, the default query of only 1000 records retrieved needs to be updated and I did so by adding a LIMIT of 1000000 to the end of the query. The dataset had far fewer than 1000000 records so i knew this parameter would work.
- With the API endpoint updated, my script was ready to run and the 'raw.csv' file was properly downloaded into my personal folder.
# Step 2
- Now with my raw.csv dataset downloaded, a new column named 'created_date_hour' would need to be made and I did so in the csv using the following formula **=LEFT(A1, LEN(A1) - 10)**. This formula removed the last ten digits of text from every 'created_date' record and left me with a column that only showed the Year/Month/Day/Hour for each record. This process is shown in the screenshots below.
![image](https://github.com/user-attachments/assets/02f7e007-443d-4a95-92c5-adffa53c44da)
![image](https://github.com/user-attachments/assets/8457b3c7-25fa-46c0-979b-a1fb4698a4f3)

