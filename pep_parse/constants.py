import datetime as dt
from pathlib import Path


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
W = 'w'
UTF8 = 'utf-8'
