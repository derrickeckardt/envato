#!/usr/bin/env python3
import requests
import pprint

request_url = "https://api.envato.com/v1/discovery/search/search/item"
headers = {
    "Authorization" : "Bearer ",
    }


query = {
    "site" : "themeforest.net",
    "term" : "awesome"
}    


def item_search(request_url, headers, query):
    r = requests.get(request_url, headers=headers, query)
    return r


if __name__ == '__main__':
    item = item_search(request_url, headers, query)
    pprint.pprint(item.json())