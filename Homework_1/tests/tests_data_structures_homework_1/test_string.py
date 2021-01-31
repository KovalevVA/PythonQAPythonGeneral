import pytest


def test_string_lower():

    ''''Данная функция проверяет корректность работы метода lower() для работы со строками'''

    string_sample = 'STRING'
    assert string_sample.lower() == 'string'

def test_string_upper():

    '''Данная функция проверяет корректность работы метода upper() для работы со строками'''

    string_sample = 'string'
    assert string_sample.upper() =='STRING'


def test_string_join():

    '''Данная функция проверяет корректность работы метода join() для работы со строками'''

    string_sample = '..'
    joined_string = string_sample.join('abc')
    assert joined_string == 'a..b..c'

def test_string_format():

    '''Данная функция проверяет корректность работы метода format() для работы со строками'''

    sample_string = '{} {} {} {} testing'
    assert sample_string.format('This', 'is', 'a', 'string' ) == 'This is a string testing'

@pytest.mark.parametrize('string_input, string_expected', [('"Unicorn".split("corn")', ['Uni', '']),
                                                               ('"ASCII_CODE".split("_")', ['ASCII', 'CODE'])])
def test_string_spilt(string_input, string_expected):

    '''Данная функция проверяет корректность работы метода split() для работы со строками'''

    assert eval(string_input) == string_expected