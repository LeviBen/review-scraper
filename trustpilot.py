from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import re

# === CONFIGURACIÓN ===
chrome_driver_path = r"C:\Users\PMF Guest\Documents\Reviews Project\chromedriver.exe"

sales_team = {
    "Jeremy Chiprin": ["Jeremy", "Jeremy Chiprin"],
    "Adonis Araya": ["Adonis", "Adonis Araya"],
    "Adam Bell": ["Adam", "Adam Bell"],
    "Anitra Davis": ["Anitra", "Anitra Davis"],
    "Alexandre Gely": ["Alexandre", "Alexandre Gely"],
    "Andy Timoniere": ["Andy", "Andy Timoniere"],
    "Anthony Rack": ["Anthony", "Anthony Rack"],
    "Chad Banks": ["Chad", "Chad Banks"],
    "David Alfaks": ["David", "David Alfaks"],
    "Daniel Cohen": ["Daniel", "Daniel Cohen"],
    "Daniel Argy": ["Daniel Argy", "Argy"],
    "Andrew Gold": ["Andrew", "Andrew Gold"],
    "Dante Siordia": ["Dante", "Dante Siordia"],
    "Giorgi Titvinidze": ["Giorgi", "Giorgi Titvinidze"],
    "Griffin Skipper": ["Griffin", "Griffin Skipper"],
    "Hitch Merdassi": ["Hitch", "Hitch Merdassi"],
    "Joey Faks": ["Joey", "Joey Faks"],
    "Jack Klicsu": ["Jack", "Jack Klicsu"],
    "Jonathan Carreno": ["Jonathan", "Jonathan Carreno"],
    "Jordan Fogel": ["Jordan", "Jordan Fogel"],
    "Jake Goranson": ["Jake", "Jake Goranson"],
    "Jason Kurashvili": ["Jason", "Jason Kurashvili"],
    "Joe Melman": ["Joe", "Joe Melman"],
    "Jeffrey Paz": ["Jeffrey", "Jeffrey Paz"],
    "Joey Simon": ["Joey Simon", "Simon"],
    "Lawrence Thompson": ["Lawrence", "Lawrence Thompson"],
    "Max Marguello": ["Max", "Max Marguello"],
    "Mitchell Barnes": ["Mitchell", "Mitchell Barnes"],
    "Moshe Galapo": ["Moshe", "Moshe Galapo"],
    "Martin Ivanov": ["Martin", "Martin Ivanov"],
    "Marshall Wells": ["Marshall", "Marshall Wells"],
    "Nathan Yusufov": ["Nathan", "Nathan Yusufov"],
    "Paul Gabay": ["Paul", "Paul Gabay"],
    "Randy Elias": ["Randy", "Randy Elias"],
    "Richard Brzezinski": ["Richard", "Richard Brzezinski"],
    "Samuel Bard": ["Samuel", "Sam", "Samuel Bard"],
    "Soufiane Diakite": ["Soufiane", "Soufiane Diakite"],
    "Siuzanna Saparkina": ["Siuzanna", "Siuzanna Saparkina"],
    "Sharugan Kumar": ["Sharugan", "Sharugan Kumar"],
    "Salman Malik": ["Salman", "Salman Malik"],
    "Trent Lewis": ["Trent", "Trent Lewis"],
    "Victor Garcia": ["Victor", "Victor Garcia"],
    "Yosef Zwick": ["Yosef", "Yosef Zwick"],
    "William Arbelaez": ["William", "William Arbelaez"]
}

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
wait = WebDriverWait(driver, 20)

# === Abre Trustpilot ===
driver.get("https://www.trustpilot.com/review/www.pmfus.com")
time.sleep(5)

# === Aceptar cookies ===
try:
    cookie_button = wait.until(EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler')))
    cookie_button.click()
    print("✅ Cookies aceptadas")
except Exception as e:
    print("⚠️ No se pudieron aceptar cookies:", e)

data = []

# === BUCLE MULTIPÁGINA ===
while True:
    print("🔄 Haciendo scroll progresivo hasta cargar reseñas...")
    for _ in range(20):
        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(1.5)

    # === Extraer reseñas de esta página ===
    review_blocks = driver.find_elements(By.XPATH, '//section//article')
    print(f"🔍 Procesando {len(review_blocks)} reseñas...")

    for block in review_blocks:
        try:
            paragraphs = block.find_elements(By.CSS_SELECTOR, 'p')
            text = " ".join([p.text for p in paragraphs if p.text.strip() != ""])

            rep = None
            for full_name, aliases in sales_team.items():
                if any(alias.lower() in text.lower() for alias in aliases):
                    rep = full_name
                    break

            # === STARS ===
            try:
                stars_img = block.find_element(By.CSS_SELECTOR, "img[alt*='Rated']")
                alt_text = stars_img.get_attribute("alt").strip()
                match = re.search(r'Rated (\d) out of 5', alt_text)
                stars_text = match.group(1) if match else "No rating"
            except:
                stars_text = "No rating"

            # === FECHA ===
            try:
                date_element = block.find_element(By.TAG_NAME, 'time')
                date_raw = date_element.text.strip()
                match = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2}, \d{4}', date_raw)
                date_text = match.group(0) if match else date_raw
            except:
                date_text = "Unknown"

            if rep:
                data.append({
                    "Representative": rep,
                    "Date": date_text,
                    "Stars": stars_text,
                    "Text": text.strip(),
                    "Platform": "Trustpilot"
                })

        except Exception as e:
            print(f"⚠️ Error procesando reseña: {e}")
            continue

    # === Ver si hay otra página ===
    try:
        next_button = driver.find_element(By.XPATH, '//a[@aria-label="Next page"]')
        is_disabled = next_button.get_attribute("aria-disabled") == "true"

        if not is_disabled:
            print("➡️ Cargando siguiente página de reseñas...")
            driver.execute_script("arguments[0].click();", next_button)
            time.sleep(4)
        else:
            print("✅ No hay más páginas (botón deshabilitado). Fin del scraping.")
            break

    except Exception as e:
        print("✅ No se encontró botón de siguiente página. Fin del scraping.")
        break

# === Guardar CSV ===
df = pd.DataFrame(data)
df.to_csv("trustpilot_reviews_sales_mentions.csv", index=False)
print(f"✅ CSV generado con {len(data)} reseñas mencionando representantes")

driver.quit()
