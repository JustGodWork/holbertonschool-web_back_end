#!/usr/bin/env python3
"""
    Place this file in the python_async_comprehension/ directory
"""

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def main():
    print(await async_comprehension())

asyncio.run(main())
