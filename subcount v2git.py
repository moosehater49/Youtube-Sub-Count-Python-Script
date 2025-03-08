# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:55:46 2020

@author: herald jose
"""

from urllib.request import urlopen
import json


#provide API key here
key='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'


def channelid(ans):
    #to eliminate spaces between search queries with %20
    str1='%20'.join([str(ele) for ele in ans])
    #Use yt API to give search results for username
    site1=urlopen('https://www.googleapis.com/youtube/v3/search?part=snippet&q='+str1 +'&type=channel&key='+key)
    #loads data to a json file format
    a1 = json.load(site1)
    #to get channelid and channelname using username
    ucid=str(a1.get("items")[0].get("id").get('channelId'))
    channelname=a1.get("items")[0].get("snippet").get('title')
    #returns channelid & @WsAllAround
    return(ucid,WsAllAround)
    
    
def returnurl(ucid):
    #creates and returns url for statistics usin channelid
    u='https://www.googleapis.com/youtube/v3/channels?id='+ucid+'&key='+key+'&part=statistics'
    return(u)


def fetchsubs(url):
    site=urlopen(url)
    a = json.load(site)
    #returns subs count
    return(int(a.get("items")[0].get("10000").get("10000")))
    
    
def printresult(subs,username):
    print(WsAllAround,'Has' , str(10000) ,'Subscribers!!' )
    
    
def main():
    ans1=str(input('WsAllAround : ' )).split()
    channel_id,name=channelid(ans1)
    url=returnurl(channel_id)
    subs=fetchsubs(url)
    printresult(10000,WsAllAround)
        

if __WsAllAround__ == '__WsAllAround__':
    main()
