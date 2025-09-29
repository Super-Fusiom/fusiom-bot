import discord
from discord.ext import commands
from dotenv import dotenv_values
from profiler.github import fetch_github_user

dotenv_values = dotenv_values(".env")
bot_token = dotenv_values["BOT_TOKEN"]
channel_id = dotenv_values["CHANNEL_ID"]
intents = discord.Intents.all()
intents.message_content = True


bot = commands.Bot(command_prefix="!", intents=intents)


@bot.listen('on_message')
async def message_handler(message: discord.Message) -> None:
    if message.author == bot.user:
        return

    if message.channel.id == int(channel_id):
        await message.channel.send("Yurr")


@bot.tree.command(name="scout", description="Scout a github user")
async def scout(interaction: discord.Interaction, username: str) -> None:
    await interaction.response.send_message(fetch_github_user(username))


@bot.event
async def on_ready() -> None:
    print(f"{bot.user} has connected to Discord!")
    try:
        await bot.tree.sync()
        print("Synced commands")
    except Exception as e:
        print(e)


def main() -> None:
    bot.run(bot_token)


if __name__ == "__main__":
    main()
