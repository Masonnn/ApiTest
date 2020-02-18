from common import Common

# 登录页路由
uri = '/login'
# username变量存储用户名参数
username = 'criss'
# password变量存储密码参数
password = 'criss'
# 拼凑body的参数
payload = 'username=' + username + '&password=' + password
comm = Common()
response_login = comm.post(uri, params=payload)
print('Response内容：' + response_login.text)
