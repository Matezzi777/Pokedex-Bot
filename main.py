import discord
import discord.ui
from classes import Bot, BotEmbed, SuccessEmbed, ErrorEmbed
from config import TOKEN, SERVERS

bot = Bot()

#################### EVENTS ####################
@bot.event
async def on_ready():
	return (print("\nPokedex connected and ready to Catch'em all!\n"))

################### COMMANDS ###################
@bot.slash_command(guild_ids=SERVERS, name="ping", description="PONG!")
async def ping(interaction: discord.Interaction) -> None:
	return await interaction.response.send_message(embed=SuccessEmbed(title="PONG !").remove_footer())

##################### RUN ######################
bot.run(TOKEN)