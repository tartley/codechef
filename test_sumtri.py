from textwrap import dedent
from unittest.mock import patch

import sumtri

# unit tests

def get_3_line_input():
    return dedent("""\
        3
        1
        2 3
        7 5 4
    """)

def get_4_line_input():
    return dedent("""\
        4
        1
        1 2
        4 1 2
        2 3 1 1
    """)

def get_input():
    myinput = "2\n" + get_3_line_input() + get_4_line_input()
    return iter(myinput.splitlines())

def get_case(length):
    assert 0 <= length < 4
    return [
        [1],
        [2, 3],
        [7, 5, 4],
    ][:length]

def test_read_case_should_read_stream_to_create_lists_of_values():
    myinput = iter((get_3_line_input() + 'end').splitlines())

    actual = sumtri.read_case(myinput)

    assert actual == get_case(3)
    assert next(myinput).strip() == 'end'

@patch('sumtri.read_case')
def test_read_cases_should_return_a_list_of_cases(my_read_case):
    my_read_case.side_effect = ['case1', 'case2']
    myinput = get_input()

    actual = sumtri.read_cases(myinput)

    assert list(actual) == ['case1', 'case2']

def test_get_parents():
    assert sumtri.get_parents([], 0) == [0]
    assert sumtri.get_parents([1], 0) == [1]
    assert sumtri.get_parents([1], 1) == [1]
    assert sumtri.get_parents([2, 3], 0) == [2]
    assert sumtri.get_parents([2, 3], 1) == [2, 3]
    assert sumtri.get_parents([2, 3], 2) == [3]

def test_new_maxes():
    assert sumtri.new_maxes([], [1]) == [1]
    assert sumtri.new_maxes([1], [2, 3]) == [3, 4]
    assert sumtri.new_maxes([3, 4], [7, 5, 4]) == [10, 9, 8]

def test_get_max_path_one_row():
    case = [[1]]
    actual = sumtri.get_max_path(case)
    assert actual == 1

def test_get_max_path():
    case = [[1], [2, 3]]
    actual = sumtri.get_max_path(case)
    assert actual == 4


# integration tests

def test_main_integration(capsys):
    myinput = get_input()

    sumtri.main(myinput)

    out, err = capsys.readouterr()
    assert out == '10\n9\n'

