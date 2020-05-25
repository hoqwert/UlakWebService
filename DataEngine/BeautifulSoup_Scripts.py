# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import parser as date_parser
from cleanHtmlContent import *
from Business import AddData,GetData,UpdateData


def AddSite(id, name, siteUrl, favicon, sourceUrl, isActive, category):
    AddData.Site(id, name, siteUrl, favicon, sourceUrl, isActive, category)

def AddCategory(id, name, color):
    AddData.Category(id, name, color)
    
def insert_news_category():
    AddCategory(1, 'Dünya', '#007ABF')
    AddCategory(2, 'Ekonomi', '#34CAD6')
    AddCategory(3, 'Siyaset', '#F7382D')
    AddCategory(4, 'Gündem', '#88A824')
    AddCategory(5, 'Son Dakika', '#FD5015')
    AddCategory(6, 'Anasayfa', '#FE6E23')
    AddCategory(7, 'Manşet', '#FE6E23')
    AddCategory(8, 'Yazarlar', '#EBD20C')

def insert_newsSite():
        AddSite(1, 'A Haber','http://www.ahaber.com.tr' ,'ahaber' , 'https://www.ahaber.com.tr/rss/gundem.xml',1, 4)
        AddSite(1, 'A Haber','http://www.ahaber.com.tr' ,'ahaber' , 'https://www.ahaber.com.tr/rss/anasayfa.xml',1, 6)
        AddSite(1, 'A Haber','http://www.ahaber.com.tr' ,'ahaber' , 'https://www.ahaber.com.tr/rss/ekonomi.xml',1, 2)
        AddSite(1, 'A Haber','http://www.ahaber.com.tr' ,'ahaber' , 'https://www.ahaber.com.tr/rss/dunya.xml',1, 1)
        AddSite(1, 'A Haber','http://www.ahaber.com.tr' ,'ahaber' , 'https://www.ahaber.com.tr/rss/haberler.xml',1, 7)

        AddSite(2, 'Cnn Türk','https://www.cnnturk.com', 'cnnturk', 'https://www.cnnturk.com/feed/rss/news',1, 4)

        AddSite(3, 'Cumhuriyet','http://www.cumhuriyet.com.tr', 'http://www.cumhuriyet.com.tr/favicon.ico', 'http://www.cumhuriyet.com.tr/rss/son_dakika.xml',1, 5)
        AddSite(3, 'Cumhuriyet','http://www.cumhuriyet.com.tr', 'http://www.cumhuriyet.com.tr/favicon.ico', 'http://www.cumhuriyet.com.tr/rss/1.xml',1, 6)
        AddSite(3, 'Cumhuriyet','http://www.cumhuriyet.com.tr', 'http://www.cumhuriyet.com.tr/favicon.ico', 'http://www.cumhuriyet.com.tr/rss/5.xml',1, 1)
        AddSite(3, 'Cumhuriyet','http://www.cumhuriyet.com.tr', 'http://www.cumhuriyet.com.tr/favicon.ico', 'http://www.cumhuriyet.com.tr/rss/6.xml',1, 2)
        AddSite(3, 'Cumhuriyet','http://www.cumhuriyet.com.tr', 'http://www.cumhuriyet.com.tr/favicon.ico', 'http://www.cumhuriyet.com.tr/rss/2.xml',1, 7)

        AddSite(4, 'Dünya', 'https://www.dunya.com', 'dunya', 'https://www.dunya.com/rss', 1, 4)

        AddSite(5, 'Diriliş', 'http://www.dirilishaber.org', 'dirilishaber', 'http://www.dirilishaber.org/rss/gundem/5.xml',1, 4)

        AddSite(6, 'Evrensel','https://www.evrensel.net', 'evrensel', 'https://www.evrensel.net/rss/haber.xml',1, 4)
        AddSite(6, 'Evrensel','https://www.evrensel.net', 'evrensel', 'https://www.evrensel.net/rss/haber_guncel.xml',1, 4)
        AddSite(6, 'Evrensel','https://www.evrensel.net', 'evrensel', 'https://www.evrensel.net/rss/haber_ekonomi.xml',1, 2)
        AddSite(6, 'Evrensel','https://www.evrensel.net', 'evrensel', 'https://www.evrensel.net/rss/haber_politika.xml',1, 3)
        AddSite(7, 'En Son Haber','http://www.ensonhaber.com', 'ensonhaber', 'http://www.ensonhaber.com/rss/ensonhaber.xml',1, 4)
        #hata verdi#AddSite(8, 'Güneş','http://www.gunes.com', 'http://www.gunes.com/favicon.ico', 'http://www.gunes.com/XmlRss',1, 4)

        AddSite(9, 'Hürriyet','http://www.hurriyet.com.tr', 'hurriyet', 'http://www.hurriyet.com.tr/rss/gundem', 1, 4)
        AddSite(9, 'Hürriyet','http://www.hurriyet.com.tr', 'hurriyet', 'http://www.hurriyet.com.tr/rss/anasayfa', 1, 6)
        AddSite(9, 'Hürriyet','http://www.hurriyet.com.tr', 'hurriyet', 'http://www.hurriyet.com.tr/rss/ekonomi', 1, 2)

        # AddSite(10, 'Haber7', 'http://sondakika.haber7.com/sondakika.rss',1)
        # AddSite(11, 'Habertürk', 'https://www.haberturk.com/rss/manset.xml',1)
        AddSite(12, 'Haberler', 'https://www.haberler.com', 'haberler', 'https://rss.haberler.com/rss.asp?kategori=sondakika',1, 5)
        # AddSite(13, 'InternetHaber', 'http://www.internethaber.com/rss',1)
        #AddSite(14, 'Karar','http://www.karar.com', 'http://www.karar.com/favicon.ico', 'http://www.karar.com/rss/otomatik-rss',1, 4)
        AddSite(15, 'Milliyet','http://www.milliyet.com.tr', 'milliyet', 'http://www.milliyet.com.tr/rss/rssNew/gundemRss.xml',1, 4)
        AddSite(15, 'Milliyet','http://www.milliyet.com.tr', 'milliyet', 'http://www.milliyet.com.tr/rss/rssNew/ekonomiRss.xml',1, 2)
        AddSite(15, 'Milliyet','http://www.milliyet.com.tr', 'milliyet', 'http://www.milliyet.com.tr/rss/rssNew/siyasetRss.xml',1, 3)
        AddSite(16, 'Ntv','https://www.ntv.com.tr', 'ntv', 'https://www.ntv.com.tr/gundem.rss',1, 4)
        AddSite(16, 'Ntv','https://www.ntv.com.tr', 'ntv', 'https://www.ntv.com.tr/ekonomi.rss',1, 4)
        AddSite(16, 'Ntv','https://www.ntv.com.tr', 'ntv', 'https://www.ntv.com.tr/dunya.rss',1, 4)
        AddSite(16, 'Ntv','https://www.ntv.com.tr', 'ntv', 'https://www.ntv.com.tr/turkiye.rss',1, 4)
        AddSite(17, 'Mynet','https://www.mynet.com', 'mynet', 'http://www.mynet.com/haber/rss/son-dakika',1, 5)
        AddSite(18, 'Milli Gazete', 'https://www.milligazete.com.tr', 'milligazete',  'https://www.milligazete.com.tr/rss',1, 4)
        AddSite(19, 'Onedio', 'https://onedio.com', 'onedio', 'https://onedio.com/support/rss.xml?category=50187b5d295c043264000144',1, 4)
        # AddSite(20, 'Türkiye', 'http://www.turkiyegazetesi.com.tr/rss/rss.xml',1)

        AddSite(21, 'Takvim', 'https://www.takvim.com.tr', 'takvim', 'https://www.takvim.com.tr/rss/son24saat.xml',1, 4)
        AddSite(21, 'Takvim', 'https://www.takvim.com.tr', 'takvim', 'https://www.takvim.com.tr/rss/ekonomi.xml',1, 2)
        AddSite(21, 'Takvim', 'https://www.takvim.com.tr', 'takvim', 'https://www.takvim.com.tr/rss/anasayfa.xml',1, 6)
        AddSite(21, 'Takvim', 'https://www.takvim.com.tr', 'takvim', 'https://www.takvim.com.tr/rss/guncel.xml',1, 4)
        #AddSite(21, 'Takvim', 'https://www.takvim.com.tr', 'https://www.takvim.com.tr/favicon.ico', 'https://www.takvim.com.tr/rss/yazarlar.xml',1, 8)

        AddSite(22, 'Star','http://www.star.com.tr', 'star', 'http://www.star.com.tr/rss/sondakika.xml',1, 5)
        AddSite(22, 'Star','http://www.star.com.tr', 'star', 'http://www.star.com.tr/rss/mansetler.xml',1, 4)
        #yazar# AddSite(22, 'Star','http://www.star.com.tr', 'http://www.star.com.tr/favicon.ico', 'http://www.star.com.tr/rss/yazarlar.xml',1, 8)
        AddSite(22, 'Star','http://www.star.com.tr', 'star', 'http://www.star.com.tr/rss/guncel.xml',1, 4)
        AddSite(22, 'Star','http://www.star.com.tr', 'star', 'http://www.star.com.tr/rss/politika.xml',1, 3)
        AddSite(22, 'Star','http://www.star.com.tr', 'star', 'http://www.star.com.tr/rss/dunya.xml',1, 1)

        AddSite(23, 'Sputnik Türkiye','https://tr.sputniknews.com', 'sputniktr', 'https://tr.sputniknews.com/export/rss2/archive/index.xml',1, 4)

        AddSite(24, 'Sabah','https://www.sabah.com.tr', 'sabah', 'https://www.sabah.com.tr/rss/gundem.xml',1, 4)
        AddSite(24, 'Sabah','https://www.sabah.com.tr', 'sabah', 'https://www.sabah.com.tr/rss/ekonomi.xml',1, 2)
        AddSite(24, 'Sabah','https://www.sabah.com.tr', 'sabah', 'https://www.sabah.com.tr/rss/dunya.xml',1, 1)
        AddSite(24, 'Sabah','https://www.sabah.com.tr', 'sabah', 'https://www.sabah.com.tr/rss/anasayfa.xml',1, 6)
        AddSite(24, 'Sabah','https://www.sabah.com.tr', 'sabah', 'https://www.sabah.com.tr/rss/sondakika.xml',1, 5)

        #"Unknown string format:", timestr# AddSite(25, 'Vatan', 'gazetevatan', 'http://www.gazetevatan.com/favicon.ico', 'http://www.gazetevatan.com/rss/gundem.xml',1, 4)
        #"Unknown string format:", timestr# AddSite(25, 'Vatan', 'gazetevatan', 'http://www.gazetevatan.com/favicon.ico', 'http://www.gazetevatan.com/rss/ekonomi.xml',1, 2)
        #"Unknown string format:", timestr# AddSite(25, 'Vatan', 'gazetevatan', 'http://www.gazetevatan.com/favicon.ico', 'http://www.gazetevatan.com/rss/dunya.xml',1, 1)

        AddSite(26, 'Yeni Asya','http://www.yeniasya.com.tr', 'yeniasya', 'http://www.yeniasya.com.tr/rss/manset',1, 7)
        AddSite(26, 'Yeni Asya','http://www.yeniasya.com.tr', 'yeniasya', 'http://www.yeniasya.com.tr/rss/son-dakika',1, 5)
        AddSite(26, 'Yeni Asya','http://www.yeniasya.com.tr', 'yeniasya', 'http://www.yeniasya.com.tr/rss/gundem',1, 4)
        AddSite(26, 'Yeni Asya','http://www.yeniasya.com.tr', 'yeniasya', 'http://www.yeniasya.com.tr/rss/yurt-haber',1, 4)
        AddSite(26, 'Yeni Asya','http://www.yeniasya.com.tr', 'yeniasya', 'http://www.yeniasya.com.tr/rss/dunya',1, 1)
        AddSite(26, 'Yeni Asya','http://www.yeniasya.com.tr', 'yeniasya', 'http://www.yeniasya.com.tr/rss/politika',1, 6)
        #AddSite(26, 'YeniAsya','http://www.yeniasya.com.tr', 'yeniasya', 'http://www.yeniasya.com.tr/rss/yazarlar',1, 8)

        AddSite(27, 'Yeni Şafak','https://www.yenisafak.com', 'yeni_safak', 'https://www.yenisafak.com/Rss',1, 6)
        AddSite(27, 'Yeni Şafak','https://www.yenisafak.com', 'yeni_safak', 'https://www.yenisafak.com/rss?xml=manset',1, 7)
        AddSite(27, 'Yeni Şafak','https://www.yenisafak.com', 'yeni_safak', 'https://www.yenisafak.com/rss?xml=gundem',1, 4)
        AddSite(27, 'Yeni Şafak','https://www.yenisafak.com', 'yeni_safak', 'https://www.yenisafak.com/rss?xml=ekonomi',1, 2)
        AddSite(27, 'Yeni Şafak','https://www.yenisafak.com', 'yeni_safak', 'https://www.yenisafak.com/rss?xml=dunya',1, 1)
        #yazar# AddSite(27, 'YeniŞafak','https://www.yenisafak.com', 'yenisafak', 'https://www.yenisafak.com/rss?xml=yazarlar',1, 7)

        AddSite(28, 'Yeni Akit', 'https://www.yeniakit.com.tr', 'yeniakit', 'https://www.yeniakit.com.tr/rss/haber/gunun-mansetleri',1, 7)
        AddSite(28, 'Yeni Akit', 'https://www.yeniakit.com.tr', 'yeniakit', 'https://www.yeniakit.com.tr/rss/haber',1, 7)
        AddSite(28, 'Yeni Akit', 'https://www.yeniakit.com.tr', 'yeniakit', 'https://www.yeniakit.com.tr/rss/haber/bugunku-akit',1, 7)
        AddSite(28, 'Yeni Akit', 'https://www.yeniakit.com.tr', 'yeniakit', 'https://www.yeniakit.com.tr/rss/haber/siyaset',1, 6)
        AddSite(28, 'Yeni Akit', 'https://www.yeniakit.com.tr', 'yeniakit', 'https://www.yeniakit.com.tr/rss/haber/gundem',1, 4)
        AddSite(28, 'Yeni Akit', 'https://www.yeniakit.com.tr', 'yeniakit', 'https://www.yeniakit.com.tr/rss/haber/ekonomi',1, 2)
        AddSite(28, 'Yeni Akit', 'https://www.yeniakit.com.tr', 'yeniakit', 'https://www.yeniakit.com.tr/rss/haber/dunya',1, 1)

        AddSite(29, 'Yeni Çağ', 'http://www.yenicaggazetesi.com.tr', 'yenicaggazetesi', 'http://www.yenicaggazetesi.com.tr/rss/',1, 4)

        AddSite(30, 'Yeni Asır', 'https://www.yeniasir.com.tr', 'yeniasir', 'https://www.yeniasir.com.tr/rss/anasayfa.xml',1, 4)
        AddSite(30, 'Yeni Asır', 'https://www.yeniasir.com.tr', 'yeniasir', 'https://www.yeniasir.com.tr/rss/Ekonomi.xml',1, 2)
        AddSite(30, 'Yeni Asır', 'https://www.yeniasir.com.tr', 'yeniasir', 'https://www.yeniasir.com.tr/rss/YerelPolitika.xml',1, 6)
        AddSite(30, 'Yeni Asır', 'https://www.yeniasir.com.tr', 'yeniasir', 'https://www.yeniasir.com.tr/rss/DisHaberler.xml',1, 1)

        AddSite(31, 'Yurt Gazetesi', 'http://www.yurtgazetesi.com.tr', 'yurtgazetesi', 'http://www.yurtgazetesi.com.tr/rss.php',1, 4)
        #AddSite(32, 'YeniSöz', 'http://www.yenisoz.com.tr', 'yenisoz.com.tr', 'http://www.yenisoz.com.tr/rss/',1, 4)
        # AddSite(33, 'Sözcü', '',1, 4)
        # AddSite(34, 'Haber7', '',1, 4)
        # AddSite(35, 'GazeteVatan', '',1, 4)
        # AddSite(36, 'Akşam', '',1, 4)

def select_newsSite():
    return GetData.Site()


def insert_news(siteId, title, description, link, imageLink, pubTime, types, stem, categoryNumber, index):
    news = GetData.SelectOneNewsByLink(link)

    if news is 0:
        AddData.News(siteId, title, description, link, imageLink, pubTime, "", types, stem, categoryNumber, index)
    else:
        UpdateData.News(siteId, title, description, link, imageLink, pubTime, "", types, stem, categoryNumber)
