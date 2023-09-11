from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from credentials import user_password, user_email, repo_name, repo_description, nickname

browser = webdriver.Chrome()
browser.get('https://github.com/')


#define sign in process
def sign_in(): 
    browser.implicitly_wait(5)
    sign_in = browser.find_element(By.LINK_TEXT, 'Sign in')
    sign_in.click()
    #enter credentials
    browser.implicitly_wait(5)
    login = browser.find_element(By.ID, 'login_field')
    login.send_keys(user_email)
    password = browser.find_element(By.ID, 'password')
    password.send_keys(user_password)
    submit = browser.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[13]')
    submit.click()


#define creation process
def create_repo(): 
    # open user modal menu
    browser.implicitly_wait(5)
    browser.find_element(By.CLASS_NAME, 'AppHeader-user').click()
    #select repos in modal menu
    browser.implicitly_wait(5)
    browser.find_element(By.LINK_TEXT, 'Your repositories').click()
    #create new repo
    browser.implicitly_wait(2)
    browser.find_element(By.XPATH, '//*[@id="user-profile-frame"]/div/div[1]/div/div').click()
    #fill in info about new repo
    browser.implicitly_wait(2)
    #set name
    browser.find_element(By.CSS_SELECTOR, '.kOsqyr > input, .kOsqyr > select').send_keys(repo_name)
    #add description
    browser.implicitly_wait(2)
    browser.find_element(By.NAME, 'Description').send_keys(repo_description)
    #set to private
    browser.find_element(By.XPATH, '/html/body/div[1]/div[6]/main/react-app/div/form/div[3]/div[1]/div[2]/div/div/div/fieldset/div/div[2]/div[1]/input').click()
    #add readme.md file
    browser.find_element(By.XPATH, '/html/body/div[1]/div[6]/main/react-app/div/form/div[3]/div[2]/div/div[1]/div/div[1]/input').click()
    #choose licence type - modal window
    #browser.find_element(By.XPATH, '//*[@id=":rg:"]').click()
    #submit
    browser.find_element(By.XPATH, '/html/body/div[1]/div[6]/main/react-app/div/form/div[5]/button/span').click()
    sleep(2)

#save the name of created repo

#define delete process
def delete_repo(): 
    browser.implicitly_wait(10)
    browser.find_element(By.ID, 'settings-tab').click()
    browser.find_element(By.ID, 'dialog-show-repo-delete-menu-dialog').click()
    browser.find_element(By.ID, 'repo-delete-proceed-button').click()
    browser.find_element(By.ID, 'repo-delete-proceed-button').click()
    browser.find_element(By.ID, 'verification_field').send_keys(nickname + '/' + repo_name)
    browser.find_element(By.ID, 'repo-delete-proceed-button').click()


#logout
def logout(): 
    browser.implicitly_wait(10)
    # open user modal menu
    browser.find_element(By.CLASS_NAME, 'AppHeader-user').click()
    browser.find_element(By.LINK_TEXT, 'Sign out').click()
    browser.find_element(By.XPATH, '/html/body/div[1]/div[6]/main/div/form/input[2]').click()



sign_in()

create_repo()
check_repo_name = browser.find_element(By.XPATH, '//*[@id="repository-container-header"]/div[1]/div[1]/div[1]/strong/a').text
assert(check_repo_name == repo_name)

delete_repo()

#logout()

sleep(10)
browser.quit()