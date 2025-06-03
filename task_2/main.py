import asyncio
from database import Session, Base, engine
from playwright.async_api import async_playwright


def create_tables():
    Base.metadata.create_all(engine)


def delete_tables():
    Base.metadata.drop_all(engine)


async def get_bulletins():
    url = 'https://spimex.com/markets/oil_products/trades/results/'
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        bulletins = []
        
        while True:
            try:
                await page.wait_for_selector('a[href*=".xls"]', timeout=5000)
            except:
                break

            links = await page.eval_on_selector_all(
                'a[href*=".xls"]',
                'elements => elements.map(el => el.href)'
            )

            bulletins.extend(links)

            next_button = await page.query_selector('button.next')
            if not next_button:
                next_button = await page.query_selector('a.next')
            if not next_button:
                next_button = await page.query_selector('text=Вперед')

            is_disabled = await next_button.get_attribute('disabled')
            if is_disabled:
                break

            await next_button.click(force=True)
            
            await page.wait_for_load_state('networkidle')

        await browser.close()
        return bulletins

def parse_bulletin(url):
    pass

# def main():
#     bulletin_links = get_bulletins()

links = asyncio.run(get_bulletins())
print(links)