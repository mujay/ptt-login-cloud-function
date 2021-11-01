# ptt-login-cloud-function

放置在 gcp cloud function 上即可以實現以 HTTP Request 自動帳號登入及登出

環境為 python3.9

## request json sample 
```json
{
    "username":"{username}",
    "password":"{password}"
}