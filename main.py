import discord
import random
import keep_alive
import list
import ids
import discord.ext
import uWu
import presence

keep_alive.keep_alive()
bot = discord.Client()

@bot.event
async def on_ready():
  print('-' * 10)
  print('logged in as')
  print(bot.user.name)
  print(bot.user.id)
  print('-' * 10)  

  await bot.change_presence(status=presence.statu, activity=presence.activit)

@bot.event
async def on_message(message):
  
  #my shortcut commands
    msg = message.content.startswith
    msgsend = message.channel.send
    content = message.content
  
    if message.author == bot.user:
      return

    if msg('test'): 
      await msgsend('testing 123')
      #if your message starts with 'test', then the bot will reply with 'testing 123' ont he same channel

    if 'testing' in content:
      await msgsend('it is working!')
      #if your message contains 'testing' anywhere, bot will reply with the following.

    if msg('give me a motivational quote'):
      await msgsend(random.choice(list.movitational_quotes))
      #this is reply back with a random motivational quote from the lists

    if 'uwu' in content:
      uwutext = uWu.generateuwu(content)
      newuwu = random.choice(list.u_wu)
      uwued = uwutext.replace(" uwu " and "uwu " and " uwu" and "uwu", (' ' + newuwu + ' '))
      await msgsend(uwued)
      #yes this exists


  
bot.run(ids.token)