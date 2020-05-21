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
        "category": "cms-themes",
        "sort_by": "updated",
        "sort_direction": "asc",
        "page_size" : "10",
        "page" : "60"
    }    
    keyword_search = search(request_url, query, headers)
    next_page_url = keyword_search.json()#['links']#['next_page_url']
    pprint.pprint(next_page_url)


    # specific item search
    request_url = "https://api.envato.com/v3/market/catalog/item"
    query = {
        "id": "12170274"
    }
    item_search = search(request_url, query, headers)
    # pprint.pprint(item_search.json())
    
    # Popular by Site
    request_url = "https://api.envato.com/v1/market/popular:themeforest.json"
    site_popular = requests.get(request_url, headers=headers)
    # pprint.pprint(site_popular.json())
    
    # Categories by Site
    request_url = "https://api.envato.com/v1/market/categories:themeforest.json"
    categories = requests.get(request_url,headers=headers)
    # print(categories.json())