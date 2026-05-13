import requests
import pandas as pd
import os
from io import BytesIO

# URL to the CSV file
file_url = "https://data.cityofnewyork.us/resource/erm2-nwe9.csv?$query=SELECT%0A%20%20%60unique_key%60%2C%0A%20%20%60created_date%60%2C%0A%20%20%60closed_date%60%2C%0A%20%20%60agency%60%2C%0A%20%20%60agency_name%60%2C%0A%20%20%60complaint_type%60%2C%0A%20%20%60descriptor%60%2C%0A%20%20%60location_type%60%2C%0A%20%20%60incident_zip%60%2C%0A%20%20%60incident_address%60%2C%0A%20%20%60street_name%60%2C%0A%20%20%60cross_street_1%60%2C%0A%20%20%60cross_street_2%60%2C%0A%20%20%60intersection_street_1%60%2C%0A%20%20%60intersection_street_2%60%2C%0A%20%20%60address_type%60%2C%0A%20%20%60city%60%2C%0A%20%20%60landmark%60%2C%0A%20%20%60facility_type%60%2C%0A%20%20%60status%60%2C%0A%20%20%60due_date%60%2C%0A%20%20%60resolution_description%60%2C%0A%20%20%60resolution_action_updated_date%60%2C%0A%20%20%60community_board%60%2C%0A%20%20%60bbl%60%2C%0A%20%20%60borough%60%2C%0A%20%20%60x_coordinate_state_plane%60%2C%0A%20%20%60y_coordinate_state_plane%60%2C%0A%20%20%60open_data_channel_type%60%2C%0A%20%20%60park_facility_name%60%2C%0A%20%20%60park_borough%60%2C%0A%20%20%60vehicle_type%60%2C%0A%20%20%60taxi_company_borough%60%2C%0A%20%20%60taxi_pick_up_location%60%2C%0A%20%20%60bridge_highway_name%60%2C%0A%20%20%60bridge_highway_direction%60%2C%0A%20%20%60road_ramp%60%2C%0A%20%20%60bridge_highway_segment%60%2C%0A%20%20%60latitude%60%2C%0A%20%20%60longitude%60%2C%0A%20%20%60location%60%0AWHERE%0A%20%20(%60created_date%60%0A%20%20%20%20%20BETWEEN%20%222024-11-30T12%3A52%3A30%22%20%3A%3A%20floating_timestamp%0A%20%20%20%20%20AND%20%222024-12-06T12%3A52%3A30%22%20%3A%3A%20floating_timestamp)%0A%20%20AND%20caseless_eq(%60agency%60%2C%20%22HPD%22)%0AORDER%20BY%20%60created_date%60%20DESC%20NULL%20FIRST%20LIMIT%201000000"
# Output CSV file path
output_csv_path = r'H:\whuckhout\PyCharm\GIS Data Challenge\Data\raw10.csv'

# output directory
output_folder = os.path.dirname(output_csv_path)
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
try:
    
    response = requests.get(file_url)
    response.raise_for_status()

    csv_data = pd.read_csv(BytesIO(response.content))
    
    csv_data.to_csv(output_csv_path, index=False)

    print(f"CSV file downloaded and saved successfully at: {output_csv_path}")

except Exception as e:
    print(f"Error processing: {e}")
