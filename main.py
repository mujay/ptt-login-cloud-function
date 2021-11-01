import time
from PyPtt import PTT


def loginAndLogOut(request):
    PTTBot = PTT.API()

    username = request.get_json().get('username')
    password = request.get_json().get('password')

    # 登入
    PTTBot.login(username, password)
    PTTBot.log('登入成功')

    # 等待
    time.sleep(9)

    # 登出
    PTTBot.logout()
    PTTBot.log('登出成功')

    return 'success'
