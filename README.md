# New York City 311 Data

## Hello! I've put together a step by step guide on how to extract, transform and load **[NYC Open Data](https://opendata.cityofnewyork.us/)** 
*This data reflects the one week (7 day) period of **11/29/2024 to 12/05/2024**

# Step 1
- Navigate to the **[NYC Open Data](https://opendata.cityofnewyork.us/)**, click the 'Data' tab and type "311 Service Requests from 2010 to Present" in the search bar. Click on the "311 Service Requests from 2010 to Present" dataset and click the 'Data' tab. Once the data user interface is shown, filter for the specific `Created_Date` dates and required `Agency`. Once filtered, the data is ready to be exported and and you will need the `API endpoint URL` to do so. After selecting `.csv` file type, copy the auto-generated `API URL` (as shown in the screenshot below).

![image](https://github.com/user-attachments/assets/e8d19438-a628-4ccf-bcf1-f73711ebd189)
- In order to download the very large dataset quickly and efficiently, use this **[Python Script](https://github.com/wb995393/gis-team-data-challenge-will-buckhout/blob/main/export_311_service_requests_2010topresent.py)** that makes a request using the copied `API endpoint`, converts the table to a dataframe using `PANDAS` and outputs the requested data as a `.csv` file.
- Once the script is complete, add a `LIMIT` clause to the `API endpoint` in order to specify the maximum records to download. Since NYC Open Data uses `Socrata API`, the default query of only 1000 records retrieved needs to be updated, so add a `LIMIT of 1000000` to the end of the query. The dataset had far fewer than `1000000` records so this parameter should work.
- With the `API endpoint` updated, the script is ready to run and the **[`raw.csv`](https://github.com/wb995393/gis-team-data-challenge-will-buckhout/blob/main/raw.csv)** file should output to the folder specified in the python script.
# Step 2
- Now, with the `raw.csv` dataset downloaded, a new column named `created_date_hour` needs to be made and, so in the `raw.csv` use the following formula **=LEFT(A1, LEN(A1) - 10)**. This formula removes the last ten digits of text from every `created_date` record and leaves you with a column that only shows the `Year/Month/Day/Hour` for each record. This process is shown in the screenshots below.

![image](https://github.com/user-attachments/assets/02f7e007-443d-4a95-92c5-adffa53c44da)

![image](https://github.com/user-attachments/assets/8d574be5-9ef6-42e3-a1b6-7b6b414e5216)

- Next, the table needs to be quiried in order to aggregate the data. Using **[DBeaver Database Management/SQL IDE Software](https://dbeaver.io/download/)**, import the `raw.csv` data and write the following  **[SQL Query](https://github.com/wb995393/gis-team-data-challenge-will-buckhout/blob/main/count_by_complaint_type_by_created_date_hour.sql)** which will create a **[new aggregated table](https://github.com/wb995393/gis-team-data-challenge-will-buckhout/blob/main/raw_aggregate.csv)**
# Step 3
- Add the original `raw.csv` table into `ArcPro` in order to create a line chart from the dataset.
- By selecting a line chart, the primary `Date or Number` input will be dependent on the `created_date_hour` column.

![image](https://github.com/user-attachments/assets/b74e425a-7db8-4bc1-9385-288ddf37bfc4)
- However, the `created_date_hour` will need to be converted back to a `Date` field type in `ArcPro`, since the previous conversion in excel had turned it into a `Text` field. To rectify this, make a custom `Arcade` expression using the `Date()` function.

![image](https://github.com/user-attachments/assets/fdf052b9-4c1e-4299-8327-7d33a61bbdb8)
- Complete the **[multi-line plot chart](https://github.com/wb995393/gis-team-data-challenge-will-buckhout/blob/main/service_request_complaints_per_hour_by_complaint_type_Line_Chart.png)** using 1 hour increments and export it.
# Step 4
- Use `ArcPro` for the final task as well. After downloading the `NTA Shapefile`, import it into a new `geodatabase`. Next, use a definition query to filter the `raw.csv` file for `HEAT/HOT WATER` complaint types only, then export it into the `geodatabase` as a `.gdb` file.
- Within the newly exported `raw.gdb` table, there will be a record that has a `<Null>` value for the `latitude` and `longitude` fields. Missing data occurances like this do happen from time to time with NYC Open Source Data. The `incident_address` field populated, so you'll need to search the address in google maps, copy the lat/long provided from there and populate the lat/long for the `<Null>` values in the `raw.gdb` table.
- Now, with the correct file type and all records populated, convert the `raw.gdb` dataset into a point layer using the `latitude` and `longitude` fields.
- To do so, right click on the `raw.gdb` file, scroll to `Create Points From Table` and click `XY Table To Point`

![image](https://github.com/user-attachments/assets/46e01604-e67f-42ae-be2f-4afbb3410b0f)
- Once the points are geocoded and the point layer is created, spatially join the geocoded points layer to the `NTA Boundaries` feature layer and export the joined layer.
- To generate the final display, use graduated colors dependent on the `Join_Count` field.
- Lastly, creat a map template and export the final **[Choropleth Map](https://github.com/wb995393/gis-team-data-challenge-will-buckhout/blob/main/heat_hotwater_servicerequest_complaints_by_NTA_Choropleth_Map.png)** results. All of the layers used to generate the final map are included in this **[`ZIP File`](https://github.com/wb995393/gis-team-data-challenge-will-buckhout/blob/main/gis_team_data_challenge_Feature_Layers.gdb.zip)**
  

  
