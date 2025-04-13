import discord
from discord.ext import commands
import math 
import sqlite3
import random

class LevelSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return 
        
        connection = sqlite3.connect("cogs/levels.db")
        cursor = connection.cursor()
        guild_id = message.guild.id 
        user_id = message.author.id
        query = "SELECT * FROM MEMBERS WHERE guild_id = ? AND user_id = ?"
        cursor.execute(query, (guild_id, user_id))
        result = cursor.fetchone()

        if result is None:
            current_level = 0
            xp = 0
            level_up_xp = 0
            query = "INSERT INTO MEMBERS (guild_id, user_id, level, xp, level_up_xp) VALUES (?,?,?,?,?)"
            cursor.execute(query, (guild_id, user_id, current_level, xp, level_up_xp))

        else:
            current_level = result[2]
            xp = result[3]
            level_up_xp = result[4]
            xp += random.randint(10, 25)

        
        if xp >= level_up_xp:
            current_level += 1
            new_level_up_xp = math.ceil(5* (current_level**2) + 50 * current_level+100)
            await message.channel.send(f"{message.author.mention} has leveled up to level {current_level}! Keep it up!")
            query = "UPDATE MEMBERS SET level = ?, xp = ?, level_up_xp = ? WHERE guild_id = ? and user_id = ?"
            cursor.execute(query, (current_level, xp, new_level_up_xp, guild_id, user_id))


        cursor.execute("UPDATE MEMBERS SET xp = ? WHERE guild_id = ? AND user_id = ?", (xp, guild_id, user_id))
        connection.commit()
        connection.close()
            
async def setup(bot):
    await bot.add_cog(LevelSystem(bot))