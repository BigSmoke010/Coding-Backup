from discord.ext import commands
import discord
import sqlite3 as sql


class economy(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='register')
    async def register(self, ctx):
        db = sql.connect('economydb.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users")
        valid = cursor.fetchall()
        for i in valid:
            if i[1] == ctx.author.id:
                await ctx.send('you are already registered in the database')
                cursor.close()
                db.close()
            else:
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS users (username,id,balance)')

                cursor.execute(
                    "INSERT INTO users (username,id,balance) VALUES (:name, :userid, 0)",
                    {
                        'name': ctx.author.name,
                        'userid': ctx.author.id
                    })
                await ctx.send('succesfully registered into the db')
                db.commit()
                cursor.close()
                db.close()

    @commands.command(name='fetchdb')
    async def fet(self, ctx):
        db = sql.connect('economydb.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users")
        valid = cursor.fetchall()
        print(valid)
        cursor.close()
        db.close()

    @commands.command(name='balance')
    async def bal(self, ctx):
        db = sql.connect('economydb.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users")
        valid = cursor.fetchall()
        for i in valid:
            if i[1] == ctx.author.id:
                embed = discord.Embed(color=7377330,
                                      title=ctx.author.name + '\'s balance',
                                      description='**Balance**\n`' +
                                      str(i[2]) + '`')
                await ctx.send(embed=embed)
        cursor.close()
        db.close()

    @commands.command(name='work')
    async def work(self, ctx):
        pass


async def setup(bot):
    await bot.add_cog(economy(bot))
