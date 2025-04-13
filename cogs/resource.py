import discord
from discord.ext import commands
from discord import app_commands


class ResourceSender(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
    @app_commands.command(name="services", description="Get links for all platform services typically used by students")
    async def send_services(self, interaction: discord.Interaction, platform: str):
        websites = {
            "moodle": "https://online.upr.edu/",
            "portal viejo": "https://home.uprm.edu/",
            "portal nuevo" : "https://portal.upr.edu/",
            "github" : "https://github.com/logout"
        }
        
        if platform.lower() in websites:
            await interaction.response.send_message(f"{websites[platform.lower()]}")
        else:
            await interaction.response.send_message("Service not found")

    @app_commands.command(name="tickets", description="Get links to specific ticket-related services")
    async def send_tickets(self, interaction: discord.Interaction, platform: str):
        websites = {
            "asistencia economica" : "https://oficinavirtual.uprm.edu/",
            "ajustes":  "https://ajustes.uprm.edu",
            "ece" : "https://ece.uprm.edu/instrucciones-para-solicitar-cuentas-yo-tarjetas/",
            "pescera" : "https://www.uprm.edu/inin/access-card-for-the-study-room/"
        }

        if platform.lower() in websites:
            await interaction.response.send_message(f"{websites[platform.lower()]}")
        else:
            await interaction.response.send_message("Website not found.")
        

async def setup(bot):
    await bot.add_cog(ResourceSender(bot))