import discord
from discord.ext import commands
import coro 

# Prefix du bot et client 
bot = commands.Bot(command_prefix='>')
client = discord.Client()

# Ping > Pong 
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# Infos sur un serveur 
@bot.command()
async def InfoServeur(ctx):
	serveur = ctx.guild
	TextChannels = len(serveur.text_channels)
	VocChannels = len(serveur.voice_channels)
	Description = serveur.description
	personnes = serveur.member_count
	serveur = serveur.name
	message = f"Le serveur **{serveur}** contient *{personnes}* personnes ! \nLa description du serveur est {Description}. \nCe serveur possède {TextChannels} salons écrits et {VocChannels} salons vocaux."
	await ctx.send(message)

# Supprimer des messages 
@bot.command(name="del")
async def delete(ctx, number: int):
    messages = await ctx.channel.history(limit=number + 1).flatten()
    
    for each_message in messages:
        await each_message.delete()

# Aide 
@bot.command()
async def jeanne_ausecours(ctx):
	helping = "HELP :\n>Ping : Pong\n>InfoServeur : Avoir quelques infos sur un serveur\n>del : Supprimer des messages"
	await ctx.send(helping)

# Message de bienvenue 
@client.event(coro)  
async def on_member_join(member):
    print(f"{member.display_name} est arrivé a destination de la Pirate Cove !")

# Token du bot 
bot.run('BOT TOKEN HERE')
client.run("BOT TOKEN HERE")
