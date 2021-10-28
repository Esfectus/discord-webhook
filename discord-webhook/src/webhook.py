import aiohttp
import asyncio
from json import dumps


class Webhook:
    """Webhook Class

    """

    def __init__(self, token: str) -> None:
        self._baseurl = "https://discord.com/api/v9/"
        self._token = token
        self._header = {'Authorization': f'Bot {self._token}'}

    
    async def get_channel_webhooks(self, channel_id):
        """Returns a list of channel webhook objects. Requires the MANAGE_WEBHOOKS permission.
        """
        url = self._baseurl+f'channels/{channel_id}/webhooks'
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self._header) as res:
                return await res.json()


    async def get_guild_webhooks(self, guild_id):
        """Returns a list of guild webhook objects. Requires the MANAGE_WEBHOOKS permission.
        """
        url = self._baseurl+f'guilds/{guild_id}/webhooks'
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self._header) as res:
                return await res.json()

    async def create_webhook(self, channel_id: int):
        """Creates Webhook.
        Sends a POST request to the discord API and returns a webhook object as json.

        Args:
            channel_id: Snowflake ID of a Discord Channel.
            name: User name of the webhook message.
        Returns:
            Returns aiohttp response

        """

        url = self._baseurl+f'channels/{channel_id}/webhooks'
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=self._header, json={'name': 'Webhook'}) as res:
                return await res.json()


    async def modify_webhook(self, webhook_id: int, name: str, channel_id: int):
        url = self._baseurl+f'webhooks/{webhook_id}'
        print(url)
        async with aiohttp.ClientSession() as session:
            async with session.patch(url, headers=self._header, json={'name': name, 'channel_id': channel_id}) as res:
                return await res.json()



    async def post_webhook(self, webhook: dict, params: dict):
        """Sends the webhook.
        Posts/sends the webhook in a Discord channel.



        Args:
            webhook: Dict with webhook object.
            params: For detailed explaination check, https://discord.com/developers/docs/resources/webhook#execute-webhook-jsonform-params
        Returns:
            Returns aiohttp response
        """

        url = self._baseurl+f'/webhooks/{webhook["id"]}/{webhook["token"]}'
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=self._header, json=params) as res:
                return res
