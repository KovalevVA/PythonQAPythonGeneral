import pytest


def test_list_pop():

    '''Данная функция проверяет корректность работы метода pop() для работы со списком'''

    pop_sample_list = [1, 'two', 'three', 4, '5']
    assert pop_sample_list.pop() == '5'

def test_list_append():

    ''''Данная функция проверяет корректность работы метода append() для работы со списком'''

    append_sample_list = ['element1','element2','element3']
    append_sample_list.append('element4')
    assert append_sample_list == ['element1','element2', 'element3', 'element4']

def test_list_count():

    '''Данная функция проверяет корректность работы метода count() для работы со списком'''

    count_sample_list = ['piano', 'guitar', 'violin', 'guitar', 'drums']
    assert count_sample_list.count('guitar') == 2

def test_list_remove():

    '''Данная функция проверяет корректность работы метода remove() для работы со списком'''

    remove_sample_list = ['1', 5, '10']
    remove_sample_list.remove(5)
    assert remove_sample_list == ['1', '10']

@pytest.mark.parametrize('len_list_input, len_list_expected', [('len([1,2,3])', 3),
                                                               ("len(['C#','C++'])",2),
                                                               ("len(['MySQL','PostgreSQL'])",2)])
def test_list_len(len_list_input, len_list_expected):

    '''Данная функция проверяет правильность вычисления длины списков переданных '''

    assert eval(len_list_input) == len_list_expected