import requests

WEBHOOK_URL = "https://discordapp.com/api/webhooks/1423323990172241991/_b7MceMZCOfpGSUQdxtNxa3cJeyp5Zn1W66l_UmXdwxAzdIglYVJXep49BxA36scr1OD"

data = {
    "content": "Hello, this is a test message from the webhook!"
}

response = requests.post(WEBHOOK_URL, json=data)

if response.status_code == 204:
    print("✅ Notification sent successfully!")
else:
    print(f"❌ Failed to send notification: {response.status_code}")