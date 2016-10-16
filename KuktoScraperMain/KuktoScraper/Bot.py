"""
TEEVEE.SK CRAWLER 2014.
Reed Jones
-------------------------------------------------------------->
"""

import json
import urllib.request
from urllib.request import Request, urlopen
from time import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#from kukto.series.models import NewShow
#from kukto.Schemas.models import Season ,Episode, TVSeries
import re
import random
import pickle
from time import sleep
import os.path
import os
import sys
from selenium.webdriver.support.ui import Select
from KuktoScraper.bot_utils import make_headers, make_exa, ExaShare, others, p, p2, p3, priority, start_url, serial_start, get_soup
from Uploaded import scraper as upload_site

chromedriver = p3
os.environ["webdriver.chrome.driver"] = chromedriver


def get_all_starts():
    if os.path.isfile('all_links.pickle'):
        print('loading from file')
        with open("all_links.p", "rb") as f:
            data = pickle.load(f)
            return data

    else:
        print('fetching links')
        links = []
        info = []
        soup = get_soup(serial_start)
        content = soup.find('div', class_='content')
        t = content.find('table')
        tds = t.find_all('td')
        i = 0
        while i < len(tds):
            current = tds[i]
            all_links = current.find_all('a', href=True)
            for link in all_links:
                links.append(link['href'])
                show = {
                    'title': link.text,
                    'link': link['href']
                }
                info.append(show)
            i += 1

        with open("all_links.p", "wb") as f:
            pickle.dump([links, info], f)

        return [links, info]


def get_episode_title(url):
    soup = get_soup(url)
    d = soup.find('div', class_='circles')
    episode_n = d.find_previous('h1')
    episode_name = episode_n.text

    title = d.find_next('h2')
    t = title.text
    ti = t.replace('EPIZÃ“DA: ', '').replace('EPIZÓDA:', '')
    title = ti.replace(' ', '')
    season = title[0:2]
    episode_num = title[3:5]
    m = {
        'title': episode_name,
        'season': season,
        'episode_num': episode_num
    }
    return m


def get_next_one(url):
    soup = get_soup(url)
    t = soup.find('p', class_='video_text')
    if t is not None:
        a = t.find_next('a', class_='video_mistake blue')
        if a is not None:
            return a['href']
        else:
            return None
    else:
        print('show text was none, looking straight for link')
        a = soup.find_all('a', class_='video_mistake blue')
        if len(a) > 1:
            for i in a:
                if i.text == 'Novšia epizóda':
                    correct = i['href']
                    return correct
        else:
            return a[0]['href']
    return None


def get_video_one(soup):
    cont = soup.find('div', class_='video_cont')


def get_frame(url):
    driver = webdriver.Chrome(executable_path=p)
    driver.get(url)

    ready = False
    start = time()
    while not ready:
        print('waiting')
        sleep(15)
        source = driver.page_source
        #todo check how long its been waiting and stop if too long, also but a random wait time so it doesn't loop so much
        elapsed = (time() - start)
        print("%s time ellapsed" % (elapsed))
        if not ready:
            soup = BeautifulSoup(source)
            cont = soup.find('div', class_='video_cont')
            frame = cont.find_next('iframe')
            print('frame found %s' % frame)
            if frame is not None:
                if 'facebook' in frame['src']:
                    print('facebook found in src')
                    print(frame['src'])
                elif 'exashare' in frame['src']:
                    print('its ok %s' % frame['src'])
                    ready = True
                else:
                    ready = True
    driver.close()
    driver.quit()
    return frame


def get_chrome():
    i = 0
    driver = None
    while driver is None:
        try:
            driver = webdriver.Chrome(executable_path=p)
        except:
            i += 1
            print('problem with driver,trying again...# of attempts %s' % i)
            try:
                driver = webdriver.Chrome(executable_path=p3)
            except:
                i += 1
                print('problem with driver,trying again...# of attempts %s' % i)
                try:
                    driver = webdriver.Chrome(executable_path=p2)
                except:
                    i += 1
                    print('problem with driver,trying again...# of attempts %s' % i)
                    try:
                        chromedriver = p2
                        os.environ["webdriver.chrome.driver"] = chromedriver
                        driver = webdriver.Chrome(executable_path=chromedriver)
                    except:
                        print('problem with driver,trying again...# of attempts %s' % i)
                        try:
                            print('shit is fucked trying to use firefox')
                            driver = webdriver.Firefox()
                        except:
                            print('firefox failed')
                            try:
                                driver = webdriver.Chrome(p2)
                            except:
                                try:
                                    print('last chance')
                                    driver = webdriver.Chrome(executable_path=p2)
                                except:
                                    print('total failure \n you blew it <-------')

        if i > 20:
            print('time out on finding driver exiting program')
            sys.exit()
    return driver


