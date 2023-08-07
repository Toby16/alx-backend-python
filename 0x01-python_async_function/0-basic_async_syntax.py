#!/usr/bin/env python3
"""
The basics of async
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random - asynchronous coroutine that takes in an integer argument,
    waits for a random delay between 0,
    and max_delay seconds and eventually returns it.
    """
    random_int = random.uniform(0, max_delay)
    await asyncio.sleep(random_int)
    return random_int


if __name__ == "__main__":
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
