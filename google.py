from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import pandas as pd
from datetime import datetime, timedelta


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
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
wait = WebDriverWait(driver, 20)

# === PMF Review page ===
driver.get("https://www.google.com/maps/search/Premium+Merchant+Funding")
time.sleep(5)

try:
    side_panel = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "tAiQdd"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", side_panel)
    time.sleep(1)
except:
    print("⚠️ Couldn't find the  panel, but we continue...")

# === Click on REVIEWS Tab ===
try:
    reviews_tab = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[contains(., "Reviews")]'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", reviews_tab)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", reviews_tab)  # ← ¡clic forzado por JS!
    print("✅ Clicked on the REVIEWS tab with JS")
    time.sleep(5)

    try:
        # Wait and click on the sort button
        sort_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label*="Sort"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", sort_button)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", sort_button)
        print("✅ Clicked sort button")
        time.sleep(2)

        # Wait for the NEWEST option and force it with JS
        newest_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Newest")]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", newest_option)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", newest_option)
        print("✅ Filter applied: Most recent reviews")
        time.sleep(3)

    except Exception as e:
        print("⚠️ Couldn't apply the filter 'Newest'")
        print(e)

except Exception as e:
    print("❌ Couldn't be possible to click on the REVIEWS tab")
    print(e)
    driver.quit()
    exit()

# === Scroll inside REVIEWS Tab ===
try:
    scrollable_div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "m6QErb.DxyBCb.kA9KIf.dS8AEf")))
    for _ in range(10):  # Aumenta si quieres más reviews
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
        time.sleep(2)
except:
    print("❌ Couldn't scroll on the REVIEWS tab")
    driver.quit()
    exit()

# === Extract REVIEWS ===
time.sleep(3)  # espera final
review_elements = driver.find_elements(By.CLASS_NAME, "jftiEf")

data = []
for el in review_elements:
    text = el.text
    rep = None
    for full_name, aliases in sales_team.items():
        if any(alias.lower() in text.lower() for alias in aliases):
            rep = full_name
            break
    if rep:
        # === STARS ===
        try:
            # Intenta encontrar directamente el span con estrellas visibles
            star_span = el.find_element(By.CSS_SELECTOR, 'span[role="img"]')
            stars = star_span.get_attribute("aria-label")
            if not stars or "star" not in stars.lower():
                stars = "No rating"
        except Exception as e:
            print(f"⚠️ Error extracting stars for review: {e}")
            stars = "No rating"

        # === FECHA ===
        try:
            date_element = el.find_element(By.CLASS_NAME, "rsqaWe")
            date_text = date_element.text.strip().lower()

            today = datetime.today()
            delta = None

            if "minute" in date_text:
                num = int(re.search(r'\d+', date_text).group())
                delta = timedelta(minutes=num)
            elif "hour" in date_text:
                num = int(re.search(r'\d+', date_text).group())
                delta = timedelta(hours=num)
            elif "day" in date_text:
                num = 1 if "a day" in date_text else int(re.search(r'\d+', date_text).group())
                delta = timedelta(days=num)
            elif "week" in date_text:
                num = 1 if "a week" in date_text else int(re.search(r'\d+', date_text).group())
                delta = timedelta(weeks=num)
            elif "month" in date_text:
                num = 1 if "a month" in date_text else int(re.search(r'\d+', date_text).group())
                delta = timedelta(days=num * 30)
            elif "year" in date_text:
                num = 1 if "a year" in date_text else int(re.search(r'\d+', date_text).group())
                delta = timedelta(days=num * 365)

            date = (today - delta).strftime("%Y-%m-%d") if delta else "Unknown"
        except:
            date = "Unknown"

        # === GUARDAR REVIEW ===
        data.append({
            "Representative": rep,
            "Date": date,
            "Stars": stars,
            "Text": text.strip(),
            "Platform": "Google"
        })

# === GUARDAR CSV ===
df = pd.DataFrame(data)
df.to_csv("google_reviews_sales_mentions.csv", index=False)
print("✅ CSV Generated with", len(data), "founded reviews")

driver.quit()
