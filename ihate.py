#!/usr/bin/env python3

import time
import sys
import requests
from lxml import etree

osearch_templates = {
    'DuckDuckGo': 'https://duckduckgo.com/ac/?q={}&type=list',
    'Google': 'https://suggestqueries.google.com/complete/search?output=firefox&q={}',
    'Bing': 'https://api.bing.com/osjson.aspx?query={}',
    'Yahoo': 'https://search.yahoo.com/sugg/os?command={}&output=fxjson&fr=opensearch'
}

religions = [
    'Catholics',
    'Christians',
    'Atheists',
    'Jehovah\'s Witnesses',
    'Mormons'
    'Muslims',
    'Hindu',
    'Buddhists',
    'Lutherans',
    'Baptists',
    'Religion',
    'Sunnis',
    'Shiites',
    'Justin Bieber'
]

races = [
    'Blacks',
    'Whites',
]

sexual = [
    'Gays',
    'Lesbians',
    'Homosexuals',
    'Straights',
    'Bisexuals',
]

politics = [
    'Feminists',
    'Liberals',
    'Conservatives',
    'Democrats',
    'Communists',
    'George Washington',
    'Abraham Lincoln',
    'Hitler',
    'George W Bush',
    'Bush',
    'Barack Obama',
    'Obama'
]

def opensearch_ihate(s, template, hate):
    q = 'I hate ' + hate
    json = s.get(template.format(q)).json()
    if len(json) < 2:
        return False
    suggestions = json[1]
    for suggestion in suggestions:
        if q.lower() == suggestion.lower():
            return True

    return False

def get_ethnicities():
    html = requests.get('https://en.wikipedia.org/wiki/List_of_contemporary_ethnic_groups').content
    html = etree.HTML(html)
    tbody = html.xpath('//table[contains(.//th/text(), "Ethnicity")]/tbody')[0]
    ret = tbody.xpath('./tr[position() > 1]/td[1]/a/text()')
    return ret

def get_nationalities():
    html = requests.get('https://en.wikipedia.org/wiki/Lists_of_people_by_nationality').content
    html = etree.HTML(html)
    tbody = html.xpath('//div[@id="mw-content-text"]/div[2]')[0]
    ret = tbody.xpath('.//a/text()')
    return ret

def main():
    hates = []
    if len(sys.argv) == 1:
        ethnicities = get_ethnicities()
        nationalities = get_nationalities()

        hates += ethnicities
        hates += nationalities
        hates += religions
        hates += races
        hates += sexual
        hates += politics

    else:
        hates.append(' '.join(sys.argv[1:]))

    hates = list(set(hates))
    hates.sort()

    s = requests.Session()
    for hate in hates:
        ihate = []
        for name, template in osearch_templates.items():
            if opensearch_ihate(s, template, hate):
                ihate.append(name)

        ihate = ' '.join(ihate)
        print('I hate {}: {}'.format(hate, ihate))

if __name__ == '__main__':
    main()
