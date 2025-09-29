import discord
from discord.ext import commands
from dotenv import dotenv_values
from profiler.github import fetch_github_repos, fetch_github_all

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


@bot.tree.command(name="scout",
                  description="Scout a user will all of their info."
                  )
async def scout(interaction: discord.Interaction, username: str) -> None:
    await interaction.response.send_message(fetch_github_all(username))


@bot.tree.command(name="scout-repos",
                  description="Scout a github user with their repos."
                  )
async def scout_repos(interaction: discord.Interaction, username: str) -> None:
    await interaction.response.send_message(fetch_github_repos(username))


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
