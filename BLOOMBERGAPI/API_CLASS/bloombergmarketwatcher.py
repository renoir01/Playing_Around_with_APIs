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
      elif not (url_functionality.port and url_functionality.port.isdigit()
                and 0 <= int(url_functionality.port) <= 65535):
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

  @property
  def header(self):
    return self.__headers

  @header.setter
  def add_header(self, key=None, value=None):
    try:
      if key is None or value is None:
        raise ValueError(
            f"Key and Value should be of type string but Key is of type \
  {type(key)} and Value is of type {type(value)}")
      elif not isinstance(key, str) or not isinstance(value, str):
        raise TypeError(
            f"Key and Value should be of type string but Key is of type \
  {type(key)} and Value is of type {type(value)}")
    except ValueError as error_message:
      print(f"{error_message}")
      time.sleep(10)
      os.system("clear")
    except TypeError as error_message:
      print(f"{error_message}")
      time.sleep(10)
      os.system("clear")
    else:
      self.__headers[key] = value

  @property
  def region(self):
    return self.__region

  @region.setter
  def region(self, region):
    try:
      if not isinstance(region, str):
        raise TypeError(
            f"Region should be of type string but Region is of type {type(region)}"
        )
    except TypeError as error_message:
      print(f"{error_message}")
      time.sleep(10)
      os.system("clear")
    else:
      self.__region = region
      while True:
        if self.__region == "americas" or self.__region == "emea" or \
  self.__region == "apac":
          break
        else:
          print("Here is the list of regions:\n",
                "Americas\n",
                "EMEA\n",
                "APAC",
                sep="")
          self.__region = input("Enter a region: ").lower()
      time.sleep(10)
      os.system("clear")

  def __regionalLocation(self):
    print("Here is the list of regions:\n",
          "Americas\n",
          "EMEA\n",
          "APAC",
          sep="")
    self.__region = input("Enter a region: ").lower()
    while True:
      if self.__region == "americas" or self.__region == "emea" or self.__region == "apac":
        break
      else:
        self.__region = input("Enter a region: ").lower()
    os.system("clear")

  def __indexNumber(self):
    if self.__region == "americas":
      print("Here is a list of the index_name\n",
            "Enter 1 for DOW JONES INDUS. AVG\n",
            "Enter 2 for S&P 500 INDEX\n", "Enter 3 for NASDAQ COMPOSITE\n",
            "Enter 4 for NYSE COMPOSITE INDEX\n",
            "Enter 5 for S&P/TSX COMPOSITE INDEX")
      self.__index_name = input("Enter a index_number: ")
      while True:
        if self.__index_name == "1" or self.__index_name == "2" or self.__index_name == "3"\
          or self.__index_name == "4" or self.__index_name == "5":
          break
        else:
          self.__index_name = input("Enter a index_number: ")
    elif self.__region == "emea":
      print("Here is a list of the index_name\n",
            "Enter 1 for Euro Stoxx 50 Pr\n", "Enter 2 for FTSE 100 INDEX\n",
            "Enter 3 for DAX INDEX\n", "Enter 4 for CAC 40 INDEX\n",
            "Enter 5 for IBEX 35 INDEX")
      self.__index_name = input("Enter a index_number: ")
      while True:
        if self.__index_name == "1" or self.__index_name == "2" or self.__index_name == "3"\
          or self.__index_name == "4" or self.__index_name == "5":
          break
        else:
          self.__index_name = input("Enter a index_number: ")
    else:
      print("Here is a list of the index_name\n", "Enter 1 for NIKKEI 225\n",
            "Enter 2 for TOPIX INDEX (TOKYO)\n",
            "Enter 3 for HANG SENG INDEX\n", "Enter 4 for CSI 300 INDEX\n",
            "Enter 5 for S&P/ASX 200 INDEX\n",
            "Enter 6 for MSCI AC ASIA PACIFIC")
      self.__index_name = input("Enter a index_number: ")
      while True:
        if self.__index_name == "1" or self.__index_name == "2" or self.__index_name == "3"\
          or self.__index_name == "4" or self.__index_name == "5" or self.__index_name == "6":
          break
        else:
          self.__index_name = input("Enter a index_number: ").lower()
    time.sleep(10)
    os.system("clear")
 def __indexRegionMapping(self):
    if self.__region == "americas":
      america_index = {
          "1": "indu:ind",
          "2": "spx:ind",  # not working
          "3": "ccmp:ind",
          "4": "nya:ind",  # not working
          "5": "sptsx:ind"
      }
      self.__id = america_index[self.__index_name]
    elif self.__region == "emea":
      emea_index = {
          "1": "sx5e:ind",
          "2": "ukx:ind",
          "3": "dax:ind",
          "4": "cac:ind",
          "5": "ibex:ind"
      }
      self.__id = emea_index[self.__index_name]
    else:
      apac_index = {
          "1": "nky:ind",
          "2": "tpx:ind",
          "3": "hsi:ind",
          "4": "shsz300:ind",
          "5": "as51:ind",
          "6": "mxap:ind"  # not working
      }
      self.__id = apac_index[self.__index_name]

  def getMovers1(self):
    """A list of assets that made the most gains in the market."""
    # url for get movers api
    self.__regionalLocation()
    self.__indexNumber()
    self.__indexRegionMapping()

    # query parameters for the get movers api
    self.__querystring = {"id": self.__id, "template": "INDEX"}
    try:
      response = requests.get(self.__url,
                              headers=self.__headers,
                              params=self.__querystring)
    except requests.exceptions.RequestException as req_error:
      print(req_error)
      return 0
    # convert response to json format
    resp_json = response.json()
    # store the data in good format
    # first open the csv file for writing to add column headers to it.
    # ask  the user categories
    print("These are the list of categories:\n", "Active\n", "Laggards\n",
          "Leaders\n")
    category = input("Enter a category: ").lower()
    while True:
      if category == "active" or category == "laggards" or category == "leaders":
        break
      else:
        category = input("Enter a category: ").lower()
    file_name = f"{self.__region}_{self.__id}_market_watch_{category}.csv"
    with open(file_name, 'w', newline='') as csvfile:
      column_writer = csv.writer(csvfile, delimiter=' ')
      # get column keys first in a list
      try:
        column_keys = list(resp_json[category][0].keys())
      except KeyError:
        print(f"Server was unable to process the request with status code \
{resp_json['status']} and message {resp_json['message']}!!!")
        time.sleep(7)
        os.system("clear")
        return 0
      # write the column headers to the csv file
      public_columns = [
          "securitytype", "symbol", "exchange", "currency", "resourcetype",
          "name", "last", "yearhigh", "dayhigh", "volume", "yearlow", "daylow",
          "pctchangeytd"
      ]
      private_columns = []
      for column in column_keys:
        if column.lower() not in public_columns:
          continue
        private_columns.append(column)

      column_writer.writerow(private_columns)
    with open(file_name, 'a', newline='') as csvfile:
      row_len = len(resp_json[category])
      row_writer = csv.writer(csvfile,
                              delimiter=' ',
                              quotechar='"',
                              quoting=csv.QUOTE_NONNUMERIC)
      for row in range(row_len):
        row_writer.writerow([
            resp_json[category][row]['securityType'],
            resp_json[category][row]['symbol'],
            resp_json[category][row]['exchange'],
            resp_json[category][row]['currency'],
            resp_json[category][row]['resourceType'],
            resp_json[category][row]['name'], resp_json[category][row]['last'],
            resp_json[category][row]['yearHigh'],
            resp_json[category][row]['dayHigh'],
            resp_json[category][row]['volume'],
            resp_json[category][row]['yearLow'],
            resp_json[category][row]['dayLow'],
            resp_json[category][row]['pctChangeYTD']
        ])
      print(f"file successfully saved as {file_name}")
      time.sleep(3)
      os.system("clear")      
