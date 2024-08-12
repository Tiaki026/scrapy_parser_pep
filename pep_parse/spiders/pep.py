import scrapy
from pep_parse.items import PepParseItem
from pep_parse.constants import (
    NAME, ALLOWED_DOMAINS, START_URL, PEP_LINK, TITLE, STATUS
)


class PepSpider(scrapy.Spider):
    name = NAME
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URL

    def parse(self, response):
        """Извлечение ссылок на страницы PEP."""
        pep_links = response.css(PEP_LINK).getall()

        for link in pep_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Извлечение данных из страницы PEP."""
        title = response.css(TITLE).get()
        numbers, name = title.split(' – ', 1)
        number = numbers.split()[-1]
        data = {
            'number': number.strip(),
            'name': name.strip(),
            'status': response.css(STATUS).get(),
        }
        yield PepParseItem(data)
