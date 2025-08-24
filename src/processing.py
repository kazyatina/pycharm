from typing import Dict, List


def filter_by_state(dict_list: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""
    return [x for x in dict_list if x["state"] == state]


dict_list: List[Dict] = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(filter_by_state(dict_list, "CANCELED"))


def sort_by_date(date_list: List[Dict], reverse: bool = True) -> List[Dict]:
    """Функция возвращает новый список, отсортированный по дате"""
    return sorted(date_list, key=lambda x: x["date"], reverse=reverse)


date_list: List[Dict] = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(sort_by_date(date_list))
