import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    intents.message_content =  True

    bot = commands.Bot(command_prefix="!", intents = intents)

    @bot.event 
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

    @bot.command()    
    async def bartend(ctx):
        await ctx.send('hi! would you like to take a look at our !menu?')

    @bot.command()    
    async def menu(ctx):
        await ctx.send("Please have a look at our fine selection of beverages")
        await ctx.send("!Tequila - 1$\n!Mojito (with lime) - 2$\n!Sweet_Mimosa - 3$\n!Pina_Colada - 5$\n!Margarita - 4$")

    #start of menu commands, will make more efficient soon    
    @bot.command()
    async def Tequila(ctx):
        with open('Tequila.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    @bot.command()
    async def Mojito(ctx):
        with open('Mojito.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    @bot.command()
    async def Sweet_Mimosa(ctx):
        with open('Sweet_Mimosa.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    @bot.command()
    async def Pina_Colada(ctx):
        with open('Pina_Colada.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    @bot.command()
    async def Margarita(ctx):
        with open('Margarita.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    



    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()