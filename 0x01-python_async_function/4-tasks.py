#!/usr/bin/env python3
"""
Tasks
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes task_wait_random n times.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*tasks))

if __name__ == "__main__":
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
