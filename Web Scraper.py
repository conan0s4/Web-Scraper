from bs4 import (BeautifulSoup)
import requests
import re


print(r"""
              

         
             SURFACE  x  DARK   W E B   S C R A P E R
             -----------------------------------------
         ⚙  Tor-enabled · Links · Usernames · Onion Links
[#]note: use proxychains or vpn when scraping.
[#]note: for dark web scraping , make sure tor service is running or open tor browser. 
""")

while True:
    getUrl = input("Target web >> ").strip()
    use_tor = input("Use Tor? [y/n] >> ").lower()
    time_out = int(input("input timeout >> "))
    if use_tor == 'y':
        proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }
        try:
            page = requests.get(getUrl, proxies=proxies, timeout=time_out)
            print("[+] Fetched via Tor")
            break
        except Exception as e:
            print(f"[!] Failed to fetch via Tor: {e}")
            continue
    elif use_tor == 'n':
        try:
            page = requests.get(getUrl, timeout=time_out)
            print("[+] Fetched without Tor")
            break
        except Exception as e:
            print(f"[!] Failed to fetch: {e}")
            continue
    else:
        print("[!] Invalid input. Please type 'y' or 'n'.")
        continue
soup = BeautifulSoup(page.text, 'html.parser')
soup.prettify()
text = (soup.get_text())




print("[+] Extracting all available data...")
print("-----------------------------------")

usernames = re.findall(r'@[\w._-]{3,}', text)
print("\n[+] Usernames found:")
for user in usernames:
    print(user)

links = [a.get('href') for a in soup.find_all('a') if a.get('href')]
print("\n[+] Links found:")
for link in links:
    print(link)

onionlinks = re.findall(r'https?://[a-z2-7]{16,56}\.onion[^\s]*', text)
print("\n[+] Onion Links found:")
for olink in onionlinks:
    print(olink)

emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
print("\n[+] Emails found:")
for email in emails:
    print(email)

ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', text)
print("\n[+] IPs found:")
for ip in ips:
    print(ip)

subdomains = re.findall(r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b', text)
print("\n[+] Subdomains found:")
for sub in subdomains:
    print(sub)

phones = re.findall(r'\+?\d[\d\s\-]{7,}\d', text)
print("\n[+] Phone numbers found:")
for phone in phones:
    print(phone)

domains = re.findall(r'\b[a-zA-Z0-9-]+\.(?:com|net|org|io|edu|gov|co|ph)\b', text)
print("\n[+] Domains found:")
for domain in domains:
    print(domain)

titles = soup.find_all(["h1", "h2", "h3", "title"])
print("\n[+] Titles found:")
for title in titles:
    print(title.get_text(strip=True))

comments = re.findall(r'<!--(.*?)-->', text, re.DOTALL)
print("\n[+] HTML Comments found:")
for comment in comments:
    print(comment.strip())







