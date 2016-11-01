.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/parser.c

.. _`match_one`:

match_one
=========

.. c:function:: int match_one(char *s, const char *p, substring_t args[])

    - Determines if a string matches a simple pattern

    :param char \*s:
        the string to examine for presence of the pattern

    :param const char \*p:
        the string containing the pattern

    :param substring_t args:
        array of \ ``MAX_OPT_ARGS``\  \ :c:type:`struct substring_t <substring_t>`\  elements. Used to return match
        locations.

.. _`match_one.description`:

Description
-----------

Determines if the pattern \ ``p``\  is present in string \ ``s``\ . Can only
match extremely simple token=arg style patterns. If the pattern is found,
the location(s) of the arguments will be returned in the \ ``args``\  array.

.. _`match_token`:

match_token
===========

.. c:function:: int match_token(char *s, const match_table_t table, substring_t args[])

    - Find a token (and optional args) in a string

    :param char \*s:
        the string to examine for token/argument pairs

    :param const match_table_t table:
        match_table_t describing the set of allowed option tokens and the
        arguments that may be associated with them. Must be terminated with a
        \ :c:type:`struct match_token <match_token>`\  whose pattern is set to the NULL pointer.

    :param substring_t args:
        array of \ ``MAX_OPT_ARGS``\  \ :c:type:`struct substring_t <substring_t>`\  elements. Used to return match
        locations.

.. _`match_token.description`:

Description
-----------

Detects which if any of a set of token strings has been passed
to it. Tokens can include up to MAX_OPT_ARGS instances of basic c-style
format identifiers which will be taken into account when matching the
tokens, and whose locations will be returned in the \ ``args``\  array.

.. _`match_number`:

match_number
============

.. c:function:: int match_number(substring_t *s, int *result, int base)

    scan a number in the given base from a substring_t

    :param substring_t \*s:
        substring to be scanned

    :param int \*result:
        resulting integer on success

    :param int base:
        base to use when converting string

.. _`match_number.description`:

Description
-----------

Given a \ :c:type:`struct substring_t <substring_t>`\  and a base, attempts to parse the substring
as a number in that base. On success, sets \ ``result``\  to the integer represented
by the string and returns 0. Returns -ENOMEM, -EINVAL, or -ERANGE on failure.

.. _`match_int`:

match_int
=========

.. c:function:: int match_int(substring_t *s, int *result)

    - scan a decimal representation of an integer from a substring_t

    :param substring_t \*s:
        substring_t to be scanned

    :param int \*result:
        resulting integer on success

.. _`match_int.description`:

Description
-----------

Attempts to parse the \ :c:type:`struct substring_t <substring_t>`\  \ ``s``\  as a decimal integer. On
success, sets \ ``result``\  to the integer represented by the string and returns 0.
Returns -ENOMEM, -EINVAL, or -ERANGE on failure.

.. _`match_octal`:

match_octal
===========

.. c:function:: int match_octal(substring_t *s, int *result)

    - scan an octal representation of an integer from a substring_t

    :param substring_t \*s:
        substring_t to be scanned

    :param int \*result:
        resulting integer on success

.. _`match_octal.description`:

Description
-----------

Attempts to parse the \ :c:type:`struct substring_t <substring_t>`\  \ ``s``\  as an octal integer. On
success, sets \ ``result``\  to the integer represented by the string and returns
0. Returns -ENOMEM, -EINVAL, or -ERANGE on failure.

.. _`match_hex`:

match_hex
=========

.. c:function:: int match_hex(substring_t *s, int *result)

    - scan a hex representation of an integer from a substring_t

    :param substring_t \*s:
        substring_t to be scanned

    :param int \*result:
        resulting integer on success

.. _`match_hex.description`:

Description
-----------

Attempts to parse the \ :c:type:`struct substring_t <substring_t>`\  \ ``s``\  as a hexadecimal integer.
On success, sets \ ``result``\  to the integer represented by the string and
returns 0. Returns -ENOMEM, -EINVAL, or -ERANGE on failure.

.. _`match_wildcard`:

match_wildcard
==============

.. c:function:: bool match_wildcard(const char *pattern, const char *str)

    - parse if a string matches given wildcard pattern

    :param const char \*pattern:
        wildcard pattern

    :param const char \*str:
        the string to be parsed

.. _`match_wildcard.description`:

Description
-----------

Parse the string \ ``str``\  to check if matches wildcard
pattern \ ``pattern``\ . The pattern may contain two type wildcardes:
'\*' - matches zero or more characters
'?' - matches one character
If it's matched, return true, else return false.

.. _`match_strlcpy`:

match_strlcpy
=============

.. c:function:: size_t match_strlcpy(char *dest, const substring_t *src, size_t size)

    - Copy the characters from a substring_t to a sized buffer

    :param char \*dest:
        where to copy to

    :param const substring_t \*src:
        &substring_t to copy

    :param size_t size:
        size of destination buffer

.. _`match_strlcpy.description`:

Description
-----------

Copy the characters in \ :c:type:`struct substring_t <substring_t>`\  \ ``src``\  to the
c-style string \ ``dest``\ .  Copy no more than \ ``size``\  - 1 characters, plus
the terminating NUL.  Return length of \ ``src``\ .

.. _`match_strdup`:

match_strdup
============

.. c:function:: char *match_strdup(const substring_t *s)

    - allocate a new string with the contents of a substring_t

    :param const substring_t \*s:
        &substring_t to copy

.. _`match_strdup.description`:

Description
-----------

Allocates and returns a string filled with the contents of
the \ :c:type:`struct substring_t <substring_t>`\  \ ``s``\ . The caller is responsible for freeing the returned
string with \ :c:func:`kfree`\ .

.. This file was automatic generated / don't edit.

