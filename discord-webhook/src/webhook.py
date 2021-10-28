import aiohttp, asyncio
from json import dumps

class Webhook:
    def __init__(self, token: str) -> None:
        self._baseurl = "https://discord.com/api/v9/"
        self._token = token
        self._header = {'Authorization': f'Bot {self._token}'}
    
    async def create_webhook(self, channel_id: int, name: str):
        url = self._baseurl+f'channels/{channel_id}/webhooks'
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=self._header, json={'name': name}) as res:
                print(await res.json())
                return await res.json()

    async def post_webhook(self, webhook, message, embed=None):
        
        url = self._baseurl+f'/webhooks/{webhook["id"]}/{webhook["token"]}'
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=self._header, json={'content': message}) as res:
                print(await res.json())
                return await res.json()



async def main():
    webhook = Webhook('NzY4MDMyNDI1NTY1MDkzODk4.X46j7w.ZCoqMj-FmOzl3sybmMDvM1EwMSs')
    await webhook.post_webhook(await webhook.create_webhook(892450184234139688, 'Jessie'), 'hello')

asyncio.run(main())

            

