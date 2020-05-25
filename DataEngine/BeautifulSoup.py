# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from dateutil import parser as date_parser
from cleanHtmlContent import *
import psycopg2
import datetime
from BeautifulSoup_Scripts import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def GetFromImageWithUrlTag(item):
    img = ""
    if item.image is None:
        img = ""
    else:
        if item.image.url is None:
            img = ""
        else:
            img = item.image.url.text
    return img


def GetFromImageTag(item):
    img = ""
    if item.image is None:
        img = ""
    else:
        img = item.image.text
    return img


def GetFromImage2Tag(item):
    img = ""
    if item.find("img640x360") is None:
        img = ""
    else:
        img = item.find("img640x360").text
    return img

def GetNoImage():
    return ""

def GetImageFromPage(SourceUrl):
    resp = requests.get(SourceUrl)
    soup = BeautifulSoup(resp.content, features="lxml")
    item = soup.find("div", {"class": "detailImg"})
    link = item.find("a" , recursive=False)
    img = link.find("img" , recursive=False).attrs["src"]
    return img

def GetImageFromPage_Takvim(SourceUrl):
    resp = requests.get(SourceUrl)
    soup = BeautifulSoup(resp.content, features="lxml")
    img = ""
    if soup.find("video", {"class":"vjs-tech"}) != None:
        print(SourceUrl)
        img = soup.find("video", {"class":"vjs-tech"}).attrs["poster"]
    elif soup.find("div", {"class":"figure"}) != None:
        img = soup.find("div", {"class":"figure"}).find("a" , recursive=False).attrs["href"]
    elif soup.find("img", {"id":"haberImg"}) != None:
        img = soup.find("img", {"id":"haberImg"}).attrs["src"]
    elif soup.find("article" , recursive=False) != None:
        img = soup.find("article").find("div").find("p").find("img").attrs["src"]
    elif soup.find("galleryItem" , recursive=False) != None:
        img = soup.find("galleryItem", {"data-order":"1"}).find("div").find("div").find("a").attrs["href"]
    elif soup.find("div", {"class":"video"}) != None:
        img = soup.find("div", {"class":"video"}).find("div").find("div").find("div").attrs["poster"]
    return img

def GetImageFromPage_YeniAsir(SourceUrl):
    resp = requests.get(SourceUrl)
    soup = BeautifulSoup(resp.content, features="lxml")
    img = ""
    if soup.find("img", {"id":"NewsImagePath"}) != None:
        img = soup.find("img", {"id":"NewsImagePath"}).attrs["src"]
    return img

def GetImageFromPage_YeniAkit(SourceUrl):
    resp = requests.get(SourceUrl)
    soup = BeautifulSoup(resp.content, features="lxml")
    item = soup.find("figure")
    link = item.find("div" , recursive=False)
    img = link.find("img" , recursive=False).attrs["src"]
    return img

def GetFromEnclosure(item):
    if item.image is None:
        if item.find("enclosure", {"type": "image/jpeg"}) == None:
            ii = ""
        else:
            ii = item.find("enclosure", {"type": "image/jpeg"}).attrs["url"]
    else:
        ii = item.image.url
    return ii


def GetFromMedia(item):
    if item.image is None:
        if item.find("media:thumbnail") == None:
            ii = ""
        else:
            ii = item.find("media:thumbnail").attrs["url"]
    else:
        ii = item.image.url
    return ii


def GetFromDescription(item):
    #print("GetFromDescription")
    # imageText = description[description.find("<img")+4:description.find("/>")-1]
    # imageSrc = imageText[imageText.find("src")+5:imageText.find(">")]
    return " "


