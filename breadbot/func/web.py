import os
import re
import urllib.parse
import urllib.request

from breadbot.core import common


def search_baidu(keyword):
    if not keyword:
        return
    p = {'wd': keyword}
    url = 'http://www.baidu.com/s?' + urllib.parse.urlencode(p)
    return common.url_to_html(url)


def search_corpus(keyword):
    if not keyword:
        return
    keyword = keyword.replace(' ', '+')
    url = 'https://github.com/rdp-studio/breadbot/search?q=' + keyword
    return common.url_to_html(url)


def show_homepage():
    url = 'https://ai.rdpstudio.top/#!index.md'
    name = 'AI.RDPStudio.top'
    return common.url_to_html(url, name)

def show_wiki():
    url = 'https://ai.rdpstudio.top/#!index.md'
    name = 'Wiki'
    return common.url_to_html(url, name)
