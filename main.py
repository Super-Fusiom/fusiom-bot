import discord
from dotenv import dotenv_values


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user}")

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")


dotenv_values = dotenv_values(".env")
bot_token: str = dotenv_values["BOT_TOKEN"]

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)


# For python style coding -> Use main
def main() -> None:
    client.run(dotenv_values["BOT_TOKEN"])


if __name__ == "__main__":
    main()
