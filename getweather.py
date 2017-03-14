#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :


#python getweather.py f31ca1fb328a9f22
import urllib2
import sys
import bs4
import json


#api_key=None #good option
api_key="f31ca1fb328a9f22"

class WetherClient(object):
    url_base="http://api.wunderground.com/api/"
    url_sevice={"almanac": "/almanac/q/CA/",
                "hourly":"/hourly/q/CA/",
                "conditions":"/conditions/q/CA/"}
    def __init__(self, api_key):
        self.api_key = api_key
    def temperatures(self,location):
        #obtenir http://api.wunderground.com/api/f31ca1fb328a9f22/almanac/q/CA/San_Francisco.json
        #obtenir la url
        url=WetherClient.url_base+self.api_key +\
            WetherClient.url_sevice["hourly"] +\
            location + "." + "json"
        web = urllib2.urlopen(url)
        page = web.read()
        web.close()
        #processar dades
        #print page
        data = json.loads(page)
        last_temp = 0
        print "Mostrando temperatura a lo largo del dia"
        for hourly in data["hourly_forecast"]:
            time = hourly["FCTTIME"]["civil"]
            temperature = hourly["temp"]["metric"]
            print "Hora: " + time + " Tempeatura: " + temperature + " C"
            last_temp = temperature

        if last_temp < "0":
            print "Hace mucho frio, tapate todo lo que puedas"
        elif last_temp < "12":
            print "Hace frio, tapate"
        elif last_temp < "20":
            print "Refresca un poco, ponte un jersey"
        else:
            print "Hoy es un buen dia, disfruta de la calor"
    def condition(self,location):
        #obtenir la url
        url=WetherClient.url_base+self.api_key +\
            WetherClient.url_sevice["conditions"] +\
            location + "." + "json"
        web = urllib2.urlopen(url)
        page = web.read()
        web.close()
        #processar dades
        data = json.loads(page)
        condit = data["current_observation"]["weather"]
        print "Y recuerda, el cielo esta " + condit

if __name__ == '__main__':
    if not api_key:
        try:
            api_key=sys.argv[1]
        except IndexError:
            print "La API a la linea de comandes"
    wc = WetherClient(api_key)
    wc.temperatures("Lleida")
    wc.condition("Lleida")
