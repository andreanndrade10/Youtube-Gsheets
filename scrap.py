from selenium import webdriver
import time
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

chromedriver_path = 'C:/Users/ASUS/Documents/Python/chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)

#Change the url for the channel you want extract data
webdriver.get('https://www.youtube.com/results?search_query=channel+that+you+want+scrap')


p_element2 = webdriver.find_element_by_xpath("//span[@id='video-count']")
nVideos = int(p_element2.text.split()[0].replace(".",""))
print(nVideos)
#click on channel
webdriver.find_element_by_xpath("//yt-img-shadow[@class='style-scope ytd-channel-renderer no-transition']").click()
time.sleep(5)
p_element = webdriver.find_element_by_xpath("//yt-formatted-string[@id='subscriber-count']")
nSubscribers = int(p_element.text.split()[0].replace(".",""))
print(nSubscribers)

webdriver.close()

#####################################

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
#.json of gsheets API credentials must be on your script directory
credentials = ServiceAccountCredentials.from_json_keyfile_name('spreadSheet-extractor-e95a9fbd1040.json', scope)


gc = gspread.authorize(credentials)
wks = gc.open('Youtube_py PQP').sheet1

# print(wks.get_all_records())
now = datetime.datetime.now()
#write on the last empty row
wks.append_row([now.strftime("%Y-%m-%d"), nSubscribers, nVideos])
print("Your Google Sheet is updated!")


