import pytest
from StringUtils import StringUtils

@pytest.fixture
def util():
    return StringUtils()

@pytest.mark.parametrize("input_string, expected_output", [
    ("hello", "Hello"),
    ("World", "World"),
    ("user1234", "User1234"),
    ("12345", "12345"),
    ("!hello", "!hello"),
    ("", "")
])
def test_capitilize_positive(util, input_string, expected_output):
    result = util.capitilize(input_string)
    assert result == expected_output

@pytest.mark.parametrize("input_string, expected_output", [
    ("привет, Миру Мир", "Привет, Миру Мир"),
    ("    hello", "    Hello")
    ])
@pytest.mark.xfail(reason="Метод еще в разработке")
def test_capitilize_negative(util, input_string, expected_output):
    result = util.capitilize(input_string)
    assert result == expected_output

@pytest.mark.parametrize("input_string,expected_output", [
    ("   Hello", "Hello"),
    ("World", "World"),
    ("     Hello, World!    ", "Hello, World!    "),
    ("", ""),
    ("          ", ""),
    ("  User1234", "User1234"),
    ("   12345", "12345")
    ])
def test_trim_positive(util, input_string, expected_output):
    result = util.trim(input_string)
    assert result == expected_output

@pytest.mark.xfail(reason="Метод еще в разработке")
def test_trim_negativ():
    result = util.trim(12345)
    assert result == 12345

@pytest.mark.parametrize("input_string, delimiter, expected_output", [
    ("", ",", []),
    ("1::2::3", "::", ["1", "2", "3"]),
    ("abc", "", ["a", "b", "c"]),
    ("a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z", ".", ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]),
    ("1,2,3,4,5,6,7,8,9,0", ",", ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
])
def test_to_list_positive(util, input_string, delimiter, expected_output):
    result = util.to_list(input_string, delimiter)
    assert result == expected_output

@pytest.mark.parametrize("input_string, delimiter, expected_output", [
    ("1,2,3", None, TypeError),
    ("1:2:3", 42, TypeError),
    ("", None, ValueError),
])
@pytest.mark.xfail(reason="Метод содержит баг")
def test_to_list_negative(util, input_string, delimiter, expected_output):
    result = util.to_list(input_string, delimiter)
    assert result == expected_output

@pytest.mark.parametrize("input_string, symbol, expected_output", [
    ("", "a", False),
    ("hello", "z", False),
    ("hello", "5", False),
    ("hello", " ", False),
    ("hello", "e", True),
    ("hello world", " ", True),
    ("hel123lo", "2", True),
    ("12345", "5", True),
    ("12345", "6", False),
    ("hello", "he", True),
    ("hello", "gg", False)
])
def test_contains_positiv(util, input_string, symbol, expected_output):
    result = util.contains(input_string, symbol)
    assert result == expected_output

@pytest.mark.parametrize("input_string, symbol, expected_output", [
    ("hello", 1, TypeError),
    ("", 1, TypeError),
    ])
@pytest.mark.xfail(reason="Метод содержит баг")
def test_contains_negative(util, input_string, symbol, expected_output):
    result = util.contains(input_string, symbol)
    assert result == expected_output

@pytest.mark.parametrize("input_string, symbol, expected_output", [
    ("", "a", ""),
    ("hello", "l", "heo"),
    ("hello", " ", "hello"),
    ("hello", "e", "hllo"),
    ("hello world", " ", "helloworld"),
    ("hello world", "o", "hell wrld"),
    ("hel123lo", "123", "hello"),
    ("12345", "5", "1234"),
    ("hello", "5", "hello"),
    ("hello", " ", "hello"),
    ("12345", "6", "12345"),
    ("Hello", "gg", "Hello"),
    ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", "b", "acdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"),
    ("HHHHHHH", "H", ""),
    ("      ", " ", ""),
    ("@#^%&!@#", "@", "#^%&!#")
])
def test_delete_sym_positiv(util, input_string, symbol, expected_output):
    result = util.delete_symbol(input_string, symbol)
    assert result == expected_output

@pytest.mark.parametrize("input_string, symbol, expected_output", [
    (12345, "5", AttributeError),
    ("12345", None, TypeError),
    (None, "g", AttributeError)
    ])
