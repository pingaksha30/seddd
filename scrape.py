import asyncio
from playwright.async_api import async_playwright

urls = [
    "https://sanand0.github.io/tdsdata/js_table/?seed=54",
    "https://sanand0.github.io/tdsdata/js_table/?seed=55",
    "https://sanand0.github.io/tdsdata/js_table/?seed=56",
    "https://sanand0.github.io/tdsdata/js_table/?seed=57",
    "https://sanand0.github.io/tdsdata/js_table/?seed=58",
    "https://sanand0.github.io/tdsdata/js_table/?seed=59",
    "https://sanand0.github.io/tdsdata/js_table/?seed=60",
    "https://sanand0.github.io/tdsdata/js_table/?seed=61",
    "https://sanand0.github.io/tdsdata/js_table/?seed=62",
    "https://sanand0.github.io/tdsdata/js_table/?seed=63"
]

async def run():
    total = 0
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        for url in urls:
            await page.goto(url)
            numbers = await page.eval_on_selector_all(
                "table td",
                "els => els.map(e => parseInt(e.innerText)).filter(n => !isNaN(n))"
            )
            total += sum(numbers)
        await browser.close()
    print(f"TOTAL_SUM={total}")

asyncio.run(run())
