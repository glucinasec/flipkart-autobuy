# flipkart-autobuy

Automated program to buy Flipkart products in flash sale online. 
Specifically to buy products which go out of sale in a fraction of seconds and are too difficult to buy manually.

Steps to run this script:
1. Clone or download this repository `git clone https://github.com/atultherajput/flipkart-autobuy.git`
2. Do `cd flipkart-autobuy`
3. Run `python3 -m venv appvenv`
`source appvenv/bin/activate`
4. Run `pip install -r requirements.txt`
5. Download the correct [chromedriver](http://chromedriver.chromium.org/downloads) for you operating system (Linux/OSX/Windows), put the chromedriver in this project directory.
6. Set path of  chromedriver in config.ini file.
7. Enter your email and password in config.ini file.
8. Enter flipkart product URL in config.ini file.
9. Enter your saved card CVV in config.ini file.
7. Run `python app.py`

Note:
Make sure to have only one address in your flipkart account and only one card saved. Remove all extra credit and debit card from flipkart and phonepe account.

More payment options coming soon (Currently only supports card payment).

Forked from [flipkart-autobuy-old](https://github.com/atultherajput/flipkart-autobuy-old)
