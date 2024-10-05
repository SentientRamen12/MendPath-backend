import asyncio

from hume.client import AsyncHumeClient

client = AsyncHumeClient(
    api_key="YOUR_API_KEY",
)

async def main() -> None:
    await client.empathic_voice.configs.list_configs()

asyncio.run(main())