@pytest.mark.xfail(reason="Метод еще в разработке")
def test_delete_sym_negativ(util, input_string, symbol, expected_output):
    result = util.delete_symbol(input_string, symbol)
    assert result == expected_output
    
    
@pytest.mark.parametrize("input_string, symbol, expected_output", [
    ("", "a", False),
    ("", "", True),
    ("hello", "z", False),
    ("hello", "5", False),
    ("hello", " ", False),
    (" hello", " ", True),
    ("hel123lo", "h", True),
    ("12345", "1", True),
    ("12345", "R", False),
    ("hello", "he", True),
    ("hello", "gg", False),
    ("@#^%&!@#", "@", True),
    ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", "a", True)
    ])
def test_starts_with_positiv(util, input_string, symbol, expected_output):
    result = util.starts_with(input_string, symbol)
    assert result == expected_output

@pytest.mark.parametrize("input_string, symbol, expected_output", [
    ("hello", 1, TypeError),
    ("", 1, False),
    (12345, 1, AttributeError),
    ("12345", None, TypeError),
    (None, "g", AttributeError)
    ])
@pytest.mark.xfail(reason="Метод содержит баг")
def test_starts_with_negative(util, input_string, symbol, expected_output):
    result = util.starts_with(input_string, symbol)
    assert result == expected_output
    
@pytest.mark.parametrize("input_string, symbol, expected_output", [
    ("", "a", False),
    ("", "", True),
    ("hello", "z", False),
    ("hello", "5", False),
    ("hello", " ", False),
    ("hello ", " ", True),
    ("hel123lo", "o", True),
    ("12345", "5", True),
    ("12345", "R", False),
    ("hello", "lo", True),
    ("hello", "gg", False),
    ("@#^%&!@#", "#", True),
    ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", "9", True)
    ])
def test_end_with_positiv(util, input_string, symbol, expected_output):
    result = util.end_with(input_string, symbol)
    assert result == expected_output

@pytest.mark.parametrize("input_string, symbol, expected_output", [
    ("hello", 1, TypeError),
    ("", 1, False),
    (12345, 5, AttributeError),
    ("12345", None, TypeError),
    (None, "g", AttributeError)
    ])
@pytest.mark.xfail(reason="Метод содержит баг")
def test_end_with_negativ(util, input_string, symbol, expected_output):
    result = util.end_with(input_string, symbol)
    assert result == expected_output

@pytest.mark.parametrize("input_string, expected_output", [
    ("", True),
    ("     ", True),
    ("12345", False),
    ("@#^%&!@#", False),
    ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", False)
    ])
def test_is_empty_positiv(util, input_string, expected_output):
    result = util.is_empty(input_string)
    assert result == expected_output

@pytest.mark.parametrize("input_string, expected_output", [
    (12345, TypeError),
    (None, TypeError),
    ])
@pytest.mark.xfail(reason="Метод содержит баг")
def test_is_empty_with_negativ(util, input_string, expected_output):
    result = util.is_empty(input_string)
    assert result == expected_output
    
@pytest.mark.parametrize("input_string, joiner, expected_output", [
    ([], ",", ""),
    ([1,2,3], "::", "1::2::3"),
    (["1","2","3"], "", "123"),
    (["a","b","c"], ", ", "a, b, c"),
    (["Sky","Pro"], "", "SkyPro"),
    (["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"], ",", "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"),
    (["1","2","3","4","5","6","7","8","9","0"], ",", "1,2,3,4,5,6,7,8,9,0")
])
def test_list_to_string_positive(util, input_string, joiner, expected_output):
    result = util.list_to_string(input_string, joiner)
    assert result == expected_output

@pytest.mark.parametrize("input_string, joiner, expected_output", [
    ([1,2,3], None, TypeError),
    ("1:2:3", 42, TypeError),
    ("", None, ValueError)
])
@pytest.mark.xfail(reason="Метод содержит баг")
def test_list_to_string_negative(util, input_string, joiner, expected_output):
    result = util.list_to_string(input_string, joiner)
    assert result == expected_output