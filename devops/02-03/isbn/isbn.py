def transform_isbn(isbn):
    """Transform ISBN and perform simple checks.
    Parameters
    ----------
        isbn
            the ISBN10 or ISBN13 number to be transformed
    Returns
    -------
        Transformed ISBN
    """
    # Make lowercase for convenience
    isbn = isbn.lower()

    # Remove spaces and dashes
    isbn = isbn.strip().replace("-", "").replace(" ", "")

    return isbn


def validate_isbn(isbn, isbn_size=None):
    """Validate the ISBN.
    Perform simple checks on the ISBN format without calculating the checksum yet.
    Parameters
    ----------
        isbn
            the ISBN10 or ISBN13 number to be validated
        isbn_size
            either 10 or 13 for ISBN10 and ISBN13 respectively, or None (unspecified)
    Returns
    -------
        bool
            Whether the ISBN passed the checks.
    """
    # All characters except the last one need to be numerical
    if not isbn[:-1].isnumeric():
        return False

    # The string needs to be 10 or 13 characters long.
    if isbn_size:
        if len(isbn) != isbn_size:
            return False
    else:  # not specified whether ISBN10 or ISBN13
        if len(isbn) != 10 and len(isbn) != 13:
            return False

    # The last character needs to be either 'x' or a digit
    if isbn[-1] != 'x' and not isbn[-1].isnumeric():
        return False

    return True


def is_valid_isbn10(isbn):
    a = list(isbn)
    b = len(a) - 1
    for i in b:
        a[i]=a[i]*i
        i = i+1
    c=0
    i=0
    for i in b:
        c = c+a[i]
        i = i+1
    if c%11 == 10:
        return a[b+1]




    """Check if the ISBN is a valid ISBN-10.
    # 1. Take all elements except the last one.
    # 2. Multiply each of these by their position (digit 1 x 1, digit 2 x 2, ..., digit 9 x 9).
    # 3. Sum the results.
    # 4. Take last result % (modulo) 11
    # 5. If the result is 10, the last digit should be 'x'; else keep the modulo result as the last digit.
    """
    # TODO: implement this function
    return False


def is_valid_isbn13(isbn):
    """Check if the ISBN is a valid ISBN-13."""

    # Checksum
    checksum_odd = sum(int(n) for i, n in enumerate(isbn[:-1]) if (i+1) % 2 == 1)
    checksum_even = sum(3 * int(n) for i, n in enumerate(isbn[:-1]) if (i + 1) % 2 == 0)
    checksum = checksum_odd + checksum_even
    last_digit = (10 - checksum % 10) % 10

    return isbn[-1] == str(last_digit)


def is_valid_isbn(isbn, isbn_type=None):
    """Check if the ISBN is a valid ISBN-10 or ISBN-13."""

    isbn = transform_isbn(isbn)

    if not validate_isbn(isbn, isbn_size=isbn_type):
        return False

    if isbn_type is None:
        return is_valid_isbn10(isbn) or is_valid_isbn13(isbn)

    if isbn_type == 10:
        return is_valid_isbn10(isbn)
    return is_valid_isbn13(isbn)