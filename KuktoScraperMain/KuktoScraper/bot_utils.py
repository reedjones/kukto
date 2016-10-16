import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import random
import os

def make_headers():
    user_agents = [
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Opera/9.25 (Windows NT 5.1; U; en)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
        'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'
    ]
    headers = {}
    headers['User-Agent'] = random.choice(user_agents)
    return headers

p='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'


p3 = os.path.join('C:','Program Files (x86)','Google','Chrome','Application','chromedriver.exe')
p2 =  os.path.join('C:','Program Files (x86)','Google','Chrome','Application','chromedriver')

chromedriver = p3
os.environ["webdriver.chrome.driver"] = chromedriver

start_url = "http://www.teevee.sk/serialy/simpsonovci-1/1-vianoce-u-simpsonovcou#21056"
serial_start = 'http://www.teevee.sk/serialy/'

class ExaShare():
    username = 'kuktocz'
    password = 'chronic247'
    exashare = 'http://exashare.com/'
    my_files = 'http://www.exashare.com/users/kuktocz'


def make_exa():
    x = ExaShare()
    return x

priority = [
    'http://www.teevee.sk/serialy/american-horror-story',
    'http://www.teevee.sk/serialy/12monkeys',
    'http://www.teevee.sk/serialy/simpsonovci',
    'http://www.teevee.sk/serialy/the-walking-dead',
    'http://www.teevee.sk/serialy/true-blood',
    'http://www.teevee.sk/serialy/orphan-black',
    'http://www.teevee.sk/serialy/futurama',
    'http://www.teevee.sk/serialy/family-guy-griffinovi',
    'http://www.teevee.sk/serialy/doctor-who',
    'http://www.teevee.sk/serialy/californication',
    'http://www.teevee.sk/serialy/breaking-bad',
    'http://www.teevee.sk/serialy/house-of-cards',
    'http://www.teevee.sk/serialy/game-of-thrones-hra-o-trony',
    'http://www.teevee.sk/serialy/it-crowd',
    'http://www.teevee.sk/serialy/penny-dreadful',
    'http://www.teevee.sk/serialy/true-detective',
    'http://www.teevee.sk/serialy/lost-girl',
    'http://www.teevee.sk/serialy/south-park',
    'http://www.teevee.sk/serialy/revolution',
    'http://www.teevee.sk/serialy/scorpion'
]
others = []


def get_soup(url):
    headers = make_headers()
    req = urllib.request.Request(url, headers = headers)
    u = urllib.request.urlopen(req)
    soup = BeautifulSoup(u)
    u.close()
    return soup