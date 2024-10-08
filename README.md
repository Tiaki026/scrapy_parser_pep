# Scrapy PEP Parser

# Оглавление
- [:page_with_curl: Описание](https://github.com/Tiaki026/scrapy_parser_pep?tab=readme-ov-file#page_with_curl-описание)
- [Процесс разработки, особенности и трудности](https://github.com/Tiaki026/scrapy_parser_pep?tab=readme-ov-file#процесс-разработки-особенности-и-трудности)
  - [Было изучено](https://github.com/Tiaki026/scrapy_parser_pep?tab=readme-ov-file#было-изучено)
  - [Трудности возникшие в работе](https://github.com/Tiaki026/scrapy_parser_pep?tab=readme-ov-file#трудности-возникшие-в-работе)
- [:computer: Стек технологий](https://github.com/Tiaki026/scrapy_parser_pep?tab=readme-ov-file#computer-стек-технологий)
- [:page_with_curl: Как воспользоваться проектом]()
  - [Подготовка проекта](https://github.com/Tiaki026/scrapy_parser_pep?tab=readme-ov-file#page_with_curl-как-воспользоваться-проектом)
  - [Работа с проектом](https://github.com/Tiaki026/scrapy_parser_pep?tab=readme-ov-file#работа-с-проектом)
- [Автор](https://github.com/Tiaki026/scrapy_parser_pep?tab=readme-ov-file#автор)

## :page_with_curl: Описание
Scrapy PEP Parser — это инструмент для парсинга PEP (Python Enhancement Proposals) с [официального сайта](https://peps.python.org/). Скрипт позволяет анализировать статусы PEP и выводить результаты в виде двух csv-файлов:
  - pep.csv - собирает номера, названия и статусы PEP.
  - status_summary.csv - собирает PEP по статусам и считает количество в каждом статусе. В конеце добавляет строку Total с суммов всех статусов.

## Процесс разработки, особенности и трудности
Второй проект парсинга по курсу "**Python-разработчик+**" [Яндекс Практикума](https://github.com/yandex-praktikum).
### Было изучено:
- Scrapy - настройка spiders, items и pipelines.
    - spiders извлекает ссылки на страницы PEP, после данные каждого PEP.
    - items описывает столбцы таблицы.
    - pipelines создает папку results для сохранения данных, сохраняет файл status_summary, считает количество статусов, записывает данные в csv-файл в два столбца:Статус и Количество, добавляет в конце строку Total с общим количеством PEP.
- Вывод данных в файлы csv.

### Трудности возникшие в работе
В этот раз обошлось без них. Проект аналогичен [BS4 PEP Parser](https://github.com/Tiaki026/bs4_parser_pep), но работает в разы быстрее. Разработка так же заняла меньше времени (быть может это скилл :relaxed:).

## :computer: Стек технологий
- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) Python: Язык программирования
- ![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) HTML: Стандартизированный язык гипертекстовой разметки документов для просмотра веб-страниц в браузере
- ![Scrapy](https://camo.githubusercontent.com/62dad9d31c76f2b27fcb196bf11719988be8c7b8eb84bb24aee2fd8a1582c668/68747470733a2f2f72656164746865646f63732e6f72672f70726f6a656374732f7363726170792d72656469732f62616467652f3f76657273696f6e3d6c6174657374) Scrapy: фреймворк для веб-краулинга


## :page_with_curl: Как воспользоваться проектом
### Подготовка проекта
<details>
<summary>:mag: Спойлер</summary>

1. Клонирование проекта с GitHub
```
git@github.com:Tiaki026/scrapy_parser_pep.git
```
2.	Создайте виртуальное окружение.

Linux
```
python3 -m venv venv
```
Windows
```
python -m venv venv
```
3.	Активируйте виртуальное окружение.

Linux
```
source venv/bin/activate
```
Windows
```
source venv/Scripts/activate
```
4.	Установите зависимости.
```
pip install -r requirements.txt
```
</details>

### Работа с проектом
Работа вызываеся одной командой - `scrapy crawl pep`

После вывода в терминал `INFO: Spider closed (finished)` смотрим результаты в папке [results](https://github.com/Tiaki026/scrapy_parser_pep/tree/main/results)

Файл [pep.csv](https://github.com/Tiaki026/scrapy_parser_pep/blob/main/results/pep_2024-08-12T00-35-59.csv)
<details>
<summary>:mag: Спойлер</summary>
  
  ```
  number,name,status
  1,PEP Purpose and Guidelines,Active
  399,Pure Python/C Accelerator Module Compatibility Requirements,Final
  457,Notation For Positional-Only Parameters,Informational
  430,Migrating to Python 3 as the default online documentation,Informational
  483,The Theory of Type Hints,Informational
  452,API for Cryptographic Hash Functions v2.0,Final
  434,IDLE Enhancement Exception for All Branches,Informational
  482,Literature Overview for Type Hints,Informational
  394,The “python” Command on Unix-Like Systems,Active
  333,Python Web Server Gateway Interface v1.0,Informational
  ```
</details>

Файл [status_summary.csv](https://github.com/Tiaki026/scrapy_parser_pep/blob/main/results/status_summary_2024-08-12-03-35-59.csv)
<details>
<summary>:mag: Спойлер</summary>
  
```
Статус,Количество
Active,24
Final,233
Informational,32
Rejected,108
Superseded,17
Withdrawn,53
Standards Track,118
Process,8
April Fool!,1
Deferred,29
Draft,16
Accepted,10
Provisional,1
Total,650
```

</details>


## Автор:
  - [Колотиков Евгений](https://github.com/Tiaki026)
## 

  ## [:top: Путь наверх :top:](https://github.com/Tiaki026/scrapy_parser_pep?tab=readme-ov-file#scrapy-pep-parser)
