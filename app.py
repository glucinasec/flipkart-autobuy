from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from configparser import ConfigParser

CONFIG = ConfigParser()
CONFIG.read('config.ini')

driver_path = CONFIG.get('MAIN', 'DRIVER_LOCATION') 
email_inp = CONFIG.get('CREDENTIALS', 'USERNAME')
pass_inp = CONFIG.get('CREDENTIALS', 'PASSWORD')
cvv_inp = CONFIG.get('ORDER', 'CVV') 
addr_input = CONFIG.get('ORDER', 'ADDRESS')
pay_opt_input = CONFIG.get('ORDER', 'PAYMENT')

bankname_input = CONFIG.get('EMIOPTIONS', 'BANK')
tenure_input = CONFIG.get('EMIOPTIONS', 'TENURE')

url= CONFIG.get('ORDER', 'URL')

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
        
def order_summary_continue():
    try:
        press_continue =  driver.find_element_by_css_selector("._2Q4i61")             
        press_continue.click()
        print('Continue Button Clicked Successfully')
    except:
        print('order_summary_continue Failed. Retrying.')
        
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
        time.sleep(0.5)	
        payment_continue()
        
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

def run_script():
    login()
    login_submit()
    buy_check()
    order_summary_continue()
    payment_cvv()
    payment_continue()

if __name__ == "__main__":
   run_script()
