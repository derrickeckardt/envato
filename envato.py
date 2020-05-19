#!/usr/bin/env python3
import requests
import pprint

# Insert personal token after Bearer
headers = {
    "Authorization" : "Bearer ",
    }

def search(request_url, query, headers):
    r = requests.get(request_url, query, headers=headers)
    return r


if __name__ == '__main__':
    # keyword search
    request_url = "https://api.envato.com/v1/discovery/search/search/item"
    query = {
        "site" : "themeforest.net",
        "term" : "ugly "
    }    
    keyword_search = search(request_url, query, headers)

    # specific item search
    request_url = "https://api.envato.com/v3/market/catalog/item"
    query = {
        "id": "16335"
    }

    item_search = search(request_url, query, headers)
    pprint.pprint(item_search.json())