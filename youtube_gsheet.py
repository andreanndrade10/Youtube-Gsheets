from selenium import webdriver
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials


#Setting up some options 
#options = webdriver.ChromeOptions()
#options.add_argument('headless')
#options.add_argument('window-size=1920x1080')
chromedriver_path = 'C:/Users/ASUS/Documents/Python/chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
#sleep(2)
webdriver.get('https://www.youtube.com/user/praquempedala')
#sleep(3)
p_element = webdriver.find_element_by_xpath("//yt-formatted-string[@id='subscriber-count']")
var = p_element.text.split()[0].replace(".","")

webdriver.close()

##############################

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
#.json of gsheets API credentials must be on your script directory
credentials = ServiceAccountCredentials.from_json_keyfile_name('spreadSheet-extractor-e95a9fbd1040.json', scope)


gc = gspread.authorize(credentials)

wks = gc.open('Youtube_py PQP').sheet1

# print(wks.get_all_records())
now = datetime.datetime.now()
#escreve na ultima linha da tabela.
wks.append_row([now.strftime("%Y-%m-%d"), int(var)])
print("Your Google Sheet is updated!")