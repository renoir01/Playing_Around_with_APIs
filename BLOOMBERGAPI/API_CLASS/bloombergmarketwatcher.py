#!/usr/bin/python3
import csv
import os
import requests
import time
import urllib.parse


class BloombergMarketWatcher:

  def __init__(self):
    self.__url = "https://bloomberg-market-and-financial-news.p.rapidapi.com/market/get-movers"
    self.__headers = {
        "X-RapidAPI-Key": "11afcd18e2msh70d16f51cfb8189p1e4487jsnb40b06717259",
        "X-RapidAPI-Host":
        "bloomberg-market-and-financial-news.p.rapidapi.com",
        "user-agent": "bloomberg_app/1.0"
    }
    self.schemes = [
        "file", "ftp", "gopher", "hdl", "http", "https", "imap", "mailto",
        "mms", "news", "nntp", "prospero", "rsync", "rtsp", "rtsps", "rtspu",
        "sftp", "shttp", "sip", "sips", "snews", "svn", "svn+ssh", "telnet",
        "wais", "ws", "wss"
    ]
    self.__region = None
