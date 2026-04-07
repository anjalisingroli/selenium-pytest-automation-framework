from api.api_helper import get_post


# Test case to verify GET post API
def test_get_post():
    response = get_post(1)

    # Validate response status code
    assert response.status_code == 200