#!/usr/bin/env python3
"""
Async Comprehensions
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Creates a list of 10 numbers from a 10-number generator
    """
    return [num async for num in async_generator()]


if __name__ == "__main__":
    import asyncio

    async def main():
        print(await async_comprehension())

    asyncio.run(main())
