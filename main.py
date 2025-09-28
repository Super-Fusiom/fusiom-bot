import discord
from dotenv import dotenv_values

dotenv_values = dotenv_values(".env")
bot_token: str = dotenv_values["BOT_TOKEN"]
channel_id = dotenv_values["CHANNEL_ID"]
intents = discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)


@client.event
async def on_ready() -> None:
    print(f"{client.user} has connected to Discord!")


@client.event
async def on_message(message: discord.Message) -> None:
    if message.author == client.user:
        return

    if message.channel.id == int(channel_id):
        await message.channel.send("Yurr")


def main() -> None:
    client.run(bot_token)


if __name__ == "__main__":
    main()
