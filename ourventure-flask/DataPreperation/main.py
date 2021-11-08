import sqlite3
from bs4 import BeautifulSoup
import os
import re
import time
from pprint import pprint
import json
import requests


def get_name_targets():
    # This function reads wikipedia and wiktionary, it then looks for valid name categories (ones with more than 50 results) and passes them to a list.
    # This list is then returned to main, and added to the next function which reads every category for the names within
    # https://en.wikipedia.org/wiki/Category:Feminine_given_names
    urls = ["https://en.wikipedia.org/wiki/Category:Feminine_given_names", "https://en.wiktionary.org/wiki/Category:Female_given_names_by_language",
            "https://en.wikipedia.org/wiki/Category:Masculine_given_names", "https://en.wiktionary.org/wiki/Category:Male_given_names_by_language"]
    #viable_links = {urls[0]: [], urls[1]: [], urls[2]: [], urls[3]: []}
    viable_links = []
    for url in urls:
        #print(url)
        #print(viable_links)
        html = requests.get(url)
        soup = BeautifulSoup(html.text, "html.parser")
        start_text = url[0:url.find(".org") + 4]
        # Returns all subcategory names on wikipedia, need to extract names (e.g. <a title="Category:Vietnamese" extract the cultural name)
        section = soup.find("div", {"id": "mw-subcategories"}).findAll("div", {"class": "CategoryTreeItem"})
        print("Section type is : ", type(section))
        for i in section:
            sec = i.find("span", {"dir": "ltr"})
            #print("Section is : ", sec.text)
            sec = list(map(int, re.findall("\d+", sec.text)))
            if max(sec) > 55 and "unisex" not in i.a.text.lower():
                #print(i.a.text.lower(), max(sec))
                final_text = start_text + i.a["href"]
                #print(final_text)
                viable_links.append(final_text)
                #viable_links[url].append(i.a.text.lower().replace("-language", ""))
                #viable_links.append(i.a.text.lower().replace("-language", ""))
                #TODO: replace with dict
            #print(sec)
    #pprint(viable_links, width=120, compact=True, sort_dicts=False)
    #print(viable_links)
    print(viable_links[-3])        
    return viable_links
    
def read_targets(values):
    print("Looping over values, looking for names")
    


def read_wiktionary():
    url = "https://en.wiktionary.org"
    print()

def get_female_values():
    print()

def get_male_values():
    print()




if __name__ == '__main__':
    # The BS4 code should read over the wikipedia entries, the wiktionary entries, and one other entry
    # Reads wikipedia into json or df object
    start = time.time()
    name_values = get_name_targets()
    print(name_values)
    #TODO: Split list before for loop
    female_list = list(filter(lambda k: "_feminine_" in k.lower() or "_female_" in k.lower(), name_values))
    male_list = list(filter(lambda k: "_masculine_" in k.lower() or "_male_" in k.lower(), name_values))
    print(female_list, "\n\n\n", male_list)
    # for v in name_values:
    #     if "feminine" in v.lower() or "female" in v.lower():
    #         print(v)
    #         get_female_values()
    #     elif "masculine" in v.lower() or "male" in v.lower():
    #         print(v)
    #         get_male_values()
    print(f"Time taken to read targets ... {time.time() - start} ")
    output_values = read_targets(values=name_values)
    #print(wikipedia_values)