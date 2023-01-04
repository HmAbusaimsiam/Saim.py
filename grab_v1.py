import requests
from bs4 import BeautifulSoup
import re
from concurrent.futures import ThreadPoolExecutor

all_domain = 0
paste = lambda x, y : print("[*] Page [>] {}\n[*] Total [>] {}\n\n".format(str(x), str(y)))

headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    }

def parse(text, filename):
    global all_domain
    try:
        soup = BeautifulSoup(text, "html.parser")
        q = soup.find("ul", class_="domains-tag-page")
        w = q.find_all("li")
        for e in w:
            r = e.text
            if " - " in r:
                domain = re.sub(" - .*", "", r)
            else:
                domain = r
            all_domain += 1
            with open(filename, "a") as f:
                f.write(domain+"\n")
                f.close()
    except Exception as e:
        print(str(e))

def get_resp(date=""):
    if date == "":
        api = "https://www.uidomains.com/not-available-domains/{}/"
        file = "newly_domains.txt"
    else:
        api = "https://www.uidomains.com/browse-daily-domains-difference/{}/"+date+"/"
        file = date+"_domains.txt"
    page = 1
    while True:
        try:
            resp = requests.get(api.format(str(page)), headers=headers, timeout=70).text
            if "nextPage" in resp:
                parse(resp, file)
                paste(page, all_domain)
                page += 1
            else:
                print("[*] Page Ended")
                break
        except Exception as e:
            print(str(e))
            break

def main():
    print("""
    1. Grab From Date (yyyy-mm-dd)
    2. Grab From Un-Available Domains
""")
    chose = int(input("Choose ~# "))
    if chose == 1:
        dat = input("Input Date ~# ")
        work = get_resp(date=dat)
    elif chose == 2:
        work = get_resp()
    else:
        print("Wrong Choose")
    with ThreadPoolExecutor(max_workers=10) as exc:
        exc.submit(work)
        exc.shutdown(wait=True)
main()