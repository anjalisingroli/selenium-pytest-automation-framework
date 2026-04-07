import requests
from config.config import API_BASE_URL


# Fetch a post by ID
def get_post(post_id):
    url = f"{API_BASE_URL}/posts/{post_id}"
    return requests.get(url)


# Create a new post using POST request
def create_post(payload):
    url = f"{API_BASE_URL}/posts"
    return requests.post(url, json=payload)


# Update an existing post using PUT request
def update_post(post_id, payload):
    url = f"{API_BASE_URL}/posts/{post_id}"
    return requests.put(url, json=payload)


# Delete a post using DELETE request
def delete_post(post_id):
    url = f"{API_BASE_URL}/posts/{post_id}"
    return requests.delete(url)