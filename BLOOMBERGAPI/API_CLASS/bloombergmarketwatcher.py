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

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        try:
            url_functionality = urllib.parse.urlparse(url)
            if url_functionality.scheme not in self.schemes:
                raise ValueError("Invalid Scheme.")
            elif url_functionality.netloc == "":
                raise ValueError("Invalid Netloc or web page name.")
            elif not (url_functionality.port and url_functionality.port.isdigit() and 0 <= int(url_functionality.port) <= 65535):
                raise ValueError("Invalid port in the URL")
        except ValueError as error_message:
        """
        The except block for ValueError
        catches these errors that may occur
        1. if an invalid port is specified in the URL
        2. Unmatched square brackets in the netloc attribute are found
        3. Characters in the netloc attribute that decompose under NFKC normalization
            (as used by the IDNA encoding) into any of /, ?, #, @, or :
        4. Invalid Scheme.
        5. Invalid Netloc or web page name.
        """
        print(f"{error_message}")
        time.sleep(10)
        os.system("clear")
        else:
            self.__url = url
            print(f"URL successfully set to {url}")
            time.sleep(10)
            os.system("clear")
