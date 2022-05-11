from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Your bot is alive!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()

'''
this is to keep the bot running 24/7 using https://uptimerobot.com/
when you run the repl, you have to take the link of the website created and add it to uptimerobot
'''