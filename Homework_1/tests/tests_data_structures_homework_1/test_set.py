import pytest


def test_set_remove():

    ''''Данная функция проверяет корректность работы метода remove() для работы с множеством'''

    set_sample_remove = set('hello!')
    set_sample_remove.remove('!')
    assert set_sample_remove == {'h','e','l','o'}

def test_set_intersection():

    '''Данная функция проверяет корректность работы метода intersection() для работы с множеством'''

    set_sample_1_intersect = set('hello!')
    set_sample_2_intersect = set('hola!')
    assert set_sample_1_intersect.intersection(set_sample_2_intersect) == {'!','h','l','o'}


def test_set_differnce():

    '''Данная функция проверяет корректность работы метода diffrence() для работы с множеством'''

    set_sample_1_diff = set('hello!')
    set_sample_2_diff = set('hola!')

    assert set_sample_1_diff.difference(set_sample_2_diff) == {'e'}

def test_set_copy():

    '''Данная функция проверяет корректность работы метода copy() для работы с множеством'''

    sample_set1_copy = set('pytest')
    sample_set2_copy = sample_set1_copy.copy()
    assert sample_set1_copy == sample_set2_copy

@pytest.mark.parametrize('set_input, set_expected', [('{1,2,3,4,5}.union({6,7,8})', {1,2,3,4,5,6,7,8}),
                                                               ('{"hello world"}.union({"world"})',{'hello world', 'world'})])
def test_set_union(set_input, set_expected):

    '''Данная функция проверяет корректность работы метода union() для множеств'''

    assert eval(set_input) == set_expected