from discord.ext import commands
import requests
import discord
import json
from random import choice

class cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='8ball')
    async def ball(self, ctx):
        req = requests.get('https://8ball.delegator.com/magic/JSON/' + ctx.message.content[8:]).text
        jsonresp = json.loads(req)
        embed = discord.Embed(title=ctx.message.content[8:], description=jsonresp["magic"]["answer"])
        await ctx.send(embed=embed)

    @commands.command(name='inspire')
    async def inspiration(self, ctx):
        req = requests.get('https://zenquotes.io/api/random').text
        jsonresp = json.loads(req)
        quote = jsonresp[0]['q']
        author = jsonresp[0]['a']
        await ctx.send(f'{quote}\n-{author}')

    @commands.command(name='guessing')
    async def guess(self, ctx):
        global gues
        global num
        num = choice(range(0, 10))
        gues = True
        await ctx.send('guessing game started')



async def setup(bot):
    await bot.add_cog(cmds(bot))




