from discord.ext import commands
import discord
import sqlite3 as sql
import random
import datetime

class economy(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='register')
    async def register(self, ctx):
        db = sql.connect('economydb.db')
        cursor = db.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS users(username,id,balance)')
        cursor.execute('CREATE TABLE IF NOT EXISTS workcooldown(userid,expiredate)')
        cursor.execute('CREATE TABLE IF NOT EXISTS betcooldowns (memberid, expiration)')
        cursor.execute("SELECT * FROM users")
        valid = cursor.fetchall()
        tmplist = []
        if valid == []:
            print('empty')
            db = sql.connect('economydb.db')
            cursor = db.cursor()
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
        else:
            for i in valid:
                tmplist.append(i[1])
            if ctx.author.id in tmplist:
                await ctx.send('you are already registered in the database')
                print('alr in')
            elif ctx.author.id not in tmplist:
                print('not in')
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
    async def bal(self, ctx, user : discord.Member = None):
        db = sql.connect('economydb.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users")
        valid = cursor.fetchall()
        for i in valid:
            if i[1] == user.id:
                    embed = discord.Embed(color=7377330,
                                        title=user.name + '\'s balance',
                                        description='**Balance**\n`' +
                                        str(i[2]) + '`')
                    await ctx.send(embed=embed)
                    cursor.close()
                    db.close()


    @commands.command(name='work')
    async def work(self, ctx):
        db = sql.connect('economydb.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users")
        valid = cursor.fetchall()
        listofworks = ['you have killed hitler and won ', 'some random rich nigga saw you at the street and gave you ', 'you sold your gpu and got ', 'you have joined filippas and stam in robbing a fucking bank and got ', 'you became a prostitute and gained ', 'super thought you were yasmin and gave you ', 'you worked for andrew tate for 30 minutes and he generousely gave you ']
        for i in valid:
            if i[1] == ctx.author.id:
                currenttime = datetime.datetime.now()
                plusonehour = currenttime + datetime.timedelta(hours=1)
                tmplist = []
                cursor.execute("SELECT * FROM workcooldown")
                allcooldowns = cursor.fetchall()
                for x in allcooldowns:
                    tmplist.append(x[0])
                if ctx.author.id in tmplist:
                    if datetime.datetime.strptime(x[1], '%Y-%m-%d %H:%M:%S.%f') < datetime.datetime.now():
                        cursor.execute('DELETE FROM workcooldown WHERE userid ='+ str(ctx.author.id))
                        x = random.randrange(0, 100)
                        if x < 1:
                            amount = random.choice(range(10000, 100000))
                            await ctx.send(random.choice(listofworks) + str(amount))
                            print(amount)
                        if x < 30 and not x<1:
                            amount = random.choice(range(1000, 2000))
                            await ctx.send(random.choice(listofworks) + str(amount))
                            print(amount)
                            print('lowe prob')
                        if x < 60 and not x< 30 and not x<1:
                            amount = random.choice(range(551, 900))
                            await ctx.send(random.choice(listofworks) + str(amount))
                            print(amount)
                            print('medium prob')
                        if x < 100 and not x < 60 and not x< 30 and not x<1:
                            amount = random.choice(range(200, 550))
                            await ctx.send(random.choice(listofworks) + str(amount))
                            print(amount)
                            print('highest prob')
                        cursor.execute('SELECT * FROM users WHERE id ='  + str(ctx.author.id))
                        selecteduser = cursor.fetchone()
                        total = selecteduser[2] + amount
                        cursor.execute('UPDATE users SET balance = :total WHERE id = :authorid',
                        {
                            'total' : amount,
                            'authorid' : ctx.author.id
                        })
                        cursor.execute('INSERT INTO workcooldown VALUES (:userid,:plusonehour)',
                        {
                            'userid' : ctx.author.id,
                            'plusonehour' : plusonehour
                        })
                        db.commit()
                    elif datetime.datetime.strptime(x[1], '%Y-%m-%d %H:%M:%S.%f')  > datetime.datetime.now():
                        await ctx.send('you are on cooldown')
                        cursor.close()
                        db.close()
                elif ctx.author.id not in tmplist:
                    x = random.randrange(0, 100)
                    if x < 1:
                        amount = random.choice(range(10000, 100000))
                        await ctx.send(random.choice(listofworks) + str(amount))
                        print(amount)
                    if x < 30 and not x<1:
                        amount = random.choice(range(1000, 2000))
                        await ctx.send(random.choice(listofworks) + str(amount))
                        print(amount)
                        print('lowe prob')
                    if x < 60 and not x< 30 and not x<1:
                        amount = random.choice(range(551, 900))
                        await ctx.send(random.choice(listofworks) + str(amount))
                        print(amount)
                        print('medium prob')
                    if x < 100 and not x < 60 and not x< 30 and not x<1:
                        amount = random.choice(range(200, 550))
                        await ctx.send(random.choice(listofworks) + str(amount))
                        print(amount)
                        print('highest prob')

                    cursor.execute('SELECT * FROM users WHERE id ='  + str(ctx.author.id))
                    selecteduser = cursor.fetchone()
                    total = selecteduser[2] + amount
                    cursor.execute('UPDATE users SET balance = :total WHERE id = :authorid',
                    {
                        'total' : total,
                        'authorid' : ctx.author.id
                    })
                    cursor.execute('INSERT INTO workcooldown VALUES (:userid,:plusonehour)',
                    {
                        'userid' : ctx.author.id,
                        'plusonehour' : plusonehour
                    })

                    db.commit()
                    cursor.close()
                    db.close()
    @commands.command(name='bet')
    async def bet(self, ctx, amountbet):
        db = sql.connect('economydb.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users')
        allusers = cursor.fetchall()
        for i in allusers:
            if i[1] == ctx.author.id:
                cursor.execute('SELECT * FROM betcooldowns')
                allcools = cursor.fetchall()
                tmplist = []
                for i in allcools:
                    tmplist.append(allcools[0])

                if random.randrange(0, 100) < 50:
                    if i[2] > int(amountbet):

                        newbal = int(i[2]) + int(amountbet)
                        cursor.execute('UPDATE users SET balance = :newbal WHERE id = :userid',
                        {
                            'newbal' : newbal,
                            'userid' : i[1]
                        })

                        db.commit()
                        cursor.close()
                        db.close()

                        await ctx.send('you have won '+ str(amountbet))
                        currenttime = datetime.datetime.now()
                        nexttime = datetime.timedelta(minutes = 5) + currenttime
                        cursor.execute('INSERT INTO  betcooldowns VALUES (:userid,:expirationdate)',
                        {
                            'userid' : ctx.author.id,
                            'expirationdate' : nexttime
                        })
                    else:
                        await ctx.send('you betted more money than you have!')
                        cursor.close()
                        db.close()



                else:
                    if i[2] > int(amountbet):
                        newbal = int(i[2]) - int(amountbet)
                        cursor.execute('UPDATE users SET balance = :newbal WHERE id = :userid',
                        {
                            'newbal' : newbal,
                            'userid' : i[1]
                        })
                        currenttime = datetime.datetime.now()
                        nexttime = datetime.timedelta(minutes = 5) + currenttime
                        cursor.execute('INSERT INTO  betcooldowns VALUES (:userid,:expirationdate)',
                        {
                            'userid' : ctx.author.id,
                            'expirationdate' : nexttime
                        })
                        db.commit()
                        cursor.close()
                        db.close()

                        await ctx.send('you have lost '+ str(amountbet))
                    else:
                        await ctx.send('you betted more money than you have!')
                        cursor.close()
                        db.close()

async def setup(bot):
    await bot.add_cog(economy(bot))
