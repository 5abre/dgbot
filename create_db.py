import asyncio
from dgbot.backend.models import *
from dgbot.core.database import async_main


async def main():
    await async_main()
    print(f"Таблицы созданы: {list(Base.metadata.tables.keys())}")


if __name__ == "__main__":
    asyncio.run(main())