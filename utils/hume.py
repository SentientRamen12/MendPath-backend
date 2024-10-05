import asyncio

from hume.client import AsyncHumeClient
from constants.config import HUME_API_KEY

class HumeClient:
    def __init__(self):
        self.client = AsyncHumeClient(api_key=HUME_API_KEY)

    async def list_configs(self):
        return await self.client.empathic_voice.configs.list_configs()