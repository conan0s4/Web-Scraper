'''''''''
The web scraping process:

1. Identify the targeted website
2. Get the URL of the web where you want to extract data from
3. Request the URL’s to get the HTML of the webpage (for: .onion sites parse the request through tor)
4. Use locators (specify) to find the data in HTML
5. Save data in a JSON

//setup tor proxy
//dark web as option parse request to tor 

HTML  - hyper text markup language (describes all elements in a webpage)
manual inspection (right click(inspect)) ctrl + f  (see the structure)
-------------------------------------------------------
..find specific data
..find all data
example: 
soup.find_all('tr', class_='col-md-12')
soup.find('author').text.strip() #.text (if you want to extract texts) # .strip (cleans it out)
note: find all doesn't have a text attribute
-------------------------------------------------------
note: Target data
Links
Username
______________________________________________________
'''''''''
#[0.1]packages
from bs4 import (BeautifulSoup) #for parsing html
import requests  # for making http request
import re #RegEx - search and extract specific patterns of text
#____________________________________________________________________
print(r"""
              

         
             SURFACE  x  DARK   W E B   S C R A P E R
             -----------------------------------------
         ⚙  Tor-enabled · Links · Usernames · Onion Links
[#]note: use proxychains or vpn when scraping.
[#]note: for dark web scraping , make sure tor service is running or open tor browser. 
""")

# r - do not \ as escape characters
while True: # error handler for both user inputs
    # [1.1] Get target web (page) w/ error handler
    getUrl = input("Target web >> ").strip()
    # [1.2] if surface or dark web use
    use_tor = input("Use Tor? [y/n] >> ").lower()  # lowercase
    time_out = int(input("input timeout >> "))


    if use_tor == 'y':  # if yes # [2.2] parse Request through tor to the URL (get HTML) (routes http request through tor by setting up a proxy)
        proxies = {  # If the user chooses Tor, set up the SOCKS5 proxy
            'http': 'socks5h://127.0.0.1:9050',  # listens locally to port 9050
            'https': 'socks5h://127.0.0.1:9050'
        }  # The socks 5h:// scheme ensures DNS resolution is done through Tor
        try:  # sends requests to tor network
            page = requests.get(getUrl, proxies=proxies, timeout=time_out)  # limits (timeout=10)
            print("[+] Fetched via Tor")  # confirms to user
            break
        except Exception as e:  # error handler (if went above that (10) then user will prompted) (could be: web is down)
            print(f"[!] Failed to fetch via Tor: {e}")
            continue
    elif use_tor == 'n':  # if no # [2.2] Request to the URL (get HTML)
        try:  # sent requests directly to target web page on regular connection
            page = requests.get(getUrl, timeout=time_out)
            print("[+] Fetched without Tor")  # limits (timeout=10)
            break
        except Exception as e:  # error handler (if went above that (10) then user will prompted) (could be: web is down)
            print(f"[!] Failed to fetch: {e}")
            continue
    else:  # error handler (none of the options where inputted)
        print("[!] Invalid input. Please type 'y' or 'n'.")
        continue




#____________________________________________________________________
#[3.1]retreives the raw html (parses the information in an html format)
soup = BeautifulSoup(page.text, 'html.parser')
#[3.1]makes the html more readable
soup.prettify()
#____________________________________________________________________

''''
get all text within the page then find all 
this specifics (substrings start with @ followed by atleast 3/more char that can be 
w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
.  _ -          (patterns)) 
within the text that we got
'''''

text = (soup.get_text()) # get all text in the html
print("---------------------------------------")
print("|data: (usernames) (links) (onionlinks)|")
print("---------------------------------------")
while True: # for error handling so that user can't proceed until he enters the right input that was given
    target_data = input("Specify target data >> ")

    if target_data == "usernames":
        # [4.1] Extract usernames (e.g., @username)
        usernames = re.findall(r'@[\w._-]{3,}', text)  # uses RegEx
        print("\n[+] Usernames found:")
        for user in usernames:  # for every user found in the usernames print it out
            print(user)


    elif target_data == "links":
        # [4.2] Extract all links
        links = [a.get('href') for a in soup.find_all('a') if a.get('href')]
        print("\n[+] Links found:")
        for link in links:
            print(link)



    elif target_data == "onionlinks":
        # [4.2] Extract all onion links
        onionlinks = re.findall(r'https?://[a-z2-7]{16,56}\.onion[^\s]*', text)
        print("\n[+] Onion Links found:")
        for olink in onionlinks:
            print(onionlinks)










