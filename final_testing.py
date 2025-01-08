import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fetch_and_write_data(title, url, output_df):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0 Safari/537.36"
    }
    chromedriver_path = '/usr/bin/chromedriver' 

    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--disable-gpu") 
    chrome_options.add_argument(f"user-agent={headers['User-Agent']}")  

    service = Service(executable_path=chromedriver_path)

    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open the webpage
    driver.get(url)

    wait = WebDriverWait(driver, 1)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body'))) 

    data = {}
    
    try:
        market_cap_label = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Market Cap')]")))
        data["Market Cap"] = market_cap_label.find_element(By.XPATH, "following-sibling::div").text

        fdv_label = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Fully Diluted Valuation')]")))
        data["Fully Diluted Valuation"] = fdv_label.find_element(By.XPATH, "following-sibling::div").text

        htv_label = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), '24 Hour Trading Vol')]")))
        data["24 Hour Trading Vol"] = htv_label.find_element(By.XPATH, "following-sibling::div").text

        circulating_supply_label = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Circulating Supply')]")))
        data["Circulating Supply"] = circulating_supply_label.find_element(By.XPATH, "following-sibling::div").text

        total_supply_label = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Total Supply')]")))
        data["Total Supply"] = total_supply_label.find_element(By.XPATH, "following-sibling::div").text

        max_supply_label = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Max Supply')]")))
        data["Max Supply"] = max_supply_label.find_element(By.XPATH, "following-sibling::div").text

    except Exception as e:
        print(f"Error: {e}")
    
    driver.quit()

    # Add the scraped data to the DataFrame as a new row
    data_row = {"Title": title, **data}
    output_df = pd.concat([output_df, pd.DataFrame([data_row])], ignore_index=True)

    return output_df

def read_and_process_csv(input_csv, output_csv):
    # Read the input CSV file using pandas
    input_df = pd.read_csv(input_csv)
    
    # Initialize an empty DataFrame for the output data
    columns = ["Title", "Market Cap", "Fully Diluted Valuation", "24 Hour Trading Vol", "Circulating Supply", "Total Supply", "Max Supply"]
    output_df = pd.DataFrame(columns=columns)

    # For each row in the input CSV, fetch and process the data
    for index, row in input_df.iterrows():
        title = row['Title']
        url = row['URL']
        output_df = fetch_and_write_data(title, url, output_df)

    # Write the output DataFrame to a CSV file
    output_df.to_csv(output_csv, index=False)

# Example usage
read_and_process_csv('input.csv', 'output.csv')  # Replace 'input.csv' with your input CSV file name
