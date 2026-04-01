def test_get_user_404(client):

    # Teste de Recuperação
    get_response = client.get("/users/1")
    assert get_response.status_code == 404 

def test_create_and_get_user_and_delete_user(client):
    data = {
        'name': 'nome',
        'email': 'email@email.com'
    }
    post_response = client.post("/users", json=data)
    assert post_response.status_code == 201

    dados = post_response.get_json()
    get_respose = client.get(f"users/{dados["id"]}")
    assert get_respose.status_code == 200

    delete_response = client.delete(f"users/{dados["id"]}")
    assert delete_response.status_code == 204

def test_create_and_delete_user(client):
    data = {
        'name': 'nome',
        'email': 'email@email.com'
    }
    post_response = client.post("/users", json=data)
    assert post_response.status_code == 201

    dados = post_response.get_json()

    delete_response = client.delete(f"users/{dados["id"]}")
    assert delete_response.status_code == 204

def test_create_two_users_and_list_and_delete_both_users(client):
    data1 = {
        'name': 'nome1',
        'email': 'email1@email.com'
    }
    post_response1 = client.post("/users", json=data1)
    assert post_response1.status_code == 201

    data2 = {
        'name': 'nome2',
        'email': 'email2@email.com'
    }
    post_response2 = client.post("/users", json=data2)
    assert post_response2.status_code == 201

    get_respose = client.get("/users")
    assert get_respose.status_code == 200

    dados1 = post_response1.get_json()
    dados2 = post_response2.get_json()

    delete_response = client.delete(f"users/{dados1["id"]}")
    assert delete_response.status_code == 204

    delete_response = client.delete(f"users/{dados2["id"]}")
    assert delete_response.status_code == 204