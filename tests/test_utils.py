from utils import get_data, get_operations, date_sort, changing_the_date_display, changing_the_account_number_display

def test_get_data():
    assert get_data('test_operations.json') == [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 594226727,
    "state": "CANCELED",
    "date": "2018-09-12T21:27:25.241689",
    "operationAmount": {
      "amount": "67314.70",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Platinum 1246377376343588",
    "to": "Счет 14211924144426031657"
  },
  {
    "id": 147815167,
    "state": "EXECUTED",
    "date": "2018-01-26T15:40:13.413061",
    "operationAmount": {
      "amount": "50870.71",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на счет",
    "from": "Maestro 4598300720424501",
    "to": "Счет 43597928997568165086"
  }
]

data = get_data('test_operations.json')

def test_get_operations():
    assert len(get_operations(data)) == 2

data = get_operations(data)

def test_date_sort():
  expect = ["2018-01-26T15:40:13.413061", "2019-08-26T10:50:58.294041"]
  result = []
  data_test = date_sort(data)
  for date in data_test:
    result.append(date['date'])
  assert result == expect

def test_changing_the_date_display():
  expect = ['26.08.2019', '26.01.2018']
  result = []
  data_test = changing_the_date_display(data)
  for date in data_test:
    result.append(date['date'])
  assert result == expect

def test_changing_the_account_number_display():
  expect = ['Maestro 5968 37** **** 5199', 'Maestro 5983 00** **** 4501']
  result = []
  data_test = changing_the_account_number_display(data)
  for number in data_test:
    result.append(number['from'])
  assert result == expect