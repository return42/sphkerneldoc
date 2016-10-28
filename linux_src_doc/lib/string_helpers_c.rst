.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/string_helpers.c

.. _`string_get_size`:

string_get_size
===============

.. c:function:: void string_get_size(u64 size, u64 blk_size, const enum string_size_units units, char *buf, int len)

    get the size in the specified units

    :param u64 size:
        The size to be converted in blocks

    :param u64 blk_size:
        Size of the block (use 1 for size in bytes)

    :param const enum string_size_units units:
        units to use (powers of 1000 or 1024)

    :param char \*buf:
        buffer to format to

    :param int len:
        length of buffer

.. _`string_get_size.description`:

Description
-----------

This function returns a string formatted to 3 significant figures
giving the size in the required units.  \ ``buf``\  should have room for
at least 9 bytes and will always be zero terminated.

.. _`string_unescape`:

string_unescape
===============

.. c:function:: int string_unescape(char *src, char *dst, size_t size, unsigned int flags)

    unquote characters in the given string

    :param char \*src:
        source buffer (escaped)

    :param char \*dst:
        destination buffer (unescaped)

    :param size_t size:
        size of the destination buffer (0 to unlimit)

    :param unsigned int flags:
        combination of the flags (bitwise OR):
        \ ``UNESCAPE_SPACE``\ :
        '\f' - form feed
        '\n' - new line
        '\r' - carriage return
        '\t' - horizontal tab
        '\v' - vertical tab
        \ ``UNESCAPE_OCTAL``\ :
        '\NNN' - byte with octal value NNN (1 to 3 digits)
        \ ``UNESCAPE_HEX``\ :
        '\xHH' - byte with hexadecimal value HH (1 to 2 digits)
        \ ``UNESCAPE_SPECIAL``\ :
        '\"' - double quote
        '\\' - backslash
        '\a' - alert (BEL)
        '\e' - escape
        \ ``UNESCAPE_ANY``\ :
        all previous together

.. _`string_unescape.description`:

Description
-----------

The function unquotes characters in the given string.

Because the size of the output will be the same as or less than the size of
the input, the transformation may be performed in place.

Caller must provide valid source and destination pointers. Be aware that
destination buffer will always be NULL-terminated. Source string must be
NULL-terminated as well.

.. _`string_unescape.return`:

Return
------

The amount of the characters processed to the destination buffer excluding
trailing '\0' is returned.

.. _`string_escape_mem`:

string_escape_mem
=================

.. c:function:: int string_escape_mem(const char *src, size_t isz, char *dst, size_t osz, unsigned int flags, const char *only)

    quote characters in the given memory buffer

    :param const char \*src:
        source buffer (unescaped)

    :param size_t isz:
        source buffer size

    :param char \*dst:
        destination buffer (escaped)

    :param size_t osz:
        destination buffer size

    :param unsigned int flags:
        combination of the flags (bitwise OR):
        \ ``ESCAPE_SPACE``\ : (special white space, not space itself)
        '\f' - form feed
        '\n' - new line
        '\r' - carriage return
        '\t' - horizontal tab
        '\v' - vertical tab
        \ ``ESCAPE_SPECIAL``\ :
        '\\' - backslash
        '\a' - alert (BEL)
        '\e' - escape
        \ ``ESCAPE_NULL``\ :
        '\0' - null
        \ ``ESCAPE_OCTAL``\ :
        '\NNN' - byte with octal value NNN (3 digits)
        \ ``ESCAPE_ANY``\ :
        all previous together
        \ ``ESCAPE_NP``\ :
        escape only non-printable characters (checked by isprint)
        \ ``ESCAPE_ANY_NP``\ :
        all previous together
        \ ``ESCAPE_HEX``\ :
        '\xHH' - byte with hexadecimal value HH (2 digits)

    :param const char \*only:
        NULL-terminated string containing characters used to limit
        the selected escape class. If characters are included in \ ``only``\ 
        that would not normally be escaped by the classes selected
        in \ ``flags``\ , they will be copied to \ ``dst``\  unescaped.

.. _`string_escape_mem.description`:

Description
-----------

The process of escaping byte buffer includes several parts. They are applied
in the following sequence.
1. The character is matched to the printable class, if asked, and in
case of match it passes through to the output.
2. The character is not matched to the one from \ ``only``\  string and thus
must go as-is to the output.
3. The character is checked if it falls into the class given by \ ``flags``\ .
\ ``ESCAPE_OCTAL``\  and \ ``ESCAPE_HEX``\  are going last since they cover any
character. Note that they actually can't go together, otherwise
\ ``ESCAPE_HEX``\  will be ignored.

Caller must provide valid source and destination pointers. Be aware that
destination buffer will not be NULL-terminated, thus caller have to append
it if needs.

.. _`string_escape_mem.return`:

Return
------

The total size of the escaped output that would be generated for
the given input and flags. To check whether the output was
truncated, compare the return value to osz. There is room left in
dst for a '\0' terminator if and only if ret < osz.

.. This file was automatic generated / don't edit.

