import asyncio

from hume.client import AsyncHumeClient

client = AsyncHumeClient(
    api_key="YOUR_API_KEY",
)

class HumeClient:
    def __init__(self, api_key: str):
        self.client = AsyncHumeClient(api_key=api_key)

    async def list_configs(self):
        return await self.client.empathic_voice.configs.list_configs()