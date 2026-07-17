def test_auth_home(test_client):

    response = test_client.get("/auth/")

    assert response.status_code == 200
