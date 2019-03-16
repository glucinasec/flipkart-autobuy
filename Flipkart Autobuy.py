from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print('Flipkart URL:')
url = input()
#url = "https://www.flipkart.com/crazyink-sqcricketer-key-chain/p/itmf4huyhtfzkpun?pid=KECF4HQVQS8ZH4D4&lid=LSTKECF4HQVQS8ZH4D4PD6NIO&marketplace=FLIPKART&srno=b_1_3&otracker=hp_omu_Deals%20of%20the%20Day_1_Starting%20%40%20%E2%82%B966_CFFNJG01YDH2_0&fm=organic&iid=d6521f47-d5a7-46c5-a7ce-68a222a98afc.KECF4HQVQS8ZH4D4.SEARCH"

email_inp = "abc@gmail.com"
pass_inp = "xyz"
cvv_inp  = "123"

addr_input  = "CNTCT1EA51B7A7EFC475992EE32A22"
pay_opt_input = "CRD170926122609387B1E5519C47D302"

print(url)

driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.maximize_window()
driver.get(url)

def login():
    try:
        print("Logging In..")
        try:
            login = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "._1jJkOg"))
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
        print("Logged In Successfully")
    except:
        print('login_submit Failed. Retrying.')
        time.sleep(0.5)	
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
    try_all()
    try_till_otp()
    #try_payment_page()
    #try_buy_page()




