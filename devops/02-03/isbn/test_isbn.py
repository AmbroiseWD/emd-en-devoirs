import pytest

from isbn import is_valid_isbn


def test_is_valid_isbn10(isbn,expected):
    result = test_is_valid_isbn10(isbn,isbn_type=10)
    # TODO: impelement this test with a list of input parameters (isbn, expected).
    assert result == expected


@pytest.mark.parametrize(
    "isbn,expected",
    [
        ("9780470059029", True),
        ("978 0 471 48648 0", True),
        ("978-0596809485", True),
        ("978-0-13-149505-0", True),
        ("978-0-262-13472-9", True),
        ("9780470059028", False),
        ("978 0 471 48648 X", False),
        ("978-0596809486", False),
        ("978-0-13-149505-1", False),
        ("978-0-262-13472-7", False)
    ]
)
def test_is_valid_isbn13(isbn, expected):
    result = is_valid_isbn(isbn, isbn_type=13)
    assert result == expected


@pytest.mark.parametrize(
    "isbn,expected",
    [
        ("abcdefghij", False),  # not numeric
        ("0471958697", True),
        ("0 471 60695 2", True),
        ("0-470-84525-2", True),
        ("0-321-14653-0", True),
        ("04719586977", False),  # too long
        ("0471958690", False),  # bad checksum
        ("123456789X", True),  # LAST ISBN-10 test
        ("9780470059029", True),  # FIRST ISBN-13 test
        ("978 0 471 48648 0", True),
        ("978-0596809485", True),
        ("978-0-13-149505-0", True),
        ("978-0-262-13472-9", True),
        ("9780470059028", False),
        ("978 0 471 48648 X", False),
        ("978-0596809486", False),
        ("978-0-13-149505-1", False),
        ("978-0-262-13472-7", False)
    ]
)
def test_is_valid_isbn_is_type_unspecified(isbn, expected):
    result = is_valid_isbn(isbn, isbn_type=None)
    assert result == expected