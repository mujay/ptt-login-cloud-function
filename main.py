from login_and_logout import loginAndLogOut


def main(request):
    username = request.get_json().get('username')
    password = request.get_json().get('password')

    loginAndLogOut(username, password)

    return 'success'
