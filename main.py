import os
import time
import datetime
import requests
import pyrogram

user_session_string = os.environ.get("user_session_string")
bots = [i.strip() for i in os.environ.get("bots").split(' ')]
bot_owner = os.environ.get("bot_owner")
update_channel = os.environ.get("update_channel")
status_message_id = int(os.environ.get("status_message_id"))
api_id = int(os.environ.get("api_id"))
api_hash = os.environ.get("api_hash")

user_client = pyrogram.Client(
    user_session_string, api_id=api_id, api_hash=api_hash)

api_url = 'http://botsuniverse.live'
api_url2 = 'http://api-bu-v2.herokuapp.com'
api_url3 = 'http://apibu.herokuapp.com'
er = requests.get(api_url)
ew = requests.get(api_url2)
eww = requests.get(api_url3)
op = er.status_code
yu = ew.status_code
oo = eww.status_code

def main():
    with user_client:
        while True:
            print("[INFO] starting to check uptime..")
            edit_text = f"Our Bot's List & Their Status:\n\nNote: All Bot Status will Be Auto Checked\nIn 4 Hours\n\n"
            user_client.send_message(bot_owner, f'Starting To Check Bots..')
            user_client.send_message(-1001482059289, f'Starting To Check Bots..')
            for bot in bots:
                print(f"[INFO] checking @{bot}")
                msg = (f"[INFO] checking @{bot}")
                user_client.send_message(-1001482059289, msg) 
                snt = user_client.send_message(bot, '/start')

                time.sleep(30)

                msg = user_client.get_history(bot, 1)[0]
                if snt.message_id == msg.message_id:
                    print(f"[WARNING] @{bot} is down")
                    jio = (f"[WARNING] @{bot} is down")
                    user_client.send_message(-1001482059289, jio)
                    edit_text += f"💔 @{bot} AVAILABLITY: Not Avaliable\n\n"
                    user_client.send_message(bot_owner,
                                             f"💤 @{bot} Available: Nope..")

                else:
                    print(f"[INFO] all good with @{bot}")
                    kya = f"[INFO] all good with @{bot}"
                    user_client.send_message(-1001482059289, kya)
                    edit_text += f"❤ @{bot} AVAILABLITY: Yesh\n\n"
                user_client.read_history(bot)

            utc_now = datetime.datetime.utcnow()
            ist_now = utc_now + datetime.timedelta(minutes=30, hours=5)

            edit_text += f"__last checked on \n{str(utc_now)} UTC\n{ist_now} IST__"

            user_client.edit_message_text(update_channel, status_message_id,
                                         edit_text)
            print(f"[INFO] everything done! sleeping for 4 Hours")
            if op == 200:
                        user_client.send_message(bot_owner,
                                                 f"💤[Api Bu]({api_url3}) **Available**: Yep !",
                                                 parse_mode="md")
                    # Tell If Alive?
            else:
                user_client.send_message(bot_owner,
                                         f"❤ [Api Bu]({api_url3}) **Available**: Nope..",
                                         disable_web_page_preview=True,
                                         parse_mode="md")
            if yu == 200:
                user_client.send_message(bot_owner,
                                         f"💤[Api Bu V2]({api_url2}) Available: Yep...",
                                         disable_web_page_preview=True,
                                         parse_mode="md")
            
            else:
                user_client.send_message(bot_owner,
                                         f"❤ [Api Bu V2]({api_url2}) Available: Nope...",
                                         disable_web_page_preview=True,
                                         parse_mode="md")
            if oo == 200:
                user_client.send_message(bot_owner,
                                         f"💤[Bots Universe Website]({api_url}) Available: Yep...",
                                         disable_web_page_preview=True,
                                         parse_mode="md")
            
            else:
                        user_client.send_message(bot_owner,
                                                 f"❤ [Bots Universe Website]({api_url}) Available: Nope....",
                                                 disable_web_page_preview=True,
                                                 parse_mode="md")
                                                 
            user_client.send_message(bot_owner, f'Everything Done..\nNext Check Is After Four Hour')

            time.sleep(120 * 120)


main()
