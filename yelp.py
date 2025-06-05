import time
import random
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = r"C:\Users\PMF Guest\Documents\Reviews Project\chromedriver.exe"

# === Humanizar comportamiento ===
def human_sleep(a=1.5, b=3.0):
    time.sleep(random.uniform(a, b))

def human_scroll(driver, min_scrolls=10, max_scrolls=18):
    for _ in range(random.randint(min_scrolls, max_scrolls)):
        delta = random.randint(300, 800)
        driver.execute_script(f"window.scrollBy(0, {delta});")
        human_sleep(0.5, 1.5)

# === Diccionario de representantes ===
sales_team = {
    "Jeremy Chiprin": ["Jeremy", "Jeremy Chiprin"],
    "Adonis Araya": ["Adonis", "Adonis Araya"],
    "Adam Bell": ["Adam", "Adam Bell"],
    # ...
    "William Arbelaez": ["William", "William Arbelaez"]
}

# === Setup opciones ===
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
wait = WebDriverWait(driver, 15)

# === URL ===
driver.get("https://www.yelp.com/biz/premium-merchant-funding-new-york")
human_sleep(3, 5)

# === Filtro ===
try:
    wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Yelp Sort"]'))).click()
    human_sleep()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Newest First"]'))).click()
    print("✅ Filtro aplicado")
    human_sleep()
except:
    print("⚠️ No se pudo aplicar filtro")

# === Extraer reseñas ===
def extract_reviews():
    blocks = driver.find_elements(By.XPATH, '//div[@data-testid="review"]')
    reviews = []
    for block in blocks:
        try:
            text = block.text
            rep = None
            for name, aliases in sales_team.items():
                if any(alias.lower() in text.lower() for alias in aliases):
                    rep = name
                    break
            if rep:
                try:
                    stars = block.find_element(By.XPATH, './/div[contains(@aria-label,"star rating")]').get_attribute("aria-label")
                except:
                    stars = "No rating"
                try:
                    date = block.find_element(By.XPATH, './/span[contains(@class, "css-chan6m")]').text
                except:
                    date = "Unknown"
                reviews.append({
                    "Representative": rep,
                    "Date": date,
                    "Stars": stars,
                    "Text": text.strip(),
                    "Platform": "Yelp"
                })
        except:
            continue
    return reviews

# === Loop paginación ===
all_reviews = []

while True:
    human_scroll(driver)
    all_reviews += extract_reviews()

    try:
        next_btn = driver.find_element(By.XPATH, '//a[@aria-label="Next"]')
        if next_btn.is_displayed():
            driver.execute_script("arguments[0].scrollIntoView();", next_btn)
            human_sleep(1, 2.5)
            next_btn.click()
            print("➡️ Página siguiente...")
            human_sleep(2, 4)
        else:
            break
    except:
        print("🛑 No hay más páginas")
        break

# === Guardar CSV ===
pd.DataFrame(all_reviews).to_csv("yelp_reviews_sales_mentions.csv", index=False)
print(f"✅ CSV generado con {len(all_reviews)} reseñas")

driver.quit()
