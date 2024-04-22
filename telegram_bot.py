import requests

chat_id = "chat_id"
token = "token"
msg = "kdlkdldkl"
message = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"

response = requests.get(message)