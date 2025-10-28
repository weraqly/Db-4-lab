import asyncio
import aiohttp
import random
import string
import time
import argparse


def make_payload() -> dict:
    r = lambda n=6: ''.join(random.choice(string.ascii_letters) for _ in range(n))
    return {
        "city": f"City_{r()}",
        "street": f"{random.choice(['Main', 'Central', 'Liberty', 'Shevchenka'])} St",
        "street_number": random.randint(1, 400),
        "district": random.choice(["Center", "North", "South", "East", "West"]),
        "city_index": random.randint(10000, 99999),
        "country": random.choice(["Ukraine", "Poland", "Germany", "Italy"]),
    }


async def send_request(session, url, payload, timeout):
    try:
        async with session.post(url, json=payload, timeout=timeout) as resp:
            return 200 <= resp.status < 300
    except:
        return False


async def run_load(url: str, total: int, rps: float):
    concurrency = 100
    timeout = 10
    sem = asyncio.Semaphore(concurrency)
    ok = fail = 0
    interval = 1 / rps if rps > 0 else 0

    async with aiohttp.ClientSession() as session:
        start = time.perf_counter()
        tasks = []

        for _ in range(total):
            await asyncio.sleep(interval)
            payload = make_payload()

            async def task():
                nonlocal ok, fail
                async with sem:
                    if await send_request(session, url, payload, timeout):
                        ok += 1
                    else:
                        fail += 1

            tasks.append(asyncio.create_task(task()))

        await asyncio.gather(*tasks)
        dur = time.perf_counter() - start

    print(f"\nURL: {url}")
    print(f"Total: {total} | OK: {ok} | Fail: {fail}")
    print(f"Target RPS: {rps} | Actual: {(ok+fail)/dur:.2f}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--url", default="https://lab2.bluecoast-58ac786c.switzerlandnorth.azurecontainerapps.io/address_machine",
                   help="Target endpoint")
    p.add_argument("--total", type=int, default=100)
    p.add_argument("--rps", type=float, default=20)
    args = p.parse_args()
    asyncio.run(run_load(args.url, args.total, args.rps))


if __name__ == "__main__":
    main()
