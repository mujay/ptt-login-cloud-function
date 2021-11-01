import time
from PyPtt import PTT


def loginAndLogOut(username, password):
    PTTBot = PTT.API()

    # 登入
    PTTBot.login(username, password)
    PTTBot.log('登入成功')

    # 等待
    time.sleep(9)

    # 登出
    PTTBot.logout()
    PTTBot.log('登出成功')

    return 'success'
