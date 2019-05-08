from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from configparser import ConfigParser

print('Paste Flipkart URL:')

CONFIG = ConfigParser()
CONFIG.read('config.ini')

driver_path = CONFIG.get('MAIN', 'DRIVER_LOCATION') #"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
email_inp = CONFIG.get('CREDENTIALS', 'USERNAME')
pass_inp = CONFIG.get('CREDENTIALS', 'PASSWORD')
cvv_inp = CONFIG.get('ORDER', 'CVV') 
addr_input = CONFIG.get('ORDER', 'ADDRESS') #CNTCT1EA51B7A7EFC475992EE32A22
pay_opt_input = CONFIG.get('ORDER', 'PAYMENT') #CRD170926122609387B1E5519C47D302

bankname_input = CONFIG.get('EMIOPTIONS', 'BANK')
tenure_input = CONFIG.get('EMIOPTIONS', 'TENURE')

#url = input()
#url = "https://www.flipkart.com/redmi-note-7-ruby-red-64-gb/p/itmfdzvfanddhqc7?pid=MOBFDXZ39VMKXZAA&lid=LSTMOBFDXZ39VMKXZAAAJKJYR&marketplace=FLIPKART&fm=personalisedRecommendation%2Fp2p-same&iid=R%3As%3Bp%3AMOBFDXZ376XRTZXH%3Bpt%3Ahp%3Buid%3Ae1401e5b-fa4c-90c6-31a2-de174d36e55e%3B.MOBFDXZ39VMKXZAA.LSTMOBFDXZ39VMKXZAAAJKJYR&ppt=HomePage&ppn=Home&ssid=9hhfdo0q4w0000001557248900979&otracker=hp_reco_Suggested%2Bfor%2BYou_1_10.productCard.PMU_V2_Redmi%2BNote%2B7%2B%2528Ruby%2BRed%252C%2B64%2BGB%2529_MOBFDXZ39VMKXZAA.LSTMOBFDXZ39VMKXZAAAJKJYR_personalisedRecommendation%2Fp2p-same_0&cid=MOBFDXZ39VMKXZAA.LSTMOBFDXZ39VMKXZAAAJKJYR"
url="https://www.flipkart.com/redmi-note-7-pro-neptune-blue-64-gb/p/itmfegkx8nbcze6t?pid=MOBFDXZ376XRTZXH&lid=LSTMOBFDXZ376XRTZXHWRK63O&marketplace=FLIPKART&sattr[]=color&sattr[]=storage&sattr[]=ram&st=color&otracker=search"

#print(url)
print('\nLogging in with username:',email_inp)
if pay_opt_input == 'EMI_OPTIONS':
    print('\nEMI Option Selected. \nBANK:',bankname_input,'\nTENURE:',tenure_input,'\n')
elif pay_opt_input == 'PHONEPE':
    print('\nPayment with Phonepay\n')
elif pay_opt_input == 'NET_OPTIONS':
    print('\nNet Banking Payment Selected\n')
elif pay_opt_input == 'COD':
    print('\nCash On Delivery Selected\n')
else:
    print('\nFull Payment Selected\n')
    
#input('Confirm Payment Details & Press Enter to proceed.')

driver = webdriver.Chrome(driver_path)
driver.maximize_window()
driver.get(url)

input('\nConfirm Payment Details above, Product Details on Browser & Press Enter to proceed.')

def login():
    try:
        print("Logging In..")
        try:
            login = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "._34niwY"))
            )
            print('Login Button Clickable')
        except:
            print('Login Button Not Clickable')
        login.click()
        print('Login Button Clicked Successfully')
    except:
        print('login Failed. Retrying.')
        time.sleep(0.5)	
        login()
        
def login_submit():
    try:
        if 'Enter Password' in driver.page_source:
            print('Trying Usual method of Login.')
            email = driver.find_element_by_css_selector(".Km0IJL ._2zrpKA")
            passd = driver.find_element_by_css_selector(".Km0IJL ._3v41xv")
            email.clear()
            passd.clear()
            email.send_keys(email_inp)
            passd.send_keys(pass_inp)
            try:
                form = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".Km0IJL ._7UHT_c"))
                )
                print('Submit Button Clickable')
            except:
                print('Submit Button Not Clickable')
            form.click()     
        else:
            print('Trying Alternate method of Login.')
            email = driver.find_element_by_css_selector("._2zrpKA")
            email.clear()
            email.send_keys(email_inp)
            loginnext = WebDriverWait(driver, 5).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, "._1LctnI"))
                        )
            loginnext.click()
            loginpassword = WebDriverWait(driver, 5).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, ".jUwFiZ"))
                        )
            loginpassword.click()
            time.sleep(0.5)
            passd = driver.find_elements_by_css_selector("._2zrpKA")[1]
            passd.clear()
            passd.send_keys(pass_inp)
            form = WebDriverWait(driver, 20).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, "._1LctnI"))
                        )
            form.click()
        print("Logged In Successfully")
    except:
        if ('Login &amp; Signup' not in driver.page_source and 'Login & Signup' not in driver.page_source):
            print('Logged in Manually.')
        else:
            print('login_submit Failed. Please login manually.')
            time.sleep(1)
            login_submit()

