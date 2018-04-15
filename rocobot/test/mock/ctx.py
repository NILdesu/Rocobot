import asyncio

import discord
from discord import abc

class MockContext(discord.abc.Messageable):
    def __init__(self):
        self.data = {}
        self.content = []

    @asyncio.coroutine
    def _get_channel(self):
        raise NotImplementedError

    @asyncio.coroutine
    def send(self, content=None, *, tts=False, embed=None, file=None,
                files=None, delete_after=None, nonce=None):
        self.content.append(content)

def create_mock_ctx():
    return MockContext()
