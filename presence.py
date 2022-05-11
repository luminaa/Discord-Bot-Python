import discord

activit = discord.Streaming(name="hi everyone", url="https://www.linkedin.com/in/rahual-r-56a6b4130/")
'''
pick one and paste it into the line above
you can tweak a little it too
discord.Game(name="a game")
discord.Streaming(name="My Stream", url=my_twitch_url)
discord.Activity(type=discord.ActivityType.listening, name="a song")
discord.Activity(type=discord.ActivityType.watching, name="a movie")
'''

statu = discord.Status.online
'''
pick one and paste it into the line above
discord.Status.online
discord.Status.offline
discord.Status.dnd                (do not disturb)
discord.Status.invisible
'''