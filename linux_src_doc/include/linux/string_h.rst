.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/string.h

.. _`sysfs_match_string`:

sysfs_match_string
==================

.. c:function::  sysfs_match_string( _a,  _s)

    matches given string in an array

    :param _a:
        array of strings
    :type _a: 

    :param _s:
        string to match with
    :type _s: 

.. _`sysfs_match_string.description`:

Description
-----------

Helper for \__sysfs_match_string(). Calculates the size of \ ``a``\  automatically.

.. _`strstarts`:

strstarts
=========

.. c:function:: bool strstarts(const char *str, const char *prefix)

    does \ ``str``\  start with \ ``prefix``\ ?

    :param str:
        string to examine
    :type str: const char \*

    :param prefix:
        prefix to look for.
    :type prefix: const char \*

.. _`kbasename`:

kbasename
=========

.. c:function:: const char *kbasename(const char *path)

    return the last part of a pathname.

    :param path:
        path to extract the filename from.
    :type path: const char \*

.. _`memcpy_and_pad`:

memcpy_and_pad
==============

.. c:function:: void memcpy_and_pad(void *dest, size_t dest_len, const void *src, size_t count, int pad)

    Copy one buffer to another with padding

    :param dest:
        Where to copy to
    :type dest: void \*

    :param dest_len:
        The destination buffer size
    :type dest_len: size_t

    :param src:
        Where to copy from
    :type src: const void \*

    :param count:
        The number of bytes to copy
    :type count: size_t

    :param pad:
        Character to use for padding if space is left in destination.
    :type pad: int

.. This file was automatic generated / don't edit.

