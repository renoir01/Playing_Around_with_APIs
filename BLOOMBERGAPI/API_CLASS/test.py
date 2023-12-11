#!/usr/bin/python3
bloom = __import__('bloombergmarketwatcher').BloombergMarketWatcher
new_object = bloom()
new_object.getCrossCurrencies()
new_object.getMovers2()
