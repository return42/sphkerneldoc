.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/lib/string.c

.. _`memdup`:

memdup
======

.. c:function:: void *memdup(const void *src, size_t len)

    duplicate region of memory

    :param const void \*src:
        memory region to duplicate

    :param size_t len:
        memory region length

.. _`strtobool`:

strtobool
=========

.. c:function:: int strtobool(const char *s, bool *res)

    convert common user inputs into boolean values

    :param const char \*s:
        input string

    :param bool \*res:
        result

.. _`strtobool.description`:

Description
-----------

This routine returns 0 iff the first character is one of 'Yy1Nn0', or
[oO][NnFf] for "on" and "off". Otherwise it will return -EINVAL.  Value
pointed to by res is updated upon finding a match.

.. _`strlcpy`:

strlcpy
=======

.. c:function:: size_t strlcpy(char *dest, const char *src, size_t size)

    Copy a C-string into a sized buffer

    :param char \*dest:
        Where to copy the string to

    :param const char \*src:
        Where to copy the string from

    :param size_t size:
        size of destination buffer

.. _`strlcpy.description`:

Description
-----------

Compatible with \*BSD: the result is always a valid
NUL-terminated string that fits in the buffer (unless,
of course, the buffer size is zero). It does not pad
out the result like \ :c:func:`strncpy`\  does.

If libc has \ :c:func:`strlcpy`\  then that version will override this

.. This file was automatic generated / don't edit.

