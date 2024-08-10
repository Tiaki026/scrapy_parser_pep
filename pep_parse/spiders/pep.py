import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        """Извлечение ссылок на страницы PEP."""
        pep_links = response.css('tbody tr td a::attr(href)').getall()

        for link in pep_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Извлечение данных из страницы PEP."""
        title = response.css('h1.page-title::text').get()
        numbers, name = title.split(' – ', 1)
        number = numbers.split()[-1]
        data = {
            'number': number.strip(),
            'name': name.strip(),
            'status': response.css('dd.field-even abbr::text').get(),
        }
        yield PepParseItem(data)
