import requests
import time

BOT_TOKEN = "7767171323:AAG-TVQALhoMCyu1xLWfc6XirE7BHY73edo"
CHAT_ID = "627879826"

def send_job():
    message = """💼 *Job Title:* Senior Python Developer  
🏢 *Company:* RemoteTech  
🌍 *Location:* Worldwide  
🧠 *Skills:* Python, Django, REST APIs  
🔗 [Apply Here](https://remoteok.com/remote-jobs/123456)
"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, data=payload)
    print(response.text)

if __name__ == "__main__":
    send_job()
