def test_cred(login_username, login_password):
    assert login_username == "admin"
    assert login_password == "123456"