def GetImageUrl(site, url, item):
    result = ""
    try:
        if site == 'A Haber': result = GetFromEnclosure(item)
        elif site == 'Milliyet': result = GetFromDescription(item)
        elif site == 'NTV': result =  GetFromDescription(item)
        elif site == 'Habertürk': result =  GetFromDescription(item)
        elif site == 'Yeni Şafak': result =  GetFromImageWithUrlTag(item)
        elif site == 'Sabah': result =  GetFromEnclosure(item)
        elif site == 'Hürriyet': result =  GetFromEnclosure(item)
        elif site == 'Star': result =  GetFromImageTag(item)
        elif site == 'Güneş': result =  GetFromImageTag(item)
        elif site == 'Dünya': result =  GetFromDescription(item)
        elif site == 'Vatan': result =  GetFromDescription(item)
        elif site == 'YeniAsya': result =  GetFromEnclosure(item)
        elif site == 'Cumhuriyet': result =  GetFromEnclosure(item)
        elif site == 'Haber7': result =  GetFromDescription(item)
        elif site == 'Takvim': result =  GetImageFromPage_Takvim(url)
        elif site == 'Milli Gazete': result =  GetFromEnclosure(item)
        elif site == 'Evrensel': result =  GetFromDescription(item)
        elif site == 'Yeni Akit': result =  GetImageFromPage_YeniAkit(url)
        elif site == 'Diriliş': result =  GetFromDescription(item)
        elif site == 'YeniÇağ': result =  GetFromDescription(item)
        elif site == 'Türkiye': result =  GetFromMedia(item)
        elif site == 'Yeni Asır': result =  GetImageFromPage_YeniAsir(url)
        elif site == 'Karar': result =  GetFromEnclosure(item)
        elif site == 'Yurt Gazetesi': result =  GetFromImageTag(item)
        elif site == 'YeniSöz': result =  GetFromEnclosure(item)
        elif site == 'EnSonHaber': result =  GetFromImageTag(item)
        elif site == 'InternetHaber': result =  GetNoImage()
        elif site == 'Onedio': result =  GetFromDescription(item)
        elif site == 'Mynet': result =  GetFromImage2Tag(item)
        elif site == 'CnnTurk': result =  GetFromImageTag(item)
        elif site == 'Sputnik Türkiye': result =  GetFromEnclosure(item)
        elif site == 'AA': result =  GetFromImageTag(item)
        elif site == 'Haberler': result =  GetFromImageTag(item)
        elif site == 'T24': result =  GetFromEnclosure(item)
        elif site == 'BloombergHT': result =  GetFromImageTag(item)
        elif site == 'Gaste24': result =  GetFromImageTag(item)
        #Akşam
        #Diriliş
        #karar
        #Onedio Gündem
        #mynet
        #Oda tv
        #Diken
        #AjansHAber
        #euronews
        #dw türkçen
        #ntv para
        #bigpara
        #tüsiad
        #ekonomist dergi
        #foreks haber
        #Müsiad
        #Investing Türkiye
        #Borsa Gündem
        #Finans Gündem
        #Uzman para
        #Dünya Finans
        #BusinessHT
        #eborsa haber7
        #paraanaliz
        #a para tv
        else: result = ""
    except Exception as e:
        print("image url error")
    return result

def get_news_data():
    print("GetNewsData running...")

    insert_news_category()
    insert_newsSite()

    UpdateData.DropNews()
    news_link = select_newsSite()

    #siteId, name, siteUrl, favicon, sourceUrl, isActive, categoryNumber
    
   
    fmt = "%Y-%m-%d %H:%M:%S"
    index = 0
    for x in news_link:
        try:
            resp = requests.get(x['sourceUrl'])
            soup = BeautifulSoup(resp.content, features="xml")
            items = soup.findAll('item')
            image_url = ""
            for item in items:
                try:
                    parsed_t = datetime.now()
                    image_url = GetImageUrl(x['name'], item.link.text, item)
                    insert_news(x['siteId'], cleanhtml(item.title.text).encode('utf-8').strip(), cleanhtml(item.description.text).encode('utf-8').strip(), item.link.text, image_url, parsed_t, 1, "", x['categoryNumber'], index)
                    index = index + 1
                except Exception as e:
                    image_url = GetImageUrl(x['name'], item.link.text, item)
                    insert_news(x['siteId'], cleanhtml(item.title.text).encode('utf-8').strip(), cleanhtml(item.description.text).encode('utf-8').strip(), item.link.text, image_url, str(datetime.now()), 1, "", x['categoryNumber'], index)
                    index = index + 1
        except Exception as e:
            print(cleanhtml(item.title.text).encode('utf-8').strip() + " : " + cleanhtml(item.description.text).encode('utf-8').strip() + " : " + str(e))
    print('GetNewsData run.')