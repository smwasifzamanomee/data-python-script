import requests
import json

# API endpoint
url = 'http://0.0.0.0:8021/api/delete-categories/'

# Set the headers
headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'insomnia/9.2.0',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI2OTE5NTY0LCJpYXQiOjE3MjQzMjc1NjQsImp0aSI6IjlkODk1MGU2Yzg3MjRkNzI4NjNiNDllMWY2ODZhYTYzIiwidXNlcl9pZCI6IjM0ZWU5NDJjLWJiY2ItNDYxNS1hY2QxLWRkYTlkMDI1NDkzOCJ9.gOGdYzeCLoXk1O55uic1-t__zf5AM1TanzipKqer1nQ'
}

# Number of categories to delete in each batch
batch_size = 5000

# Total number of categories to delete
total_categories = 5000  # Adjust this as needed

# Function to delete categories in batches
def delete_categories():
    for batch_start in range(0, total_categories, batch_size):
        category_ids = []

        # Collect category IDs for the current batch
        for i in range(batch_start, min(batch_start + batch_size, total_categories)):
            category_id = f'580dc1a7-60ed-4893-9719-8b09fd02dc{i + 11}'
            category_ids.append(category_id)

        # Prepare the request data
        data = {
            'category_ids': category_ids
        }

        # Send the DELETE request
        try:
            response = requests.delete(url, headers=headers, data=json.dumps(data))
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            print(f"Batch from {batch_start + 1} to {min(batch_start + batch_size, total_categories)} deleted successfully!")
            print(response.json())  # Print the response data
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred for batch {batch_start + 1} to {min(batch_start + batch_size, total_categories)}: {http_err}")
        except Exception as err:
            print(f"An error occurred for batch {batch_start + 1} to {min(batch_start + batch_size, total_categories)}: {err}")

# Execute the deletion
delete_categories()