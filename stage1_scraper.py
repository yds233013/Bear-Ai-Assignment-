#!/usr/bin/env python3
"""
Bear AI Assignment - Stage 1: Web Scraping
This script queries ChatGPT with sportswear prompts and counts brand mentions.
"""

import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config import BRANDS, PROMPTS, CHATGPT_URL, RESPONSE_WAIT_TIME, REQUEST_DELAY
from utils import count_brand_mentions, create_result_entry, print_summary

def setup_driver():
    """Set up Chrome driver for web scraping"""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def scrape_chatgpt_response(driver, prompt):
    """Query ChatGPT with a prompt and extract the response"""
    try:
        driver.get(CHATGPT_URL)
        
        wait = WebDriverWait(driver, 20)
        textarea = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[data-id='root']")))
        
        textarea.clear()
        textarea.send_keys(prompt)
        textarea.send_keys(Keys.RETURN)
        
        time.sleep(RESPONSE_WAIT_TIME)
        
        response_elements = driver.find_elements(By.CSS_SELECTOR, "[data-message-author-role='assistant']")
        if response_elements:
            return response_elements[-1].text
        else:
            return "No response generated"
            
    except Exception as e:
        print(f"Error scraping response: {e}")
        return "Error occurred during scraping"

def main():
    """Main function to run the web scraping process"""
    print("🐻 Bear AI Assignment - Stage 1: Web Scraping")
    print("=" * 50)
    
    results = []
    driver = setup_driver()
    
    try:
        for i, prompt in enumerate(PROMPTS, 1):
            print(f"\n📝 Processing prompt {i}/10: {prompt[:50]}...")
            
            response = scrape_chatgpt_response(driver, prompt)
            brand_counts = count_brand_mentions(response, BRANDS)
            result = create_result_entry(i, prompt, response, brand_counts)
            results.append(result)
            
            print(f"✅ Found mentions: {brand_counts}")
            time.sleep(REQUEST_DELAY)
    
    finally:
        driver.quit()
    
    # Save results to JSON file
    output_file = 'brand_mentions_results.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print_summary(results, BRANDS)
    print(f"\n📁 Results saved to: {output_file}")
    return results

if __name__ == "__main__":
    main() 