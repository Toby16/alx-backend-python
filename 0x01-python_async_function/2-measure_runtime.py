#!/usr/bin/env python3
"""
Measure the runtime
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Computes the average runtime of wait_n
    """
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    elapsed_time = end_time - start_time

    return float(elapsed_time/n)


if __name__ == "__main__":
    n = 5
    max_delay = 9

    print(measure_time(n, max_delay))
