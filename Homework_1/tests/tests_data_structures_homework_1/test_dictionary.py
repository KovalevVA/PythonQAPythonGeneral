import pytest

def test_dictionary_get():

    '''Данная функция проверяет корректность выполнения метода get() при работе со словарем'''

    get_sample_dictionary = {'a': 10, 'b': 20, 'c': 30}
    assert get_sample_dictionary.get('b') == 20

def test_dictionary_items():

    '''Данная функция проверяет корректность выполнения метода items() при работе со словарем'''

    items_sample_dictionary = {'a': 10, 'b': 20, 'c': 30}
    assert list(items_sample_dictionary.items())[2][1] == 30

def test_dictionary_keys():

    '''Данная функция проверяет корректность выполнения метода метода keys() при работе со словарем'''

    keys_sample_dictionary = {'a': 10, 'b': 20, 'c': 30}
    assert list(keys_sample_dictionary.keys())  == ['a', 'b', 'c']

def test_dictionary_values():

    '''Данная функция проверяет корректность выполнения метода values() при работе со словарем'''

    values_sample_dictionary = {'a': 10, 'b': 20, 'c': 30}
    assert list(values_sample_dictionary.values()) == [10,20,30]



@pytest.mark.parametrize('dict_input, dict_expected', [('{"a": 10, "b": 20, "c": 30}.popitem()', ("c", 30)),
                                                               ('{"a": 10, "b": 20}.popitem()', ("b", 20)),
                                                               ('{"a" : 10}.popitem()', ("a", 10))])

def test_dictionary_popitem(dict_input, dict_expected):

    '''Данная функция проверяет корректность выполнения метода popitem() при работе со словарем'''

    assert eval(dict_input) == dict_expected

