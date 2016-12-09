import textwrap
from unittest.mock import patch

import sumtri

# unit tests

def get_3_line_input():
    return textwrap.dedent("""\
        3
        1
        2 1
        1 2 3
    """)

def get_4_line_input():
    return textwrap.dedent("""\
        4
        1
        1 2
        4 1 2
        2 3 1 1
    """)

def get_input():
    myinput = "2\n" + get_3_line_input() + get_4_line_input()
    return iter(myinput.splitlines())

def get_rows():
    return [
        [1],
        [2, 1],
        [1, 2, 3],
    ]

def get_graph():
    """
      1
     4  2
    8 16 32
    """
    d = sumtri.Node(8, None, None)
    e = sumtri.Node(16, None, None)
    f = sumtri.Node(32, None, None)

    b = sumtri.Node(4, d, e)
    c = sumtri.Node(2, e, f)

    return sumtri.Node(1, b, c)

def test_all_paths():
    graph = get_graph()

    actual = sumtri.all_paths(graph)

    assert list(actual) == [
        [1, 4, 8],
        [1, 4, 16],
        [1, 2, 16],
        [1, 2, 32],
    ]

def test_to_graph():
    myrows = get_rows()

    actual = sumtri.to_graph(myrows)

    assert actual.value == 1
    assert actual.left.value == 2
    assert actual.right.value == 1
    assert actual.left.left.value == 1
    assert actual.left.right.value == 2
    assert actual.left.right is actual.right.left
    assert actual.right.right.value == 3

def test_to_graph_one_node():
    actual = sumtri.to_graph([ [123] ])

    assert actual.value == 123
    assert actual.left is None
    assert actual.right is None

def test_read_case_should_read_stream_to_create_lists_of_values():
    myinput = iter("""\
        3
        1
        2 1
        1 2 3
        end
    """.splitlines())

    actual = sumtri.read_case(myinput)

    assert actual == get_rows()
    assert next(myinput).strip() == 'end'

@patch('sumtri.read_case', lambda _: 'case')
def test_read_cases_should_return_a_list_of_cases():
    myinput = get_input()

    actual = sumtri.read_cases(myinput)

    # read_cases should return an iterable,
    # with as many elements as the first number in myinput
    # Each element should be whatever is returned by read_case()
    assert list(actual) == ['case', 'case']


# integration tests

def test_main_integration(capsys):
    myinput = get_input()

    sumtri.main(myinput)

    out, err = capsys.readouterr()
    assert out == '5\n9\n'

