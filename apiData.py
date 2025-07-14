import requests

#GET

# url = "https://jsonplaceholder.typicode.com/posts/1"

# response = requests.get(url)

# print("Status: ",response.status_code)
# print("Data: ", response.json())

# POST

# url = "https://jsonplaceholder.typicode.com/posts"

# new_post = {
#     "title": "Mohit Decodes",
#     "body": "This is a new post created by Mohit.",
#     "userId": 1
# }

# response = requests.post(url, json=new_post)
# print("Status: ", response.status_code)
# print("Data: ", response.json())

# PUT

# url = "https://jsonplaceholder.typicode.com/posts/1"

# new_data = {
#     "title": "Updated Title",
#     "body": "This is the updated body of the post.",
#     "userId": 1
# }

# response = requests.put(url, json=new_data)

# print("Status: ", response.status_code)
# print("Data: ", response.json())

#PATCH

# url = "https://jsonplaceholder.typicode.com/posts/1"

# new_data = {
#     "title": "Updated Title Two"
# }

# response = requests.patch(url, json=new_data)
# print("Status: ", response.status_code)
# print("Data: ", response.json())

# DELETE

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.delete(url)

print("Status: ", response.status_code)
if response.status_code == 200:
    print("Post deleted successfully.")
else:
    print("Failed to delete the post.")