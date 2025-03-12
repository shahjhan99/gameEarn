import time
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Streamlit UI
st.title("💰 Auto Click 'Get Money' in Real-Time")
st.subheader("This will log in and keep clicking 'Get Money' every 90 seconds.")

# User inputs
phone_number = st.text_input("Enter Phone Number", "9234066337733")
start_bot = st.button("Start Bot")
stop_bot = st.button("Stop Bot")

# Global driver variable
driver = None

def start_selenium_bot():
    global driver

    # Launch Chrome
    driver = webdriver.Chrome()
    driver.get("https://shft.pw/")

    # Wait for input field and enter phone number
    phone_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, "payeer"))
    )
    phone_input.clear()
    phone_input.send_keys(phone_number)

    # Click login
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @value='Login / Sign up']"))
    ).click()

    # Click "Earn"
    earn_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/bonus' and text()='Earn']"))
    )
    earn_button.click()

    st.success("✅ Logged in successfully! Auto-clicking 'Get Money'.")

    # Start auto-clicking loop
    while True:
        if stop_bot:
            st.warning("⛔ Bot Stopped.")
            break

        try:
            get_money_button = WebDriverWait(driver, 70).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/get.php' and contains(@class, 'button')]"))
            )
            get_money_button.click()
            st.write("✅ Clicked 'Get Money' at:", time.strftime("%H:%M:%S"))
        except Exception as e:
            st.error(f"⚠️ Error: {e}")

        time.sleep(90)

if start_bot:
    start_selenium_bot()

if stop_bot and driver:
    driver.quit()
    st.warning("🚫 Chrome closed.")
