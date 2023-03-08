from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pandas as pd

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)
driver.get("https://twitter.com/login") 
sleep(3)

nomeUsuario = driver.find_element(By.XPATH,"//input[@name='text']")
nomeUsuario.send_keys("EMAIL")
avancar = driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
avancar.click()

sleep(3)

telefone = driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
telefone.send_keys('TELEFONE')
buttonPhone = driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')
buttonPhone.click()
sleep(3)

senha = driver.find_element(By.XPATH,"//input[@name='password']")

senha.send_keys('SENHA')
loginButton = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
loginButton.click()
sleep(5)

subject = '@jairbolsonaro'
search_box = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")
search_box.send_keys(subject)
search_box.send_keys(Keys.ENTER)

articles = driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")

UserTags=[]
TimeStamps=[]
Tweets=[]
Replys=[]
reTweets=[]
Likes=[]

for article in articles:
    
        UserTag = driver.find_element(By.XPATH,".//div[@data-testid='User-Names']").text
        UserTags.append(UserTag)
        
        TimeStamp = driver.find_element(By.XPATH,".//time").get_attribute('datetime')
        TimeStamps.append(TimeStamp)
        
        Tweet = driver.find_element(By.XPATH,".//div[@data-testid='tweetText']").text
        Tweets.append(Tweet)
        
        Reply = driver.find_element(By.XPATH,".//div[@data-testid='reply']").text
        Replys.append(Reply)
        
        reTweet = driver.find_element(By.XPATH,".//div[@data-testid='retweet']").text
        reTweets.append(reTweet)
        
        Like = driver.find_element(By.XPATH,".//div[@data-testid='like']").text
        Likes.append(Like)

        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        sleep(3)
        articles = driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")
        Tweets2 = list(set(Tweets))
        if len(Tweets2) > 5:
            break


data = {
    'Tag de usuário': UserTags,
    'TimeStamp': TimeStamps,
    'Tweet': Tweets,
    'Replys': Replys,
    'ReTweets': reTweets,
    'Likes': Likes
}

df = pd.DataFrame(data)
display(df)
