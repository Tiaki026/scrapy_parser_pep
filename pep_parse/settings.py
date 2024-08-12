import datetime as dt
from pathlib import Path


BOT_NAME = "pep_parse"

SPIDER_MODULES = ["pep_parse.spiders"]
NEWSPIDER_MODULE = "pep_parse.spiders"

ROBOTSTXT_OBEY = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
ASYNCIO_EVENT_LOOP = 'asyncio.SelectorEventLoop'
FEED_EXPORT_ENCODING = "utf-8"

NAME = "pep"
ALLOWED_DOMAINS = ["peps.python.org"]
START_URL = ["https://peps.python.org/"]

PEP_LINK = 'tbody tr td a::attr(href)'
TITLE = 'h1.page-title::text'
STATUS = 'dd.field-even abbr::text'

BASE_DIR = Path(__file__).parent.parent
RESULTS = 'results'
DT_FILE = dt.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
FILE_NAME = f'status_summary_{DT_FILE}.csv'
STATUS_COUNT = 'Статус,Количество\n'
ITEM_STATUS = 'status'
TOTAL = 'Total'
WRITE = 'w'
UTF8 = 'utf-8'

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