def get_via_chrome(url, wanted):
    driver = get_chrome()
    driver.get(url)
    source = driver.page_source
    ready = False
    start = time()
    while not ready:
        elapsed = (time() - start)
        print("%s time ellapsed" % (elapsed))
        if not ready:
            soup = BeautifulSoup(source)
            content = soup.find(wanted[0], wanted[1])
            if content is not None:
                ready = True
    driver.close()
    driver.quit()
    return content


def get_season_links(url, get_all):
    driver = get_chrome()
    driver.get(url)
    links = driver.find_elements_by_css_selector('a.hl')
    if get_all:
        i = 0
        all_season_links = []

        while i < len(links):
            if i == 0:
                current_menu = 1
            else:
                current_menu = i
            menu = 'submenu' + str(current_menu)
            got_menu = False
            current = links[i]
            current.click()
            sleep(10)
            source = driver.page_source
            soup = BeautifulSoup(source)
            d = soup.find('div', id=menu)
            if not d:
                pass
            else:
                all_links = d.find_all('a', href=True)
                for link in all_links:
                    all_season_links.append(link['href'])
            i += 1
        driver.close()
        driver.quit()
        return all_season_links

    links[0].click()
    sleep(15)

    source = driver.page_source
    soup = BeautifulSoup(source)
    d = soup.find('div', id='submenu1')

    first_episode = d.find_next('a', href=True)
    if first_episode is not None:
        driver.close()
        driver.quit()
        return first_episode['href']
    else:
        print('no episode @ get season episodes')
        driver.close()
        driver.quit()
        return None


def exa_share_start(link):
    e = ExaShare()
    driver = get_chrome()
    driver.get(e.exashare)
    login_form = driver.find_element_by_xpath("//form[@name='FL']")
    username = driver.find_element_by_xpath("//input[@name='login']")
    password = driver.find_element_by_xpath("//input[@name='password']")
    stay = driver.find_element_by_xpath("//input[@name='Field']")
    stay.click()
    username.send_keys('kuktocz')
    password.send_keys('chronic247')
    username.submit()
    upload_url = 'http://www.exashare.com/?op=upload_url'
    driver.get(upload_url)
    url_space = driver.find_element_by_xpath("//textarea[@name='urls']")
    url_space.send_keys(link)
    try:
        url_space.submit()
    except:
        sub_button = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div/div[2]/form/div/div[3]/input")
        sub_button.click()
    sleep(30)
    source = driver.page_source
    soup = BeautifulSoup(source)

    hh = soup.find('h3', text='Your Cloning URL uploads')
    tbody = hh.find_next('tbody')
    td = tbody.find_next('td')
    if 'exashare' in td.text:
        e = 'http://www.exashare.com/embed-ke712l52y9wd-960x540.html'
        f = 'http://exashare.com/ke712l52y9wd'
        exa_link = td.text
        cleaned = exa_link.replace('http://www.exashare.com/', '')
        embed_url = 'http://www.exashare.com/embed-' + cleaned + '-960x540.html'
        driver.close()
        driver.quit()
        return embed_url
    else:
        #problem fix it ;)
        print('ERROR NO EXASHARE LINK FOUND!!!! <-------')
        driver.close()
        driver.quit()
        return None


