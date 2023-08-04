from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By


# specify the path to the geckodriver executable
driver_path = "geckodriver.exe"

service = Service(executable_path=driver_path)

# create a new Firefox browser instance with the specified driver path
driver = webdriver.Firefox(service=service)

# navigate to Bing website
driver.get("https://www.bing.com/")
print(driver.title) # print the title of the page

# find the search box element and enter "place to eat dinner"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("place to eat dinner")
search_box.send_keys(Keys.ENTER)

# find the first search result and print the title
try:
    search_results = driver.find_elements(By.CSS_SELECTOR, "li.b_algo")
    first_result = search_results[0]
    first_result_title = first_result.find_element(By.CSS_SELECTOR, "h2").text
    print("Place to eat dinner: ", first_result_title)
except IndexError:
    print("No search results found.")

# navigate back to the Bing homepage
driver.get("https://www.bing.com/")

# find the search box element and enter "movie to watch at 11pm"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("movie to watch at 11pm")
search_box.send_keys(Keys.ENTER)

# find the first search result and print the title
try:
    search_results = driver.find_elements(By.CSS_SELECTOR, "li.b_algo")
    first_result = search_results[0]
    first_result_title = first_result.find_element(By.CSS_SELECTOR, "h2").text
    print("Movie to watch at 11pm: ", first_result_title)
except IndexError:
    print("No search results found.")

# close the browser window
driver.quit()