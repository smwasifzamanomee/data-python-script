import requests
import json
 
# API endpoint
url = "http://0.0.0.0:8021/api/categories/"
 
# Set the headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI2OTE3MTIxLCJpYXQiOjE3MjQzMjUxMjEsImp0aSI6IjM1OTllZmZjYmUwODRjZmJiYjZlMDI0NDg4YmEzN2UwIiwidXNlcl9pZCI6IjM0ZWU5NDJjLWJiY2ItNDYxNS1hY2QxLWRkYTlkMDI1NDkzOCJ9.YFEjKujbSPuJbZBtZikACOMi_rEmAQXu_j3lj5DRlO4"
}
 
data = []
for i in range(100000):
    category_id = f"780dc1a7-60ed-4893-9719-8b09fd02dc{i+11}"
    category_name = f"Category {i+1}"
    data.append({"category_id": category_id, "category_name": category_name})
 
 
# Convert data to JSON format
json_data = json.dumps(data)
 
# Send the POST request
response = requests.post(url, data=json_data, headers=headers)
 
# Print the response
print("Response Status Code:", response.status_code)
print("Response Text:", response.text)
 
# Check the response status code
if response.status_code == 201:
    print("Data sent successfully!")
else:
    print("Error sending data. Status code:", response.status_code)
