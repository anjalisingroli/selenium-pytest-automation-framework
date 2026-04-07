from api.api_helper import update_post


# Test case to verify PUT API for updating a post
def test_update_post():

    payload = {
        "title": "Updated Title",
        "body": "Updated body",
        "userId": 1
    }

    response = update_post(1, payload)

    # Validate update success
    assert response.status_code == 200