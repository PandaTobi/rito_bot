import discord
import random
import nest_asyncio

nest_asyncio.apply()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
            
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        
        voicelines = ["Mundo (slurps) smash!", "Mundo too strong for you!", 
                      "Rawr!", "Mundo will go where he pleases!", "Come to Mundo!",
                      "Blah!", "Mundo go this way!"]
        if message.content.startswith('!mundo'):
            await message.channel.send(random.choice(voicelines))
        elif message.content.startswith('!owner'):
            await message.channel.send('mUnDoOoOoOo ThE gOdOoOoOoO#4918')
        elif message.content.startswith('!rivershen'):
            await message.channel.send('pftt, river shen? more like  r i v e r  s h e n')
        elif message.content.startswith('!suckcock'):
            await message.channel.send("What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little 'clever' comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo.")
        elif message.content.startswith('!rito_plz'):
            commands = ['!mundo', '!owner', '!rivershen', '!suckcock', '!patch']
            for command in commands:
                await message.channel.send(command)
        elif message.content == '!patch':
            await message.channel.send('https://na.leagueoflegends.com/en/news/game-updates/patch/patch-917-notes')
        else:
            if random.randint(1,30) >= 28:
                await message.channel.send('Curious about my buddy RhythmBot? Type !help in chat for a list of his commands! As for me, just type !rito_plz, for a list of my current commands!')

    
            
client = MyClient()
client.run('NjE0ODM2NjU1MTM5ODQ4MTk.XWFS4A.kVuWg7-lGfxrXPGLxkM8FshxJV8')
