import asyncio
from whatsapp import Client
from features import *

class ClaudeMod:
    def __init__(self):
        self.client = None

    async def connect(self, connection_method='qr'):
        if connection_method == 'qr':
            self.client = await Client.connect_with_qr()
        elif connection_method == 'pairing_code':
            pairing_code = input("Enter the pairing code: ")
            self.client = await Client.connect_with_pairing_code(pairing_code)
        else:
            raise ValueError("Invalid connection method")

    async def start(self):
        @self.client.on_message()
        async def handle_message(message):
            if message.text.startswith('!'):
                command = message.text.split()[0][1:]
                if command == 'help':
                    await help_command(message)
                elif command == 'joke':
                    joke = await jokes_maker()
                    await message.reply(joke)
                elif command == 'weather':
                    city = message.text.split(maxsplit=1)[1]
                    weather_info = await weather(city)
                    await message.reply(weather_info)
                # Add more command handlers here
            
            await handle_group_message(message)

        print("CLAUDE MOD is now running!")
        await self.client.run()

if __name__ == "__main__":
    bot = ClaudeMod()
    connection_method = input("Choose connection method (qr/pairing_code): ")
    asyncio.run(bot.connect(connection_method))
    asyncio.run(bot.start())