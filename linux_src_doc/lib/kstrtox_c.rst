.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/kstrtox.c

.. _`kstrtoull`:

kstrtoull
=========

.. c:function:: int kstrtoull(const char *s, unsigned int base, unsigned long long *res)

    convert a string to an unsigned long long

    :param s:
        The start of the string. The string must be null-terminated, and may also
        include a single newline before its terminating null. The first character
        may also be a plus sign, but not a minus sign.
    :type s: const char \*

    :param base:
        The number base to use. The maximum supported base is 16. If base is
        given as 0, then the base of the string is automatically detected with the
        conventional semantics - If it begins with 0x the number will be parsed as a
        hexadecimal (case insensitive), if it otherwise begins with 0, it will be
        parsed as an octal number. Otherwise it will be parsed as a decimal.
    :type base: unsigned int

    :param res:
        Where to write the result of the conversion on success.
    :type res: unsigned long long \*

.. _`kstrtoull.description`:

Description
-----------

Returns 0 on success, -ERANGE on overflow and -EINVAL on parsing error.
Used as a replacement for the obsolete simple_strtoull. Return code must
be checked.

.. _`kstrtoll`:

kstrtoll
========

.. c:function:: int kstrtoll(const char *s, unsigned int base, long long *res)

    convert a string to a long long

    :param s:
        The start of the string. The string must be null-terminated, and may also
        include a single newline before its terminating null. The first character
        may also be a plus sign or a minus sign.
    :type s: const char \*

    :param base:
        The number base to use. The maximum supported base is 16. If base is
        given as 0, then the base of the string is automatically detected with the
        conventional semantics - If it begins with 0x the number will be parsed as a
        hexadecimal (case insensitive), if it otherwise begins with 0, it will be
        parsed as an octal number. Otherwise it will be parsed as a decimal.
    :type base: unsigned int

    :param res:
        Where to write the result of the conversion on success.
    :type res: long long \*

.. _`kstrtoll.description`:

Description
-----------

Returns 0 on success, -ERANGE on overflow and -EINVAL on parsing error.
Used as a replacement for the obsolete simple_strtoull. Return code must
be checked.

.. _`kstrtouint`:

kstrtouint
==========

.. c:function:: int kstrtouint(const char *s, unsigned int base, unsigned int *res)

    convert a string to an unsigned int

    :param s:
        The start of the string. The string must be null-terminated, and may also
        include a single newline before its terminating null. The first character
        may also be a plus sign, but not a minus sign.
    :type s: const char \*

    :param base:
        The number base to use. The maximum supported base is 16. If base is
        given as 0, then the base of the string is automatically detected with the
        conventional semantics - If it begins with 0x the number will be parsed as a
        hexadecimal (case insensitive), if it otherwise begins with 0, it will be
        parsed as an octal number. Otherwise it will be parsed as a decimal.
    :type base: unsigned int

    :param res:
        Where to write the result of the conversion on success.
    :type res: unsigned int \*

.. _`kstrtouint.description`:

Description
-----------

Returns 0 on success, -ERANGE on overflow and -EINVAL on parsing error.
Used as a replacement for the obsolete simple_strtoull. Return code must
be checked.

.. _`kstrtoint`:

kstrtoint
=========

.. c:function:: int kstrtoint(const char *s, unsigned int base, int *res)

    convert a string to an int

    :param s:
        The start of the string. The string must be null-terminated, and may also
        include a single newline before its terminating null. The first character
        may also be a plus sign or a minus sign.
    :type s: const char \*

    :param base:
        The number base to use. The maximum supported base is 16. If base is
        given as 0, then the base of the string is automatically detected with the
        conventional semantics - If it begins with 0x the number will be parsed as a
        hexadecimal (case insensitive), if it otherwise begins with 0, it will be
        parsed as an octal number. Otherwise it will be parsed as a decimal.
    :type base: unsigned int

    :param res:
        Where to write the result of the conversion on success.
    :type res: int \*

.. _`kstrtoint.description`:

Description
-----------

Returns 0 on success, -ERANGE on overflow and -EINVAL on parsing error.
Used as a replacement for the obsolete simple_strtoull. Return code must
be checked.

.. _`kstrtobool`:

kstrtobool
==========

.. c:function:: int kstrtobool(const char *s, bool *res)

    convert common user inputs into boolean values

    :param s:
        input string
    :type s: const char \*

    :param res:
        result
    :type res: bool \*

.. _`kstrtobool.description`:

Description
-----------

This routine returns 0 iff the first character is one of 'Yy1Nn0', or
[oO][NnFf] for "on" and "off". Otherwise it will return -EINVAL.  Value
pointed to by res is updated upon finding a match.

.. This file was automatic generated / don't edit.

