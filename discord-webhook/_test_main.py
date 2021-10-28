import requests, asyncio
from json import dumps


class Webhook:
    """Webhook Class"""

    def __init__(self, token: str) -> None:
        self._baseurl = 'https://discord.com/api/v9'
        self._auth_header = {'Authorization': f'Bot {token}'}

    async def create_webhook(self, channel_id):
        """Creates a new webhook.
        Create a new webhook. Requires the MANAGE_WEBHOOKS permission. Returns a webhook object on success.
        """
        url = self._baseurl+f'/channels/{channel_id}/webhooks'

    async def get_channel_webhooks(self, channel_id):
        """Create a new webhook. Requires the MANAGE_WEBHOOKS permission. Returns a webhook object on success."""
        url = self._baseurl+f'/channels/{channel_id}/webhooks'

    async def get_guild_webhooks(self, guild_id):
        """Returns a list of guild webhook objects. Requires the MANAGE_WEBHOOKS permission."""
        url = self._baseurl+f'/guilds/{guild_id}/webhooks'

    async def get_webhook(self, webhook_id):
        """Returns the new webhook object for the given id."""
        url = self._baseurl+f'/webhooks/{webhook_id}'

    async def get_webhook_with_token(self, webhook_id, webhook_token):
        """Like get webhook except this call does not
         require authentication and returns no user in the webhook object."""
        url = self._baseurl+f'/webhooks/{webhook_id}/{webhook_token}'

    async def modify_webhook(self, webhook_id):
        """Modify a webhook. Requires the MANAGE_WEBHOOKS permission. Returns the updated webhook object on success."""
        url = self._baseurl+f'/webhooks/{webhook_id}'

    async def modify_webhook_with_token(self, webhook_id, webhook_token):
        """Same as above, except this call does not require authentication,
         does not accept a channel_id parameter in the body, and does not return a user in the webhook object."""
        url = self._baseurl+f'/webhooks/{webhook_id}/{webhook_token}'

    async def delete_webhook(self, webhook_id):
        """Delete a webhook permanently. Requires the MANAGE_WEBHOOKS permission.
         Returns a 204 NO CONTENT response on success."""
        url = self._baseurl+f'/webhooks/{webhook_id}'

    async def delete_webhook_with_token(self, webhook_id, webhook_token):
        """Same as delete webhook, except this call does not require authentication."""
        url = self._baseurl+f'/webhooks/{webhook_id}/{webhook_token}'

    async def execute_webhook(self, webhook_id, webhook_token):
        """Executes the webhook"""
        url = self._baseurl+f'/webhooks/{webhook_id}/{webhook_token}'

    async def get_webhook_message(self, webhook_id, webhook_token, message_id):
        """Returns a previously-sent webhook message from the same token. Returns a message object on success."""
        url = self._baseurl+f'/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}'

    async def edit_webhook_message(self, webhook_id, webhook_token, message_id):
        """Edits a previously-sent webhook message from the same token. Returns a message object on success."""
        url = self._baseurl+f'/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}'

    async def delete_webhook_message(self, webhook_id, webhook_token, message_id):
        """Deletes a message that was created by the webhook. Returns a 204 NO CONTENT response on success."""
        url = self._baseurl+f'/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}'



