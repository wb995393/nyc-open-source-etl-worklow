# Will Buckhout's GIS Team Data Challenge Results

## Hello! I've put together a step by step guide on how to complete the GIS Team Data Challenge using **[NYC Open Data](https://opendata.cityofnewyork.us/)**. 
My challenge results reflect the specified **311 Service Requests from 2010 to Present** dataset filters during the one week (7 day) period of **11/29/2024 to 12/05/2024**

# Step 1
- After navigating to the 311 Service Requests from 2010 to Present dataset and filtering for my specific 'created_date_hour' dates and required 'Agency', the data is ready to be exported and I will need the API endpoint URL to do so. After selecting CSV file type, I can copy the auto-generated API URL (as shown in the screenshot below). ![image](https://github.com/user-attachments/assets/e8d19438-a628-4ccf-bcf1-f73711ebd189)
- In order for me to download the very large dataset quickly and efficiently, I wrote a **[Python Script](https://github.com/wb995393/gis-team-data-challenge-will-buckhout/blob/main/export_311_service_requests_2010topresent.py)** that would make a request using the copied API endpoint, convert the table to a dataframe using PANDAS and output the requested data as a CSV file.
- Once the script was complete, I still needed to add a LIMIT clause to the API endpoint in order to specify the maximum records to download. Since NYC Open Data uses Socrata API, the default query of only 1000 records retrieved needs to be updated and I did so by adding a LIMIT of 1000000 to the end of the query. The dataset had far fewer than 1000000 records so i knew this parameter would work.
- With the API endpoint updated, my script was ready to run and the 'raw.csv' file was properly downloaded into my personal folder.
# Step 2
- Now with my raw.csv dataset downloaded, a new column named 'created_date_hour' would need to be made and I did so in the csv using the following formula **=LEFT(A1, LEN(A1) - 10)**. This formula removed the last ten digits of text from every 'created_date' record and left me with a column that only showed the Year/Month/Day/Hour for each record. This process is shown in the screenshots below.
![image](https://github.com/user-attachments/assets/02f7e007-443d-4a95-92c5-adffa53c44da)

![image](https://github.com/user-attachments/assets/8d574be5-9ef6-42e3-a1b6-7b6b414e5216)

- Next, the table needed to be quireied in order to meet the specifications of Task 2 and aggregate the data. Using **[DBeaver Database Management/SQL IDE Software](https://dbeaver.io/download/)** I imported the raw data, wrote the following  **[SQL Query](https://github.com/wb995393/gis-team-data-challenge-will-buckhout/blob/main/count_by_complaint_type_by_created_date_hour.sql)** and was able to create a new aggregated table to complete task 2.
# Step 3
- To complete Task 3, I added my origininal 'raw.csv' table into ArcPro in order to create a line chart from the dataset.
- By selecting a line chart, the primary 'Date or Time' input needed to be dependent on the 'created_date_hour' column.
![image](https://github.com/user-attachments/assets/b74e425a-7db8-4bc1-9385-288ddf37bfc4)
- However, the 'created_date_hour' would need to be converted back to a 'Date' field type in ArcPro, since my previous conversion in excel had turned it into a 'Text' field. to rectify this I made a custom arcade expression using the Date() funcrtion.
![image](https://github.com/user-attachments/assets/fdf052b9-4c1e-4299-8327-7d33a61bbdb8)
- Now, I could complete the line chart using 1 hour increments and export it to PNG.
# Step 4
- I used ArcPro as well for the final task. After downloading the NTA shapefile, I created a GDB to import it into. Next I used a definition query to filter the raw.csv file for 'HEAT/HOT WATER' complaint types only and exported it into the geotabase as a GDB file.
- Finally, I noticed that there was one record that had a <Null> value for the 'latitude' and 'longitude' fields. It did have a street address, so I was able to search the address in google maps and copy the lat ond long from there.
- Now, with the correct file type and all records populated, I converted the raw.gbd dataset into a point layer using the 'latitude' and 'longitude' fields.
- To do so, I right clicked on the raw.gbd file, scrolled to 'Create Points From Table' and clicked 'XY Table To Point'
![image](https://github.com/user-attachments/assets/46e01604-e67f-42ae-be2f-4afbb3410b0f)
- Once the points were geocoded and the point layer was created, I then spatially joined the geocoded points layer to the NTA boundaries feature layer.
- 

  
