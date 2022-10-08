import discord
import asyncpraw
from discord.ext import commands
from random import choice
from requests import get
from os import getenv
from dotenv import load_dotenv

load_dotenv('.env')
bot = commands.Bot(command_prefix='p#', intents=discord.Intents.all())
allcommands = ['cat', 'help', 'say']

@bot.event
async def on_ready():
	print("Bot is running!")
	game=discord.Game("with my balls.")
	await bot.change_presence(status=discord.Status.idle,activity=game)

@bot.command(name='cat')
async def catpic(ctx):
	reddit = asyncpraw.Reddit(
	client_id=getenv('CLIENTID'),
	client_secret=getenv('TOKENSECRET'),
	password=getenv('REDDITPASS'),  
	user_agent="SmokBot",
	username="BigSmug101"
	)
	chosensubs = []
	sub = await reddit.subreddit('cat')
	submissions = sub.hot()

	async for i in submissions:
		if i.url[-4:] == '.jpg' or i.url[-4:] == '.png':
			chosensubs.append(i.url)

	await ctx.send(choice(chosensubs))

@bot.command(name='nsfw')
async def catpic(ctx):
	if ctx.channel.nsfw:
		reddit = asyncpraw.Reddit(
		client_id=getenv('CLIENTID'),
		client_secret=getenv('TOKENSECRET'),
		password=getenv('REDDITPASS'),  
		user_agent="SmokBot",
		username="BigSmug101"
		)
		chosensubs = []
		sub = await reddit.subreddit('nsfw')
		submissions = sub.hot()

		async for i in submissions:
			if i.url[-4:] == '.jpg' or i.url[-4:] == '.png':
				chosensubs.append(i.url)

		await ctx.send(choice(chosensubs))
	
@bot.command(name='boobs')
async def catpic(ctx):
	if ctx.channel.nsfw:
		reddit = asyncpraw.Reddit(
		client_id=getenv('CLIENTID'),
		client_secret=getenv('TOKENSECRET'),
		password=getenv('REDDITPASS'),  
		user_agent="SmokBot",
		username="BigSmug101"
		)
		chosensubs = []
		sub = await reddit.subreddit('boobs')
		submissions = sub.hot()

		async for i in submissions:
			if i.url[-4:] == '.jpg' or i.url[-4:] == '.png':
				chosensubs.append(i.url)

		await ctx.send(choice(chosensubs))
@bot.command(name='gonewild')
async def catpic(ctx):
	if ctx.channel.nsfw:
		reddit = asyncpraw.Reddit(
		client_id=getenv('CLIENTID'),
		client_secret=getenv('TOKENSECRET'),
		password=getenv('REDDITPASS'),  
		user_agent="SmokBot",
		username="BigSmug101"
		)
		chosensubs = []
		sub = await reddit.subreddit('gonewild')
		submissions = sub.hot()

		async for i in submissions:
			if i.url[-4:] == '.jpg' or i.url[-4:] == '.png':
				chosensubs.append(i.url)

		await ctx.send(choice(chosensubs))

@bot.command(name='helpp')
async def helpq(ctx):
	embed = discord.Embed(title='Help', color=7640463, description='**help**\n `i hate niggers` `ok` `kala` \n **tiri** \n `ok` __tiri__ #lka _ok_ ')
	await ctx.send(embed=embed)
            
@bot.command(name='8ball')
async def ball(ctx):
	req = get('https://8ball.delegator.com/magic/JSON/' + ctx.message.content[8:]).text
	embed = discord.Embed(title=req['magic']['type'], description=req['magic']['answer'])
	await ctx.send(embed=embed)

@bot.command(name='say')
async def goodmorning(ctx):
	if ctx.message.reference:
		original = await ctx.fetch_message(ctx.message.reference.message_id)
		await original.reply(ctx.message.content[6:])
	elif ctx.message.content[6:] == '':
		await ctx.send('nothing to say')
	else:
		await ctx.send(ctx.message.content[6:])
        
bot.run(getenv('TOKEN'))


