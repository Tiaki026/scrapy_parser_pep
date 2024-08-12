import csv
from collections import defaultdict

from pep_parse.settings import (
    BASE_DIR, FILE_NAME, ITEM_STATUS,
    RESULTS, STATUS_COUNT, TOTAL, UTF8, WRITE
)


class PepParsePipeline:

    def open_spider(self, spider):
        """Начало работы "паука".
        Создает папку results для сохранения данных.
        Сохраняет файл status_summary."""
        self.results_dir = BASE_DIR / RESULTS
        self.results_dir.mkdir(exist_ok=True)
        self.file_path = self.results_dir / FILE_NAME
        self.count_status = defaultdict(int)

    def process_item(self, item, spider):
        """Процесс "паука".
        Считает количество статусов."""
        self.count_status[item[ITEM_STATUS]] += 1
        return item

    def close_spider(self, spider):
        """Завершение работы "паука".
        Записывает данные в csv-файл в два столбца:Статус и Количество.
        Добавляет в конце строку Total с общим количеством PEP."""
        self.count_status[TOTAL] = sum(self.count_status.values())

        with open(self.file_path, mode=WRITE, encoding=UTF8, newline='') as f:
            writer = csv.writer(f)
            writer.writerow(STATUS_COUNT)
            writer.writerows([
                (status, count) for status, count in self.count_status.items()
            ])