def buy_check():
    try:
        nobuyoption = True
        while nobuyoption:
            try:
                driver.refresh()
                time.sleep(0.2)
                buyprod = driver.find_element_by_css_selector("._1k1QCg ._7UHT_c")
                print('Buy Button Clickable')
                nobuyoption = False
            except:
                nobuyoption = True
                print('Buy Button Not Clickable')
        buyprod.click()
        print('Buy Button Clicked Successfully')
        buy_recheck()
    except:
        print('buy_check Failed. Retrying.')
        time.sleep(0.5)	
        buy_check()
        
def buy_recheck():        
    try:
        WebDriverWait(driver, 4).until(
            EC.title_contains("Secure Payment")
        )        
        print('Redirected to Payment')
    except:
        print('Error in Redirecting to Payment')
        time.sleep(0.5)	
        buy_check()
        
def deliver_option():
    try:
        addr_input_final = "//label[@for='"+addr_input+"']"
        try:
            sel_addr = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH,addr_input_final))
            )
            print('Address Selection Button Clickable')
        except:
            print('Address Selection Button Not Clickable')    
        sel_addr.click()
        print('Address Selection Button Clicked Successfully')
    except:
        print('deliver_option Failed. Retrying.')
        #time.sleep(0.5)	
        #deliver_option()
    
def deliver_continue():
    try:
        addr_sal_avl = True
        while addr_sal_avl:
            try:
                address_sel = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "._3K1hJZ ._7UHT_c"))
                )
                address_sel.click()
                addr_sal_avl = False
                print('Address Delivery Button Clickable')
            except:
                addr_sal_avl = True
                print('Address Delivery Button Not Clickable')
        print('Address Delivery Button Clicked Successfully')
    except:
        print('deliver_continue Failed. Retrying.')
        #time.sleep(0.5)	
        #deliver_continue()
        
def order_summary_continue():
    try:
        press_continue =  driver.find_element_by_css_selector("._2Q4i61")             
        press_continue.click()
        print('Continue Button Clicked Successfully')
    except:
        print('order_summary_continue Failed. Retrying.')
        #time.sleep(0.5)	
        #order_summary_continue()
        
def choose_payment():
    try:
        pay_opt_input_final = "//label[@for='"+pay_opt_input+"']"
        pay_method_sel = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, pay_opt_input_final)) )
        pay_method_sel.click()

        if pay_opt_input == 'EMI_OPTIONS':
            emi_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".B7BM8s"))
            )
            emi_button.click()
            time.sleep(0.5)
            card_name = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "'+bankname_input+'")]')) )
            card_name.click()
            time.sleep(0.5)
            emi_tenure = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//label[@for='"+tenure_input+"']")) )
            emi_tenure.click()
            time.sleep(0.5)
            continue_emi = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "._7UHT_c"))
            )
            continue_emi.click()
        print('Payment Method Selected Successfully')
    except:
        print('choose_payment Failed. Retrying.')
        #time.sleep(0.5)	
        #choose_payment()
        
def payment_cvv():
    try:
        payment_sel =  None
        payment_sel = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "._16qL6K"))
        )
        payment_sel.clear()
        payment_sel.send_keys(cvv_inp)
        print('CVV Entered:'+cvv_inp)
    except:
        print('payment_cvv Failed. Retrying.')
        #time.sleep(0.5)	
        #payment_cvv()
        
def payment_continue():
    try:
        pay =  None
        try:
            pay = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "._3K1hJZ ._7UHT_c"))
            )
            print('Pay Button Clickable')   
        except:
            print('Pay Button Not Clickable')        
        pay.click()
        print('Pay Button Clicked Successfully')
    except:
        print('payment_continue Failed. Retrying.')
        #time.sleep(0.5)	
        #payment_continue()
        
def otp_submit():
    try:
        otp = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "._3K1hJZ .l5dwor"))
            )
        otp.clear()
        print('Please enter OTP here:')
        otp_input = input()    
        otp.send_keys(otp_input)
                    
        submit_otp = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "._3K1hJZ ._7UHT_c"))
            )
        submit_otp.click()
        print('OTP Submitted Successfully')
    except:
        print('otp_submit Failed. Retrying.')
        #time.sleep(0.5)	
        #otp_submit()

def try_all():       
    login()
    login_submit()
    buy_check()
    deliver_option()
    deliver_continue()
    order_summary_continue()
    choose_payment()
    payment_cvv()
    payment_continue()
    otp_submit()

def try_till_otp():       
    login()
    login_submit()
    buy_check()
    deliver_option()
    deliver_continue()
    order_summary_continue()
    choose_payment()
    payment_cvv()
    payment_continue()
    #otp_submit()

def try_till_summary():       
    login()
    login_submit()
    buy_check()
    deliver_option()
    deliver_continue()
    order_summary_continue()

def try_initial():       
    login()
    login_submit()
    buy_check()


def try_buy_page():
    driver.refresh()
    buy_check()
    deliver_option()
    deliver_continue()
    order_summary_continue()
    choose_payment()
    payment_cvv()
    payment_continue()
    #otp_submit()
    
def try_payment_page():
    driver.refresh()
    deliver_option()
    deliver_continue()
    order_summary_continue()
    choose_payment()
    payment_cvv()
    payment_continue()
    #otp_submit()

if __name__ == "__main__":
    #try_all()
    try_till_otp()
    #try_payment_page()
    #try_buy_page()
    #try_till_summary()
    #try_initial()





