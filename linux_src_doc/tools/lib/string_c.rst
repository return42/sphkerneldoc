.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/lib/string.c

.. _`memdup`:

memdup
======

.. c:function:: void *memdup(const void *src, size_t len)

    duplicate region of memory

    :param src:
        memory region to duplicate
    :type src: const void \*

    :param len:
        memory region length
    :type len: size_t

.. _`strtobool`:

strtobool
=========

.. c:function:: int strtobool(const char *s, bool *res)

    convert common user inputs into boolean values

    :param s:
        input string
    :type s: const char \*

    :param res:
        result
    :type res: bool \*

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

    :param dest:
        Where to copy the string to
    :type dest: char \*

    :param src:
        Where to copy the string from
    :type src: const char \*

    :param size:
        size of destination buffer
    :type size: size_t

.. _`strlcpy.description`:

Description
-----------

Compatible with \*BSD: the result is always a valid
NUL-terminated string that fits in the buffer (unless,
of course, the buffer size is zero). It does not pad
out the result like \ :c:func:`strncpy`\  does.

If libc has \ :c:func:`strlcpy`\  then that version will override this

.. This file was automatic generated / don't edit.

