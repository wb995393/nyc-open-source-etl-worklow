# Will Buckhout's GIS Team Data Challenge Results

## Hello! I've put together a step by step guide on how I completed the *GIS Team Data Challenge* using **[NYC Open Data](https://opendata.cityofnewyork.us/)**. Thank you for your time and consideration.
*My challenge results reflect the specified **311 Service Requests from 2010 to Present** dataset filters during the one week (7 day) period of **11/29/2024 to 12/05/2024**

# Step 1
- After navigating to the 311 Service Requests from 2010 to Present dataset and filtering for my specific `Created_Date` dates and required `Agency`, the data is ready to be exported and I will need the `API Endpoint URL` to do so. After selecting `.csv` file type, I can copy the auto-generated `API URL` (as shown in the screenshot below). ![image](https://github.com/user-attachments/assets/e8d19438-a628-4ccf-bcf1-f73711ebd189)
- In order for me to download the very large dataset quickly and efficiently, I wrote a **[Python Script](https://github.com/wb995393/gis-team-data-challenge-will-buckhout/blob/main/export_311_service_requests_2010topresent.py)** that makes a request using the copied `API Endpoint`, converts the table to a dataframe using `PANDAS` and outputs the requested data as a `.csv` file.
- Once the script was complete, I still needed to add a `LIMIT` clause to the `API Endpoint` in order to specify the maximum records to download. Since NYC Open Data uses `Socrata API`, the default query of only 1000 records retrieved needs to be updated and I did so by adding a `LIMIT of 1000000` to the end of the query. The dataset had far fewer than `1000000` records so I knew this parameter would work.
- With the `API Endpoint` updated, my script was ready to run and the **[`raw.csv`](https://github.com/wb995393/gis-team-data-challenge-will-buckhout/blob/main/raw.csv)** file was downloaded into my personal folder.
# Step 2
- Now with my `raw.csv` dataset downloaded, a new column named `created_date_hour` would need to be made and I did so in the `.csv` using the following formula **=LEFT(A1, LEN(A1) - 10)**. This formula removed the last ten digits of text from every `created_date` record and left me with a column that only showed the `Year/Month/Day/Hour` for each record. This process is shown in the screenshots below.
![image](https://github.com/user-attachments/assets/02f7e007-443d-4a95-92c5-adffa53c44da)

![image](https://github.com/user-attachments/assets/8d574be5-9ef6-42e3-a1b6-7b6b414e5216)

- Next, the table needed to be quiried in order to aggregate the data. Using **[DBeaver Database Management/SQL IDE Software](https://dbeaver.io/download/)**, I imported the `raw.csv` data, wrote the following  **[SQL Query](https://github.com/wb995393/gis-team-data-challenge-will-buckhout/blob/main/count_by_complaint_type_by_created_date_hour.sql)** and created a **[new aggregated table](https://github.com/wb995393/gis-team-data-challenge-will-buckhout/blob/main/raw_aggregate.csv)** to complete Task 2.
# Step 3
- To complete Task 3, I added my original `raw.csv` table into `ArcPro` in order to create a line chart from the dataset.
- By selecting a line chart, the primary `Date or Number` input needed to be dependent on the `created_date_hour` column.
![image](https://github.com/user-attachments/assets/b74e425a-7db8-4bc1-9385-288ddf37bfc4)
- However, the `created_date_hour` would need to be converted back to a `Date` field type in `ArcPro`, since my previous conversion in excel had turned it into a `Text` field. To rectify this, I made a custom Arcade expression using the `Date()` function.
![image](https://github.com/user-attachments/assets/fdf052b9-4c1e-4299-8327-7d33a61bbdb8)
- I then completed the **[multi-line plot chart](https://github.com/wb995393/gis-team-data-challenge-will-buckhout/blob/main/service_request_complaints_per_hour_by_complaint_type_Line_Chart.png)** using 1 hour increments and exported it to `.png`.
# Step 4
- I used `ArcPro` for the final task as well. After downloading the `NTA Shapefile`, I imported it into a new `geodatabase`. Next I used a definition query to filter the `raw.csv` file for `HEAT/HOT WATER` complaint types only, then I exported it into the `geodatabase` as a `.gdb` file.
- Finally, I noticed that there was one record that had a `<Null>` value for the `latitude` and `longitude` fields. It did have a street address, so I was able to search the address in google maps, copy the lat/long provided from there and populate the lat/long for the `<Null>` values.
- Now, with the correct file type and all records populated, I converted the `raw.gdb` dataset into a point layer using the `latitude` and `longitude` fields.
- To do so, I right clicked on the `raw.gdb` file, scrolled to `Create Points From Table` and clicked `XY Table To Point`
![image](https://github.com/user-attachments/assets/46e01604-e67f-42ae-be2f-4afbb3410b0f)
- Once the points were geocoded and the point layer was created, I then spatially joined the geocoded points layer to the `NTA boundaries` feature layer and exported the joined layer.
- To generate the final display, I used graduated colors dependent on the `Join_Count` field.
- Lastly, I created a map template and exported the final **[Choropleth Map](https://github.com/wb995393/gis-team-data-challenge-will-buckhout/blob/main/heat_hotwater_servicerequest_complaints_by_NTA_Choropleth_Map.png)** results to `.png`.
  

  
