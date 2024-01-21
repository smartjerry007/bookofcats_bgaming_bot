from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from time import sleep


# Please insert your username or email, below password and totalPlayNumber
useremail = "Louis"
password = "Best Friend"
playNum=10000

driver = webdriver.Chrome()
driver.maximize_window()
# Open the web page
driver.get("https://shuffle.com")
sleep(2)
login = driver.find_element(By.CLASS_NAME, "Header_transparentButton__5_2oL")

# Automate login
login.click()
sleep(1)
nameinput = driver.find_element(By.CLASS_NAME, "iYJcJA")
nameinput.send_keys(useremail)
sleep(0.1)
passwordinput = driver.find_element(By.CLASS_NAME, "mask-input")
passwordinput.send_keys(password)
logingroup = driver.find_element(By.XPATH, "//*[@id='login-form']/div[4]/button")
logingroup.click()

#During captcha and email verify, you should do it manually. The time is 40s, but you can change it.
sleep(40)

#Select the game
search = driver.find_element(By.XPATH,'//*[@id="pageContent"]/div/div/section[2]/div/div[2]/div/div/input')
search.send_keys("book of cats")
sleep(0.5)
selectgame = driver.find_elements(By.XPATH, '//*[@id="pageContent"]/div/div/section[3]/div/div/div[1]/div[2]/div/a/div')[0]
selectgame.click()
sleep(0.5)
realgame = driver.find_element(By.XPATH, '//*[@id="pageContent"]/div/div/div[1]/div/div[1]/div[1]/div/div[2]/button[1]')
#       //*[@id="pageContent"]/div/div/div[1]/div/div[1]/div[1]/div/div[2]/button[1]          --realgame
#       //*[@id="pageContent"]/div/div/div[1]/div/div[1]/div[1]/div/div[2]/button[2]          --fungame
realgame.click()
sleep(1)

def click_button_in_canvas(driver):
    iframe = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div[2]/iframe")
    driver.switch_to.frame(iframe)
    canvas = driver.find_element(By.TAG_NAME, "canvas")  # Replace with the actual ID of the canvas
    action = ActionChains(driver)
    sleep(0.1)
    action.move_to_element_with_offset(canvas, 480, 300) #Click the play button
    action.click()
    action.perform()
    action.move_to_element_with_offset(canvas, 0, 50)#Click OK of error window
    action.click()
    action.perform()
    sleep(0.1)
    driver.switch_to.default_content()
    
# Continuous button click with a delay of 1 second
def main() :
    count = 0
    while (count <= playNum):
        try:
            click_button_in_canvas(driver)
            count += 1
            sleep(0.5)
        except:
            pass

if __name__ == "__main__":
    main()