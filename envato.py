#!/usr/bin/env python3
import requests

request_url = "https://api.envato.com/v1/discovery/search/search/item"
headers = {
    "Authorization" : "Bearer oVi4yPxk1bJ64Y2qOsLJ2D2ZlC3FpK4L",
    }

post = {
    "site" : "themeforest.net",
    "term" : "awesome"
}    

def item_search(request_url, headers, post):
    r = requests.post(request_url, headers=headers, json=post)
    return r

item = item_search(request_url, headers, post)

print(item)