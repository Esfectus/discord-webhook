import requests, asyncio
from json import dumps


class Webhook:
    """Webhook Class"""

    def __init__(self, token: str) -> None:
        self._baseurl = 'https://discord.com/api/v9'
        self._auth_header = {'Authorization': f'Bot {token}'}

    async def create_webhook(self):
        """Creates a new webhook.
        Create a new webhook. Requires the MANAGE_WEBHOOKS permission. Returns a webhook object on success.
        """
        pass

    async def get_channel_webhooks(self):
        """Create a new webhook. Requires the MANAGE_WEBHOOKS permission. Returns a webhook object on success."""
        pass

    async def get_guild_webhooks(self):
        """Returns a list of guild webhook objects. Requires the MANAGE_WEBHOOKS permission."""
        pass

    async def get_webhook(self):
        """Returns the new webhook object for the given id."""
        pass

    async def get_webhook_with_token(self):
        """Like get webhook except this call does not
         require authentication and returns no user in the webhook object."""
        pass

    async def modify_webhook(self):
        """Modify a webhook. Requires the MANAGE_WEBHOOKS permission. Returns the updated webhook object on success."""
        pass

    async def modify_webhook_with_token(self):
        """Same as above, except this call does not require authentication,
         does not accept a channel_id parameter in the body, and does not return a user in the webhook object."""
        pass

    async def delete_webhook(self):
        """Delete a webhook permanently. Requires the MANAGE_WEBHOOKS permission.
         Returns a 204 NO CONTENT response on success."""
        pass

    async def delete_webhook_with_token(self):
        """Same as delete webhook, except this call does not require authentication."""
        pass

    async def execute_webhook(self):
        """Executes the webhook"""
        pass

    async def get_webhook_message(self):
        """Returns a previously-sent webhook message from the same token. Returns a message object on success."""
        pass

    async def edit_webhook_message(self):
        """Edits a previously-sent webhook message from the same token. Returns a message object on success."""
        pass

    async def delete_webhook_message(self):
        """Deletes a message that was created by the webhook. Returns a 204 NO CONTENT response on success."""
        pass



