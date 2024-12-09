# Will Buckhout's GIS Team Data Challenge Results

## Hello! I've put together a step by step guide on how to complete the GIS Team Data Challenge using **[NYC Open Data](https://opendata.cityofnewyork.us/)**. 
My challenge results reflect open source data downloaded from the specified **311 Service Requests from 2010 to Present** dataset during the one week (7 day) period of **11/29/2024 to 12/05/2024**

# Step 1
- After navigating to the 311 Service Requests from 2010 to Present dataset and filtering for my specific 'Created_Date' dates and required 'Agency', the data is ready to be exported and I will need the API endpoint URL to do so. After selecting CSV file type, I can copy the auto-generated API url (as shown in the screenshot below). ![image](https://github.com/user-attachments/assets/e8d19438-a628-4ccf-bcf1-f73711ebd189)
- In order for me to download the very large dataset quickly and efficiently I wrote a python script that would make a request using the copied API endpoint, convert the table to a dataframe using PANDAS and output the requested data as a csv file. 

