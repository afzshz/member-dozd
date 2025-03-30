import json
from telethon import TelegramClient, events
api_id = int(input("api id: "))
api_hash = str(input("api hash: "))
phone = str(input("phone: "))
client = TelegramClient("session_name", api_id, api_hash)
json_file = 'users.json'
def load_users():
    try:
        with open(json_file, 'r') as file:
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        users = []
    if not isinstance(users, list):
        users = []
    return users
def save_users(users):
    with open(json_file, 'w') as file:
        json.dump(users, file, ensure_ascii=False, indent=4)
@client.on(events.NewMessage)
async def handle_new_message(event):
    if event.is_group:
        user_id = event.sender_id
        users = load_users()
        if user_id not in users:
            users.append(user_id)
            save_users(users)
            sender = await event.get_sender()
            await client.send_message(sender,
                                      '𓄂ꪴꪰ𝗪𝗲𝗹𝗰𝗼𝗺𝗲༆𝗣𝗼𝘄𝗲𝗿𓆃\n'
                                      '☻𝗙𝗮𝗵𝗮𝘀𝗵𝗶⇨𝗕𝗮𝗻🚫☻𝗠𝗲𝗺𝗯𝗲𝗿 𝗗𝗼𝘇𝗱𝗶⇨𝗕𝗮𝗻🚫\n'
                                      '☻𝗹𝗶𝗻𝗸⇨𝗕𝗮𝗻🚫\n'
                                      '𝗖𝗮𝗹𝗹➠²⁴𝗛✆🩹\n'
                                      '𝗚𝗮𝗺𝗲➠²⁴𝗛🧩\n'
                                      '❥𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐆𝐔𝐘𝐒🫵\n'
                                      '𝗹𝗶𝗻𝗸➠https://t.me/+pLIq8-z3PGxjMDA0'
                                      )
print("ربات آماده است...")
client.start()
client.run_until_disconnected()