def do_priorities():
    #continue_show = True
    all_link = get_all_starts()
    all_links = all_link[1] # {title and link}
    link_count = 0
    #episodes_count = 0
    episode_pages = []

    while link_count < len(all_links):
        first_time = True
        episodes_count = 0
        continue_show = True

        current_link = all_links[link_count]['link']
        current_show_title = all_links[link_count]['title']
        final_show = {
            'show_title': current_show_title,
            'seasons': [],
            'episodes': []
        }

        if current_link in priority:

            while continue_show:

                if first_time:

                    first_page = get_season_links(current_link, False) #returns the first episode link

                    print('first time and page is %s' % first_page)

                    if first_page:
                        episode_pages.append(first_page)
                    else:
                        #first_page was none ERROR
                        pass
                else:
                    #doesn't matter
                    pass

                current_page = episode_pages[episodes_count]
                print('currently on page %s' % current_page)

                next_url = get_next_one(current_page)
                print('next url is %s' % next_url)

                info = get_episode_title(current_page) #{title season episode_num}
                frame = get_frame(current_page) #frame['src']
                frame_src = frame['src']
                print('frame found %s' % frame_src) # ERROR

                if info['season'] not in final_show['seasons']:
                    season_info = {
                        'partOfSeries': current_show_title,
                        'numberOfEpisodes': None,
                        'number': info['season']
                    }
                    final_show['seasons'].append(season_info)
                else:
                    #seaon already there doesn't matter
                    pass

                episode_info = {
                    'link': frame_src,
                    'title': info['title'],
                    'season': info['season'],
                    'number': info['episode_num']
                }
                final_show['episodes'].append(episode_info)

                #TODO GO TO EXASHARE LINK -> GET FILE TITLE -> UPLOAD TO EXASHARE -> WAIT -> GET FILE TITLE -> FINAL LINK = THAT LINK
                #TODO CREATE NEW SHOW IF NOT EXSISTS -> NEW EPISODE ->SEASON-> ETC... -> SAVE TO DB

                if next_url is not None:
                    #is still next
                    #append to
                    episode_pages.append(next_url)
                    episodes_count += 1
                    first_time = False
                    print('moving to next url %s' % episodes_count + 'pages completed')

                else:
                    #next_url is None
                    episode_pages = []
                    episodes_count = 0
                    continue_show = False
                    link_count += 1
                    print('finished the show %s' % current_show_title + '%s' % link_count + 'out of %s' % len(
                        all_links) + ' completed')

            print('looped %s times at continue_show' % link_count)
            #end continue_show

        else:

            # Isn't a priority
            pass

    #end while link count
    print('looped %s times at while link_count' % link_count)


def main():
    all_links = get_all_starts()[1]
    link_count = 0
    shows = []
    episodes = []
    episode_count = 0
    episode_pages = []
    while link_count < len(all_links):

        current_link = all_links[link_count]['link']
        current_show_title = all_links[link_count]['title']
        final_show = {
            'show_title': current_show_title,
            'seasons': [],
            'episodes': []
        }

        first_page = get_season_links(current_link, False) #get first page
        episode_pages.append(first_page)

        current_url = episode_pages[episode_count]

        next_url = get_next_one(current_url)
        print('next url {0} \n current url {1}'.format(next_url, current_url))

        info = get_episode_title(current_url) #{title season episode_num}
        frame = get_frame(current_url) #frame['src']
        frame_src = frame['src']
        print('frame found %s' % frame_src) # ERROR

        if info['season'] not in final_show['seasons']:
            season_info = {
                'partOfSeries': current_show_title,
                'numberOfEpisodes': None,
                'number': info['season']
            }
            final_show['seasons'].append(season_info)

        episode_info = {
            'link': frame_src,
            'title': info['title'],
            'season': info['season'],
            'number': info['episode_num']
        }
        final_show['episodes'].append(episode_info)

        print(final_show)
        fs_link = final_show['episodes'][0]['link']
        real_final_link = exa_share_start(fs_link)
        if real_final_link is None:
            print('No link')
        print(real_final_link)

        download_link = upload_site.get_uploaded_link(real_final_link)
        print(download_link)
        sleep(60)

#from KuktoScraper import Bot as bot
#http://www.exashare.com/dfiy5fo07wzo
from Uploaded.scraper import get_uploaded_link_three
def uploader_test():
    driver = get_chrome()
    download_link = get_uploaded_link_three('http://www.exashare.com/dfiy5fo07wzo',driver)
    print('download link {0}'.format(download_link))

