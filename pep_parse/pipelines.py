from itemadapter import ItemAdapter
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).parent


class PepParsePipeline:

    def open_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        file_name = 'status_summary_%(time)s.csv'
        self.file_path = results_dir / file_name
        self.count_status = defaultdict(int)

    def process_item(self, item, spider):
        self.count_status[item['status']] += 1
        return item

    def close_spider(self, spider):
        self.count_status['Total'] = sum(self.count_status.values())
        for status, count in self.count_status.items():
            self.results.append((status, count))
        with open(self.file_path, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            f.write(f'Total,{self.results}\n')
