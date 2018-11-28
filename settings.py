"""
title:config item of project in this code page
date:2018-11-12
author:doug zhnag
description:

"""


import os
from enum import Enum, unique

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LIBRARY_BASE_PATH = os.path.join(BASE_DIR,'library')

SCRAPER_SLEEP_TIME = 5

MY_DOMAIN = 'Athereshopping.com'
ALIEXPRESS_DOMAIN = 'Aliexpress.com | Alibaba Group'


@unique
class Browser(Enum):
    CHROME = 1
    FIREFOX = 2


BASE_BROWSER = Browser.CHROME
