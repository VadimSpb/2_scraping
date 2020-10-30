from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

from MongoDb_session import push_to_MongoDb

sender_list=[]
date_list=[]
subject_list=[]
body_list=[]
driver = webdriver.Chrome()
driver.get('https://mail.ru')
assert "Mail.ru" in driver.title

#Заполняем поля для ввода
login = driver.find_element_by_id("mailbox:login")
login.send_keys('study.ai_172@mail.ru')
login.submit()

#Кнопка введите пароль
btn_pass_ent = driver.find_element_by_id("mailbox:submit")
btn_pass_ent.click()
password = driver.find_element_by_id("mailbox:password")
password.send_keys('Password172')
password.submit()
time.sleep(5)

action = ActionChains(driver)
all_ = driver.find_element_by_class_name("ico_16-burger")
action.move_to_element(all_).perform()
all_.click()
driver.implicitly_wait(1)
folders = driver.find_elements_by_class_name("nav__folder-name__txt")
folder = folders[-5]
action.move_to_element(folder).perform()
folder.click()
time.sleep(2)
i = 0
while True:
    try:
        content = driver.find_elements_by_class_name('llc__container')
        action.move_to_element(content[i])
        content[i].click()
        from_ = driver.find_element_by_class_name('letter__contact-item')
        sender_list.append(from_.text)
        date = driver.find_element_by_class_name('letter__date')
        date_list.append(date.text)
        subject = driver.find_element_by_class_name('thread__subject')
        subject_list.append(subject.text)
        try :
            text = driver.find_element_by_class_name('letter__body')
            body_list.append(text.text)
        except:
            body_list.append(None)
        driver.back()
        i+=1
    except IndexError:
        break
    except Exception as e:
        print(e)
        pass

letters = []
for i in range(len(senderlist)):
    letter = {}
    letter['from'] = sender_list[i]
    letter['date'] = date_list[i]
    letter['subject'] = subject_list[i]
    letter['text'] = body_list[i]

print(f"{len(letters)} letters was parced from mail.ru")

collection = 'mail_letters'
push_to_MongoDb(letters, collection)


